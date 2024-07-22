from src.mlproject.logger import logging
from src.mlproject.exceptions import CustomException   
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_ingestion import DataIngestionConfig
import sys

if __name__ == "__main__":

    logging.info("the execution has started")

try:
#    data_ingestion = DataIngestionConfig()
    data_ingestion = DataIngestion()
    data_ingestion.initiate_dataIngestion()

except Exception as e:
    logging.info("Custom Exception")
    raise CustomException(e,sys)
