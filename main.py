from cornLeafHealth import logger
from cornLeafHealth.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cornLeafHealth.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cornLeafHealth.pipeline.stage_03_model_training import ModelTrainingPipeline
from cornLeafHealth.pipeline.stage_04_model_evaluation import ModelEvaluationPipeline


if __name__ == '__main__':
    
    STAGE_NAME = "Data Ingestion"
    try:
        logger.info("#########################################")
        logger.info(f"STAGE ---> {STAGE_NAME} <--- STARTED...")
        logger.info("#########################################")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info("#########################################")
        logger.info(f"STAGE ---> {STAGE_NAME} <--- COMPLETED.")
        logger.info("#########################################")
    except Exception as e:
        raise e
        
    STAGE_NAME = "Model Preparation"   
    try:
        logger.info("############################################")
        logger.info(f"STAGE ---> {STAGE_NAME} <--- STARTED...")
        logger.info("############################################")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info("############################################")
        logger.info(f"STAGE ---> {STAGE_NAME} <--- COMPLETED.")
        logger.info("############################################")
    except Exception as e:
        raise e        
        
    STAGE_NAME = "Model Training"   
    try:
        logger.info("#########################################")
        logger.info(f"STAGE ---> {STAGE_NAME} <--- STARTED...")
        logger.info("#########################################")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info("#########################################")
        logger.info(f"STAGE ---> {STAGE_NAME} <--- COMPLETED.")
        logger.info("#########################################")
    except Exception as e:
        raise e
        
    STAGE_NAME = "Model Evaluation" 
    try:
        logger.info("###########################################")
        logger.info(f"STAGE ---> {STAGE_NAME} <--- STARTED...")
        logger.info("###########################################")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info("###########################################")
        logger.info(f"STAGE ---> {STAGE_NAME} <--- COMPLETED.")
        logger.info("###########################################")
    except Exception as e:
        raise e
        



