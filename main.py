from cornLeafHealth import logger
from cornLeafHealth.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cornLeafHealth.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cornLeafHealth.pipeline.stage_03_model_training import ModelTrainingPipeline
from cornLeafHealth.pipeline.stage_04_model_evaluation import ModelEvaluationPipeline


if __name__ == '__main__':
    
    STAGE_NAME = "Data Ingestion"
    try:
        logger.info(f">> STAGE {STAGE_NAME} started <<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">> STAGE {STAGE_NAME} completed <<")
    except Exception as e:
        raise e
        
    STAGE_NAME = "Prepare base model"   
    try:
        logger.info(f">> STAGE {STAGE_NAME} started <<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">> STAGE {STAGE_NAME} completed <<")
    except Exception as e:
        raise e
        
    STAGE_NAME = "Model training"   
    try:
        logger.info(f">> STAGE {STAGE_NAME} started <<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">> STAGE {STAGE_NAME} completed <<")
    except Exception as e:
        raise e
       
    STAGE_NAME = "Model evaluation" 
    try:
        logger.info(f">> STAGE {STAGE_NAME} started <<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">> STAGE {STAGE_NAME} completed <<")
    except Exception as e:
        raise e



