from src.chicken_disease_classifier import logger
from src.chicken_disease_classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.chicken_disease_classifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.chicken_disease_classifier.pipeline.stage_03_training import ModelTrainingPipeline
from src.chicken_disease_classifier.pipeline.stage_04_evaluation import EvaluationPipeline



STAGE_NAME="Data Ingestion Stage"

try:
    logger.info(f">>>>>>stage{STAGE_NAME} started <<<<<<")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>staget {STAGE_NAME} completed<<<<<<\n\nx==========")
        
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME=" Prepare base model"
try:
    logger.info(f" *************")
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<")
    prepare_base_model=PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>> stage{STAGE_NAME} completed <<<<\n\nx=====x")
    
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Training"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_trainer = ModelTrainingPipeline()
   model_trainer.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Evaluation stage"
try:
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_evalution = EvaluationPipeline()
   model_evalution.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
        logger.exception(e)
        raise e