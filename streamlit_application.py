import os
import streamlit as st
from src.utils import create_folder
from src.pipeline.prediction_pipeline import prediction_pipeline
import librosa
import librosa.display
import matplotlib.pyplot as plt


def main():
   st.set_page_config(page_title="Infant Cry Analyzer")
   st.sidebar.header("Infant Cry Analyzer:baby:")
   selection = st.sidebar.selectbox("Select a page", ("Home", "About"))
   
   if selection == "Home":
       
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

                        prediction_result,confidence = prediction_pipeline(audio_file_path)
                        prediction_result = prediction_result.upper()

        if prediction_result is not None:
            plt.figure(figsize=(14,5))
            data,sample_rate = librosa.load(audio_file_path)
            fig, ax = plt.subplots(figsize=(14, 5))
            ax.plot(data, color='green')
            ax.set_title("Audio Waveform")
            ax.set_xlabel("Time (seconds)")
            ax.set_ylabel("Amplitude")
            ax.axis('off')
            st.pyplot(fig)

            st.success(f"{prediction_result} - {confidence*100}% confident")
        else:
                if predict_clicked:
                    st.info("Processing... This may take a few seconds.")

   elif selection == "About":
        st.title("About Infant Cry Analyzer")
        st.write("""
        This application is designed to analyze infant cries and predict discomfort types.
                 
        You can get detailed information about the project from README.md file of github.
        GitHub: https://github.com/Aman-Vishwakarma1729/Automatic_Infant_Cry_Audio_Classification?tab=readme-ov-file

        **Features:**
        - Upload audio files (wav or mp3)
          -- Note: Audio lenght should be between 6 to 10 seconds for better results.
        - Visualize audio waveform
        - Predict discomfort type with confidence probability
        - The model used in this project is trained on data that contains discomfort categories:
        - ASPHYXIA
        - DEAF
        - HUNGER
        - NORMAL
        - NOT CRY
        - PAIN
        - OTHERS (Tired,Discomfort,Burping)
        - **Disclaimer:**
          This application is for informational purposes only and should not be used as a substitute for professional medical advice.
        """)
if __name__ == "__main__":
    main()