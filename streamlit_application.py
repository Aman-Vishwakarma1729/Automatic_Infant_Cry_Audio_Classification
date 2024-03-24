import os
import streamlit as st
from src.utils import create_folder
from src.pipeline.prediction_pipeline import prediction_pipeline



def main():
   st.set_page_config(page_title="Infant Cry Analyzer")
   st.header("Infant Cry Analyzer :baby:")
   
   if 'file_buffer' not in st.session_state:
        st.session_state['file_buffer'] = None

   uploaded_file = st.file_uploader("Upload Audio File (Length of audio must be less than 10 seconds)", type=["wav", "mp3"])

   predict_clicked = False
   prediction_result = None

   create_folder("Input_Audio_Files")

   if uploaded_file is not None:
      predict_button = st.button("Predict")
      predict_clicked = predict_button
      st.session_state['file_buffer'] = uploaded_file.read()

      if predict_clicked:
         if uploaded_file is not None:
            with st.spinner("Analyzing audio... Please wait."):
                audio_data_folder_path = os.path.join(os.getcwd(),"Input_Audio_Files")
                audio_file_path = os.path.join(audio_data_folder_path,uploaded_file.name)
                with open(audio_file_path,'wb') as f:
                    f.write(st.session_state.file_buffer)

                prediction_result = prediction_pipeline(audio_file_path)
                prediction_result = prediction_result.upper()

   if prediction_result is not None:
      st.success(prediction_result)
   else:
        if predict_clicked:
            st.info("Processing... This may take a few seconds.")

if __name__ == "__main__":
    main()