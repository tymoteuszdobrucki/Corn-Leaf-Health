from cornLeafHealth.config.configuration import ConfigurationManager
from cornLeafHealth.components.data_ingestion import DataIngestion
from cornLeafHealth import logger

STAGE_NAME = "Data Ingestion"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip()

if __name__ == '__main__':
    
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