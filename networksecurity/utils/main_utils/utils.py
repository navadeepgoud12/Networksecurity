import yaml
import os,sys
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
import dill
import numpy as np
import pandas as pd

import pickle

def read_yaml_file(file_path:str)->dict:
    """
    Docstring for read_yaml_file
    
    :param file_path: Description
    :type file_path: str
    :return: Description
    :rtype: dict
    read the yaml file and return the contents as dictionary
    """
    try:
        with open(file_path,"rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise NetworkSecurityException(e,sys) from e
    


def write_yaml_file(file_path:str,content:object,replace=False)->None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,"w") as yaml_file:
            yaml.dump(content,yaml_file)
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    
def save_numpy_array_data(file_path:str,array:np.array):
    """
    save numpy array to data file
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,"wb") as file_obj:
            np.save(file_obj,array)
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    
# to picke the object
def save_object(file_path:str,obj:object) -> None:
    """
    file_path: str location of the file to save
    obj: object to save
    return None
    """
    try:
        logging.info("enter into the save_object method of utils module to pickle the object")
        
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)
        logging.info("exit from the save_object method of utils module after pickling the object")
    except Exception as e:
        raise NetworkSecurityException(e,sys)