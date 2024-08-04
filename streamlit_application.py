import os
import streamlit as st
from src.utils import create_folder
from src.pipeline.prediction_pipeline import prediction_pipeline
import librosa
import librosa.display
import matplotlib.pyplot as plt

# Main function to run the app
def main():
    # Set page configuration
    st.set_page_config(page_title="Infant Cry Analyzer", page_icon=":baby:", layout="wide")

    # Sidebar configuration
    st.sidebar.header("Infant Cry Analyzer :baby:")
    selection = st.sidebar.selectbox("Select a page", ("Home", "About"))

    # Home page
    if selection == "Home":
        st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Infant Cry Analyzer </h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Upload an audio file to analyze and predict the type of infant discomfort.</p>", unsafe_allow_html=True)

        # File upload
        if 'file_buffer' not in st.session_state:
            st.session_state['file_buffer'] = None
        uploaded_file = st.file_uploader("Upload Audio File (Length of audio must be less than 10 seconds)", type=["wav", "mp3"])

        predict_clicked = False
        prediction_result = None

        # Create folder for input audio files
        create_folder("Input_Audio_Files")

        if uploaded_file is not None:
            predict_button = st.button("Predict")
            predict_clicked = predict_button
            st.session_state['file_buffer'] = uploaded_file.read()

            if predict_clicked:
                if uploaded_file is not None:
                    with st.spinner("Analyzing audio... Please wait."):
                        audio_data_folder_path = os.path.join(os.getcwd(), "Input_Audio_Files")
                        audio_file_path = os.path.join(audio_data_folder_path, uploaded_file.name)
                        with open(audio_file_path, 'wb') as f:
                            f.write(st.session_state.file_buffer)

                        prediction_result, confidence = prediction_pipeline(audio_file_path)
                        prediction_result = prediction_result.upper()

        # Display prediction result and audio waveform
        if prediction_result is not None:
            st.markdown("<h3 style='text-align: center;'>Prediction Result</h3>", unsafe_allow_html=True)
            plt.figure(figsize=(14, 5))
            data, sample_rate = librosa.load(audio_file_path)
            fig, ax = plt.subplots(figsize=(14, 5))
            ax.plot(data, color='green')
            ax.set_title("Audio Waveform")
            ax.set_xlabel("Time (seconds)")
            ax.set_ylabel("Amplitude")
            ax.axis('off')
            st.pyplot(fig)

            st.success(f"{prediction_result} - {confidence*100:.2f}% confident")
        else:
            if predict_clicked:
                st.info("Processing... This may take a few seconds.")
                
        st.markdown("""
        <div style='text-align: center; margin-top: 20px;'>
            For more details, visit the project's GitHub page:
            <br>
            <a href='https://github.com/Aman-Vishwakarma1729/Automatic_Infant_Cry_Audio_Classification' target='_blank'>Automatic Infant Cry Audio Classification</a>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<p style='text-align: center; margin-top: 20px;'>&copy; 2024 Aman Vishwakarma</p>", unsafe_allow_html=True)

    # About page
    elif selection == "About":
        st.title("About Infant Cry Analyzer")
        st.markdown("""
        <style>
            .about-text {
                text-align: justify;
                line-height: 1.6;
                margin-top: 20px;
            }
            .feature-section {
                margin-top: 20px;
            }
            .feature-title {
                font-size: 20px;
                font-weight: bold;
                color: #4CAF50;
            }
            .disclaimer {
                margin-top: 20px;
                color: red;
            }
        </style>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="about-text">
        This application is designed to analyze infant cries and predict discomfort types.
        <br><br>
        You can get detailed information about the project from the README.md file on GitHub.
        <br><br>
        </div>
        """, unsafe_allow_html=True)

        # Features section with collapsible content
        with st.expander("Features"):
            st.markdown("""
            <div class="feature-section">
            <div class="feature-title">Upload audio files (wav or mp3)</div>
            <ul>
                <li>Note: Audio length should be between 6 to 10 seconds for better results.</li>
            </ul>
            </div>
            <div class="feature-section">
            <div class="feature-title">Visualize audio waveform</div>
            </div>
            <div class="feature-section">
            <div class="feature-title">Predict discomfort type with confidence probability</div>
            </div>
            """, unsafe_allow_html=True)

        # Discomfort categories section with collapsible content
        with st.expander("Discomfort Categories"):
            st.markdown("""
            <div class="feature-section">
            The model used in this project is trained on data that contains the following discomfort categories:
            <ul>
                <li>ASPHYXIA</li>
                <li>DEAF</li>
                <li>HUNGER</li>
                <li>NORMAL</li>
                <li>NOT CRY</li>
                <li>PAIN</li>
                <li>OTHERS (Tired, Discomfort, Burping)</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)

        # Disclaimer section
        st.markdown("""
        <div class="disclaimer">
        **Disclaimer:**
        <br>This application is for informational purposes only and should not be used as a substitute for professional medical advice.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style='text-align: center; margin-top: 20px;'>
            For more details, visit the project's GitHub page:
            <br>
            <a href='https://github.com/Aman-Vishwakarma1729/Automatic_Infant_Cry_Audio_Classification' target='_blank'>Automatic Infant Cry Audio Classification</a>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<p style='text-align: center; margin-top: 20px;'>&copy; 2024 Aman Vishwakarma</p>", unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    main()
