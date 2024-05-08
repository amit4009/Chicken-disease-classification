from src.chicken_disease_classifier import logger
from src.chicken_disease_classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME="Data Ingestion Stage"

try:
    logger.info(f">>>>>>stage{STAGE_NAME} started <<<<<<")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>staget {STAGE_NAME} completed<<<<<<\n\nx==========")
        
except Exception as e:
    logger.exception(e)
    raise e
