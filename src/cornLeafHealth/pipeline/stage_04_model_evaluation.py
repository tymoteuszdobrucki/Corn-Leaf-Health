from cornLeafHealth.config.configuration import ConfigurationManager
from cornLeafHealth.components.model_evaluation import Evaluation
from cornLeafHealth import logger

STAGE_NAME = "Model Evaluation"

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(config=eval_config)
        evaluation.evaluation()
        evaluation.log_into_mlflow()


if __name__ == '__main__':
    
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
        
        