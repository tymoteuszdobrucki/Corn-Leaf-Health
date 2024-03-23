from cornLeafHealth.config.configuration import ConfigurationManager
from cornLeafHealth.components.model_evaluation import Evaluation
from cornLeafHealth import logger

STAGE_NAME = "Model evaluation"

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
        logger.info(f">> STAGE {STAGE_NAME} started <<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">> STAGE {STAGE_NAME} completed <<")
    except Exception as e:
        raise e
        
        