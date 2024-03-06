# <div align="center">Automatic Infant Cry Audio Classification for Differentiating Infant Cries Indicating Discomfort</div>

<div align="center">
  <img src="README_images_sources/Baby_Crying.jpeg" alt="Designer" width="500"/>
</div>

## Table of content
--------------
1. [Introduction](#introduction)
2. [About Dataset](#about_dataset)

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

* Since the project is **open source** if any one get's **more data for given categories** or any **other category data** they can append that data folder in [Audio_Data](Audio_Data), and can run each cell of the file [Basic_Data_Understanding.ipynb](Audio_Data/Research/Basic_Data_Understanding.ipynb) to get basic understanding of data.




## Requirements:

1. setuptools==68.2.2