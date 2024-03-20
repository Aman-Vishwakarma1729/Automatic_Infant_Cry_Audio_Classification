import os
import sys
from src.logger import logging
from src.exception import CustomException
from src.utils import create_folder
from dataclasses import dataclass
import pandas as pd
import librosa
import librosa.display
import warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
import IPython.display as ipd
import time
import numpy as np



@dataclass

class data_extraction_from_audio_config:
    extracted_data_path = os.path.join('artifacts','audio_signals.csv')

class data_extraction_from_audio:
    def __init__(self):
        self.data_extraction_from_audio_config = data_extraction_from_audio_config()
    
    def get_audio_data_folder_path(self):
        try:
            main_directory = os.getcwd()
            audio_data_folder_path = os.path.join(main_directory,"Audio_Data")
            logging.info(f"Succesfully got the path to folder containing audio data\n{audio_data_folder_path}")
            return audio_data_folder_path
        except Exception as e:
            logging.info("An exception occured while getting path of audio data folder")
            raise CustomException(e,sys)
        
    def get_child_discomfort_categories(self):
        try:
            audio_data_folder_path = self.get_audio_data_folder_path()
            audio_data_categories_raw = os.listdir(audio_data_folder_path)
            audio_data_categories = []
            for i in audio_data_categories_raw:
                cat = i.replace("_"," ")
                cat = " ".join(word.capitalize() for word in cat.split())
                audio_data_categories.append(cat)
            logging.info(f"We have following categories of audio data\n{audio_data_categories}")
            return audio_data_categories_raw, audio_data_categories
        except Exception as e:
            logging.info("An exception occured while getting categoy names")
            raise CustomException(e,sys)
        
    def get_mfccs(self,audio_file_path):
        try:
            audio,sample_rate = librosa.load(audio_file_path)
            mffcs_features = librosa.feature.mfcc(y=audio,sr=sample_rate,n_mfcc=40)
            mfccs_scaled_features = np.mean(mffcs_features.T,axis=0)
            logging.info(f"The MFCCs scaled features for,\n{audio_file_path} is:\n{mfccs_scaled_features}")
            return mfccs_scaled_features
        except Exception as e:
            logging.info(f"An exception occured while extracting MFCCs data from {audio_file_path} audio")
            raise CustomException(e,sys)
    
    def feature_extractor(self):
        try:
            audio_data_categories_raw, audio_data_categories = self.get_child_discomfort_categories()
            audio_data_folder_path = self.get_audio_data_folder_path()
            extracted_features = []
            for cat in audio_data_categories_raw:
                logging.info(f"Feature extraction is started for {cat} category")
                audio_cat_folder_path = os.path.join(audio_data_folder_path,cat)
                for file in os.listdir(audio_cat_folder_path):
                    if file.endswith('.wav') or file.endswith('.mp3'):
                        logging.info(f"Extracting feature for: {file}")
                        audio_file_path = os.path.join(audio_cat_folder_path,file)
                        mfccs_scaled_features = self.get_mfccs(audio_file_path)
                        extracted_features.append([cat,mfccs_scaled_features])
            logging.info(f"Here is the extracted features of audio data: \n {extracted_features}")
            return extracted_features
        except Exception as e:
            logging.info(f"Exception occured while extracting features frm audio")
            raise CustomException(e,sys)
    
    def get_dataframe(self):
        try:
            extracted_features = self.feature_extractor()
            features_and_class_data = pd.DataFrame(extracted_features,columns=['Class','Features'])
            features_and_class_data_exploded = features_and_class_data.explode("Features")
            for i in range(40):
                features_and_class_data[f"Feature_{i+1}"] = features_and_class_data["Features"].apply(lambda x: x[i] if len(x) > i else None)
            features_and_class_data.drop(columns=["Features"], inplace=True)
            create_folder("artifacts")
            logging.info(f"The dataframe containing features looks like:\n{features_and_class_data.head()}")
            features_and_class_data.to_csv(self.data_extraction_from_audio_config.extracted_data_path,index=False,header=True)
            return self.data_extraction_from_audio_config.extracted_data_path
        except Exception as e:
            logging.info("Exception occured while creating dataframe of features dataset")
            raise CustomException(e,sys)