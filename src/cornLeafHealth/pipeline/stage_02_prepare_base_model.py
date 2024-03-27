from cornLeafHealth.config.configuration import ConfigurationManager
from cornLeafHealth.components.prepare_base_model import PrepareBaseModel
from cornLeafHealth import logger

STAGE_NAME = "Model Preparation"

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