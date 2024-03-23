# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 14:03:29 2024

@author: Dobrucki
"""

from cornLeafHealth.config.configuration import ConfigurationManager
from cornLeafHealth.components.prepare_base_model import PrepareBaseModel
from cornLeafHealth import logger

STAGE_NAME = "Prepare base model"

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()



if __name__ == '__main__':
    
    try:
        logger.info(f">> STAGE {STAGE_NAME} started <<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">> STAGE {STAGE_NAME} completed <<")
    except Exception as e:
        raise e