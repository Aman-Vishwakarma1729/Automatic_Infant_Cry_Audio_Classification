import os
import sys
from src.logger import logging
from src.exception import CustomException
from src.utils import load_object
import librosa
import librosa.display
import warnings
warnings.filterwarnings("ignore")
import time
import numpy as np
import pandas as pd


def load_models():
    try:
        logging.info("Loading models for prediction on given input data")
        artifacts_folder_path = os.path.join(os.getcwd(),'artifacts')
        encoder_model_path = os.path.join(artifacts_folder_path,'encoder_model.pkl')
        scaler_model_path = os.path.join(artifacts_folder_path,'scaler_model.pkl')
        predictor_model_path = os.path.join(artifacts_folder_path,'predictor_model.pkl')
        encoder = load_object(encoder_model_path)
        scaler = load_object(scaler_model_path)
        model = load_object(predictor_model_path)
        logging.info(f"Sucesfully loaded models\nencoder:{encoder}\nscaler:{scaler}\npredictor model{model}")
        return encoder,scaler,model
    except Exception as e:
        logging.info("Exception occured while loading models for prediction")
        raise CustomException(e,sys)

def prediction_pipeline(audio_file_path):
    try:
        logging.info("Prediction procees for input data starts")
        encoder,scaler,model = load_models()
        audio_file = audio_file_path
        logging.info(f"The input audio data path:\n{audio_file}")
        audio,sample_rate = librosa.load(audio_file)
        mffcs_features = librosa.feature.mfcc(y=audio,sr=sample_rate,n_mfcc=40)
        mfccs_scaled_features = np.mean(mffcs_features.T,axis=0)
        logging.info(f"The mfccs scaled features for input file:\n{mfccs_scaled_features}")
        features_df= pd.DataFrame(mfccs_scaled_features.reshape(1, -1), columns=[f"Feature_{i+1}" for i in range(40)])
        scaled_input = scaler.transform(features_df)
        pred_output = model.predict(scaled_input)
        encoded_label = pred_output[0]
        class_name = encoder.inverse_transform([encoded_label])[0]
        result = class_name
        logging.info(f"The result for the input data is:{result}")
        return result
    except Exception as e:
        logging.info("Exception occured while predicting result for given input")


