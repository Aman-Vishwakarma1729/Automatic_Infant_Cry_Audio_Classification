# <div align="center">Automatic Infant Cry Audio Classification for Differentiating Infant Cries Indicating Discomfort</div>

<div align="center">
  <img src="README_images_sources/Baby_Crying.jpeg" alt="Designer" width="500"/>
</div>

## Table of content
--------------
1. [Introduction](#introduction)
2. [About Dataset](#about_dataset)
3. [About Important Libraries Used In This Project](#About_important_libraries_used_in_this_project)

## Introduction
--------------
Infant crying is the **physiological** action that infants use to reflect their **physical**, **medical**, or **emotional** state to the outside world. Although infant cries seem to like each other, the physiological formation of crying includes different characteristics. Experienced parents, doctors, or nurses can perceive these differences based on their past experiences. Various features in the signal of infant cry provide information not only about the physical needs of the baby but also about medical issues such as **developmental disorders**, **autism**, and **chromosomal abnormalities**. This project aims to classify the **discomfort** that a infant is suffering from by analyzing the pattern of their crying audio. A small survey was done within friends and family to know weather educated adults can audibly distinguish different types of cries, and it was determined that crying types can be distinguished auditory. But we found that training human perception is a much more difficult and longer process than training machine learning algorithm to classify the discomfort type using infant crying audio.  The machine learning-based process can provide support to **parents**, **caregivers**, and **physicians** as it provides **low-cost**, **non-invasive**, **low-risk**, and **higher success**. 

## About Dataset
----------------
* The data is taken from **Infant Cry Audio Corpus**.
* An infant cry audio corpus that has been built through the **Donate-a-cry** campaign (no longer active).
* Also it include some extra data taken from kaggle.
* - [Data_source_1](https://www.kaggle.com/datasets/sanmithasadhish/infant-cry-dataset)
* - [Data_source_2](https://www.kaggle.com/datasets/warcoder/infant-cry-audio-corpus)
* The database is published under the **ODbL**.
* **File naming convention**
* One can visit the [Naming Convention](https://github.com/gveres/donateacry-corpus) github repository -> README.md to understand naming convention.
* Below is data category and number of audio files that we have for each category.
<div align="center">
  <img src="README_images_sources/Data_Distribution.png" alt="Designer" width="300"/>
</div>

* Below is distribution of audio length for each cartegory.
<div align="center">
  <img src="README_images_sources/Audio_length_distribution.png" alt="Designer" width="300"/>
</div>

* Since the project is **open source** if any one get's **more data for given categories** or any **other category data** they can append that data folder in [Audio_Data](Audio_Data), and can run each cell of the file [Basic_Data_Understanding.ipynb](Audio_Data/Research/Basic_Data_Understanding.ipynb) to get basic understanding of data.

## About Important Libraries Used In This Project
-------------------------------------------------
1. **Librosa**

Librosa is a Python package for music and audio analysis. It provides tools for a variety of tasks related to audio processing, feature extraction, and analysis. Librosa is widely used in the fields of music information retrieval, audio signal processing, and machine learning for audio applications.

Some key features and functionalities of librosa include:

1. **Audio Loading:** Librosa allows you to load audio files in various formats and provides functions to manipulate and extract information from them.

2. **Feature Extraction:** It provides tools for extracting various audio features such as Mel-frequency cepstral coefficients (MFCCs), chroma feature, spectral contrast, and more. These features are commonly used for audio analysis and machine learning applications.

3. **Time-Frequency Representations:** Librosa allows you to create time-frequency representations of audio signals, such as spectrograms and chromagrams, which are useful for visualizing and analyzing the frequency content of audio over time.

4. **Beat and Tempo Analysis:** Librosa includes functions for beat tracking and tempo estimation, which are essential for music analysis.

5. **Pitch Estimation:** It provides tools for estimating pitch and harmonic content in audio signals.

6. **Time-Domain and Frequency-Domain Manipulation:** Librosa allows you to manipulate audio signals in both the time and frequency domains.

7. **Machine Learning Integration:** Librosa is often used in conjunction with machine learning libraries for audio classification, genre recognition, and other audio-related tasks.

Librosa simplifies many of the complex tasks associated with audio analysis, making it easier for researchers, developers, and data scientists to work with audio data in Python. It's a valuable tool for anyone working on projects involving audio processing, music analysis, or machine learning with audio data.



## Requirements:

1. setuptools==68.2.2