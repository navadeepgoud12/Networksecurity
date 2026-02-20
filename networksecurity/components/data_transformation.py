import os,sys
import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer
from networksecurity.constant import training_pipeline
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from sklearn.pipeline import Pipeline
from networksecurity.entity.artifacts_entity import(
    DataTransformationArtifact,
    DataValidationArtifact
) 

from networksecurity.constant.training_pipeline import TARGET_COLUMN
from networksecurity.constant.training_pipeline import DATA_TRANSFORMATION_IMPUTER_PARAMS
from networksecurity.utils.main_utils.utils import save_numpy_array_data,save_object
from networksecurity.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self,data_validation_artifact:DataValidationArtifact,
                 data_transformation_config:DataTransformationConfig):
        try:
            logging.info("data transformation class has been started")
            self.data_vaidation_artifact:DataValidationArtifact = data_validation_artifact
            self.data_transformation_config:DataTransformationConfig = data_transformation_config
        except Exception as e:
            raise NetworkSecurityException(e,sys) from e
        
    # static method to read the data from the file path
    @staticmethod
    def read_data(file_path:str)->pd.DataFrame:
        try:
            logging.info('reading the data from the file path')
            return pd.read_csv(file_path)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def get_data_trasformation_object(self)->Pipeline:
        try:
            logging.info("enterd into get data transformation object")
            imputer:KNNImputer = KNNImputer(**DATA_TRANSFORMATION_IMPUTER_PARAMS)
            logging.info(f"knn imputer has been created with {DATA_TRANSFORMATION_IMPUTER_PARAMS} parameters")
            processor:Pipeline = Pipeline([("knn_imputer",imputer)])
            return processor
        except Exception as e:
            raise NetworkSecurityException(e,sys) from e
        
    #initiating the data transformation pipeline
    def initiate_data_transformation(self)->DataTransformationArtifact:
        logging.info("initiating the data transformation method")
        try:
            logging.info("data transformation has been started")
            train_df = DataTransformation.read_data(self.data_vaidation_artifact.valid_train_file_path)
            test_df = DataTransformation.read_data(self.data_vaidation_artifact.valid_test_file_path)

            # separating the dependent and independent features
            # traingdata
            input_feature_train_df = train_df.drop(columns=[TARGET_COLUMN],axis=1)
            target_feature_train_df = train_df[TARGET_COLUMN]
            target_feature_train_df = target_feature_train_df.replace(-1,0)
            # test data
            input_feature_test_df = test_df.drop(columns=[TARGET_COLUMN],axis=1)
            target_feature_test_df = test_df[TARGET_COLUMN]
            target_feature_test_df = target_feature_test_df.replace(-1,0)

            preprocessor = self.get_data_trasformation_object()
            # fitting the preprocessor object on the training and testing data
            preprocessor_object = preprocessor.fit(input_feature_train_df)
            transformed_input_train_feature = preprocessor_object.transform(input_feature_train_df)
            transformed_input_test_feature = preprocessor_object.transform(input_feature_test_df)

            train_arr = np.c_[transformed_input_train_feature,np.array(target_feature_train_df)]
            test_arr = np.c_[transformed_input_test_feature,np.array(target_feature_test_df)]

            # save the transformed object file
            save_numpy_array_data(self.data_transformation_config.transformed_train_file_path,array=train_arr)
            save_numpy_array_data(self.data_transformation_config.transformed_test_file_path,array=test_arr)
            save_object(self.data_transformation_config.transformed_object_file_path,preprocessor_object)

            # preparing the artifacts
            data_transformation_artifact = DataTransformationArtifact(
                transformed_object_file_path=self.data_transformation_config.transformed_object_file_path,
                transformed_train_file_path=self.data_transformation_config.transformed_train_file_path,
                transformed_test_file_path=self.data_transformation_config.transformed_test_file_path
            )
            
            logging.info(f"Data transformation artifact: {data_transformation_artifact}")
            return data_transformation_artifact

        except Exception as e:
            raise NetworkSecurityException(e,sys)

