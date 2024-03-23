# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 14:03:29 2024

@author: Dobrucki
"""

from cornLeafHealth.config.configuration import ConfigurationManager
from cornLeafHealth.components.model_training import Training
from cornLeafHealth import logger

STAGE_NAME = "Model training"

class ModelTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()



if __name__ == '__main__':
    
    try:
        logger.info(f">> STAGE {STAGE_NAME} started <<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">> STAGE {STAGE_NAME} completed <<")
    except Exception as e:
        raise e
        
        