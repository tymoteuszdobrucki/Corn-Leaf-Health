# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 22:16:06 2024

@author: Dobrucki
"""

from cornLeafHealth import logger
from cornLeafHealth.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


logger.info("testing the logger")




if __name__ == '__main__':
    
    try:
        logger.info(f">> STAGE {STAGE_NAME} started <<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">> STAGE {STAGE_NAME} completed <<")
    except Exception as e:
        raise e