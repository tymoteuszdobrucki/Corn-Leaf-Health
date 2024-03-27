from cornLeafHealth.config.configuration import ConfigurationManager
from cornLeafHealth.components.model_training import Training
from cornLeafHealth import logger

STAGE_NAME = "Model Training"

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
        
        