# Exnaton Coding challenge

This is the official code repository of the project 'Exnaton_challenge'. This repository contains utilities for:
- EDA of the [real estate data](https://www.kaggle.com/datasets/corrieaar/apartment-rental-offers-in-germany) from Immoscout24
- Preprocessing and loading the dataset
- Training, Evaluation and Testing pipelines

## Data
The [data](https://www.kaggle.com/datasets/corrieaar/apartment-rental-offers-in-germany) was scraped from Immoscout24, the biggest real estate platform in Germany. Immoscout24 has listings for both rental properties and homes for sale, however, the data only contains offers for rental properties.
## Task
Task is divided into two main parts, focusing on machine learning model development for rent prediction:

1.	Predicting Rent with Structural Data: Develop a machine learning model to predict the total rent using only the structural data. Exclude the “description” and “facilities” text fields for this model.

2.	Predicting Rent with Structural and Text Data: Create a second machine learning model that predicts the total rent using both structural and text data (“description” and “facilities”). Using modern generative AI techniques for processing text data is encouraged.
## Overview of Solution
