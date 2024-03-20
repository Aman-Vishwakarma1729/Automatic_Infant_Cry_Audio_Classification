
import os
import sys
import pickle
from src.exception import CustomException
from src.logger import logging
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
    except Exception as e:
        logging.info(f"An Exception occured while saving {obj}")
        raise CustomException(e, sys)
  
def load_object(file_path):
    try:
        with open(file_path,'rb') as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        logging.info('Exception occured in load_object function in utils')
        raise CustomException(e,sys)
