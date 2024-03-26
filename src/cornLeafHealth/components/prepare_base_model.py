# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 14:57:44 2024

@author: Dobrucki
"""

import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
from pathlib import Path
from cornLeafHealth.entity.config_entity import PrepareBaseModelConfig


class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig):
        self.config = config
    
    def get_base_model(self):
        self.model = tf.keras.applications.vgg16.VGG16(
            input_shape=self.config.params_image_size,
            weights=self.config.params_weights,
            include_top=self.config.params_include_top
            )
        
        self.save_model(path=self.config.base_model_path, model=self.model)
        
        
    @staticmethod
    def _prepare_full_model(model, classes, freeze_all, freeze_till, learning_rate):
        if freeze_all:
            for layer in model.layers:
                model.trainable=False
        elif (freeze_till is not None) and (freeze_till > 0):
            for layer in model.layers[:-freeze_till]:
                model.trainable=False
        
        flatten_in = tf.keras.layers.Flatten()(model.output)
        prediction = tf.keras.layers.Dense(units=classes, activation="softmax")(flatten_in)
        
        full_model = tf.keras.models.Model(inputs=model.input, outputs=prediction)
        
        # alternative model architecture (no transfer learning)
        alternative_model = tf.keras.models.Sequential([
            tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224,224,3)),
            tf.keras.layers.MaxPooling2D((2, 2)),
            tf.keras.layers.Conv2D(64, kernel_size=(3, 3), activation='relu'),
            tf.keras.layers.MaxPooling2D((2, 2)),
            tf.keras.layers.Conv2D(64, kernel_size=(3, 3), activation='relu'),
            tf.keras.layers.MaxPooling2D((2, 2)),
            tf.keras.layers.Conv2D(64, kernel_size=(3, 3), activation='relu'),
            tf.keras.layers.MaxPooling2D((2, 2)),
            tf.keras.layers.Conv2D(64, kernel_size=(3, 3), activation='relu'),
            tf.keras.layers.MaxPooling2D((2, 2)),
            tf.keras.layers.Conv2D(64, kernel_size=(3, 3), activation='relu'),
            tf.keras.layers.MaxPooling2D((2, 2)),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(classes, activation='softmax'),

])
        full_model = alternative_model
        
        full_model.compile(
            #optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
            optimizer='adam',
            loss=tf.keras.losses.CategoricalCrossentropy(),
            metrics=["accuracy"]
            )
        
        full_model.summary()
        return full_model
    
    def update_base_model(self):
        self.full_model = self._prepare_full_model(
            model=self.model,
            classes=self.config.params_classes,
            freeze_all=True,
            freeze_till=None,
            learning_rate=self.config.params_learning_rate
            )
        
        self.save_model(path=self.config.updated_base_model_path, model=self.full_model)
        
        
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)