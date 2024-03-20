
import os
import sys
import pickle
from src.exception import CustomException
from src.logger import logging

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

def create_folder(folder_name):
    try:
        main_directory = os.getcwd()
        folder_path = os.path.join(main_directory,folder_name)
        if not os.path.exists(folder_path):
           os.makedirs(folder_path)
           logging.info(f"{folder_name} folder is created")
        else:
           logging.info("Folder already exists:", folder_name)
    except Exception as e:
        logging.info(f"Exception occured during creating folder: {folder_name}")
        raise CustomException(e,sys)

def delete_folder(folder_path):
  try:
    for root, dirs, files in os.walk(folder_path):
      for file in files:
        os.remove(os.path.join(root, file))
      for dir in dirs:
        os.rmdir(os.path.join(root, dir))
    os.removedirs(folder_path)
    logging.info("Folder deleted:", folder_path)
  except OSError as error:
    logging.info(f"Exception occured while deleting folder: {folder_path}")
    raise CustomException(e,sys)

 