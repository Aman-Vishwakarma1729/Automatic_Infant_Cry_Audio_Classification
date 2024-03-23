import os 
import sys
from dataclasses import dataclass
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from src.utils import save_object
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,recall_score,precision_score

@dataclass
class data_transformation_model_building_config:
    encoder_model_path = os.path.join('artifacts','encoder_model.pkl')
    scaler_model_path = os.path.join('artifacts','scaler_model.pkl')
    predictor_model_path = os.path.join('artifacts','predictor_model.pkl')

class data_transformation_model_building:
    def __init__(self):
        self.data_transformation_model_building_config = data_transformation_model_building_config()
    
    def data_encoder(self,data):
        try:
            logging.info("Encoding target variable")
            encoder = LabelEncoder()
            target = "Class"
            logging.info(f"Target variable before encoding:\n{data[target]}")
            data[target] = list(encoder.fit_transform(data[target]))
            logging.info(f"Target variable after encoding:\n{data[target]}")
            save_object(
                file_path = self.data_transformation_model_building_config.encoder_model_path,
                obj = encoder
            )
            logging.info(f"Encoder model saved to the path:\n{self.data_transformation_model_building_config.encoder_model_path}")
            return data
        except Exception as e:
            logging.info('Exception occured during encoding target variabel')
            raise CustomException(e,sys)
        
    def data_scaling(self,X_train,X_test):
        try:
            logging.info("Scaling the data using standard scling technique")
            scaler = StandardScaler()
            X_train_scaled = scaler.fit_transform(X_train)
            logging.info(f"Training input data after scaling:\n{X_train_scaled}")
            X_test_scaled = scaler.transform(X_test)
            logging.info(f"Test input data after scaling:\n{X_test_scaled}")
            save_object(
                file_path = self.data_transformation_model_building_config.scaler_model_path,
                obj = scaler
            )
            logging.info(f"Scaler model saved to path:\n{self.data_transformation_model_building_config.scaler_model_path}")
            return X_train_scaled,X_test_scaled
        except Exception as e:
            logging.info("Exception occured while scaling the exception")
            raise CustomException(e,sys)
        
    def data_ingestion(self,data_path):
        try:
            data = pd.read_csv(data_path)
            data = self.data_encoder(data)
            target = "Class"
            X = data.drop(columns = [target])
            logging.info(f"Dependent variables:\n{X.head()}")
            logging.info(f"Dimension of whole input data:\n{X.shape}")
            y = data[target]
            logging.info(f"Independent variables:\n{y.head()}")
            logging.info(f"Dimension of whole output data:\n{y.shape}")
            X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.20,random_state=42)
            X_train_scaled,X_test_scaled = self.data_scaling(X_train,X_test)
            return X_train_scaled,X_test_scaled,y_train,y_test
        except Exception as e:
             logging.info("Exception occured while data ingestion process")
             raise CustomException(e,sys)
        
    def transform_data_and_get_models(self,data_path):
        try:
            logging.info("Data transformation and model traning")
            X_train_scaled,X_test_scaled,y_train,y_test = self.data_ingestion(data_path)
            model = RandomForestClassifier()
            model.fit(X_train_scaled,y_train)
            y_pred = model.predict(X_test_scaled)
            save_object(
                file_path = self.data_transformation_model_building_config.predictor_model_path,
                obj = model
            )
            logging.info("----------------------------Getting Metrics-------------------------------")
            accuracy = accuracy_score(y_test,y_pred)
            logging.info(f"The model has accuracy of {accuracy}")
            precision = precision_score(y_test,y_pred,average=None)
            logging.info(f"The model has precission of {precision}")
            recall = recall_score(y_test,y_pred,average=None)
            logging.info(f"The model has recall of {recall}")
            cf = confusion_matrix(y_test,y_pred)
            logging.info(f"The confusion matrix for model\n{cf}")
            logging.info(f"The predicor model has been saved to:\n{self.data_transformation_model_building_config.predictor_model_path}")
        except Exception as e:
            logging.info("Exception occured during model training")