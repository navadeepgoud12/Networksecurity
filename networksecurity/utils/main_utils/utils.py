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