from src.components.data_extraction import data_extraction_from_audio

data_extractor = data_extraction_from_audio()
data_path = data_extractor.get_dataframe()
print(data_path)