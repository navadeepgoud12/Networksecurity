from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from networksecurity.entity.config_entity import TrainingPipelineConfig,DataInjestionConfig
from networksecurity.entity.artifacts_entity import DataIngestionArtifact
from networksecurity.components.data_ingestion import DataIngestion
import os
import sys

if __name__ == "__main__":
    try:
        TrainingPipelineConfig = TrainingPipelineConfig()
        DataInjestionConfig = DataInjestionConfig(TrainingPipelineConfig)
        dataingestion = DataIngestion(DataInjestionConfig)
        logging.info("Starting data ingestion")
        dataingestionartifact = dataingestion.initiate_data_ingestion()
        logging.info(f"Data ingestion completed and artifact is {dataingestionartifact}")
        print(dataingestionartifact)
    except Exception as e:
        raise NetworkSecurityException(e,sys)