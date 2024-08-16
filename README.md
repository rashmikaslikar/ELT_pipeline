# Overview of the Exnaton Coding challenge

This is the official code repository of the project 'Exnaton_challenge'. This repository contains utilities for:
- Exploratory Data Analysis of the energy data retrieved from the following API
  - [95ce3367-cbce-4a4d-bbe3-da082831d7bd.json](https://exnaton-public-s3-bucket20230329123331528000000001.s3.eu-central-1.amazonaws.com/challenge/95ce3367-cbce-4a4d-bbe3-da082831d7bd.json)
  - [1db7649e-9342-4e04-97c7-f0ebb88ed1f8.json](https://exnaton-public-s3-bucket20230329123331528000000001.s3.eu-central-1.amazonaws.com/challenge/1db7649e-9342-4e04-97c7-f0ebb88ed1f8.json)

- Implementing an ELT pipeline to extract data from the source (API) and load it into the appropriate destination (database).
  At a high level, we're going to:
  - Extract and Load data from source to destination.
  - Transform data for downstream applications.

## Details of the challenge
Task is divided into 2 parts

### Task A - Data Exploration  
- Explore the data and group it by different time intervals. Explain what you see/what the data represents. Come up with a hypothesis on what kind of data you are looking at.
- Bonus: Check for any autocorrelation within the time-series data.
- Please refer to Task_A.md for the solution 

### Task B - Backend  
- Please retrieve the data from the GET endpoint and store it in a database of your choice.
- Write an endpoint to access the data from a frontend application. Which kind of query parameters might be useful to access the data from the frontend? Document your API for your fellow frontend developer.
- Bonus: Provide environment files and/or Deployment files (dockerfile, docker-compose, k8s resource definitions) to deploy the backend.
- - Please refer to Task_B.md for the solution 

