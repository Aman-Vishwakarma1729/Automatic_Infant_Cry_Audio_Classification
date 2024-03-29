from src.components.data_extraction import data_extraction_from_audio
from src.components.data_transformation_model_building import data_transformation_model_building

data_extractor = data_extraction_from_audio()
data_transformer_model_builder = data_transformation_model_building()

data_path = data_extractor.get_dataframe()
data_transformer_model_builder.transform_data_and_get_models(data_path)
print("Done")