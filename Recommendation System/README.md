# Recommendation System

## Data Description:

Unique ID of each anime.

Anime title.

Anime broadcast type, such as TV, OVA, etc.

anime genre.

The number of episodes of each anime.

The average rating for each anime compared to the number of users who gave ratings.

Number of community members for each anime.

## Objective:

The objective of this assignment is to implement a recommendation system using cosine similarity on an anime dataset. 

## Dataset:

Use the Anime Dataset which contains information about various anime, including their titles, genres,No.of episodes and user ratings etc.

## Tasks:

### Data Preprocessing:

Load the dataset into a suitable data structure (e.g., pandas DataFrame).

Handle missing values, if any.

Explore the dataset to understand its structure and attributes.

![image](https://github.com/user-attachments/assets/106c347e-609c-49a7-8891-28be16ceddc8)


![image](https://github.com/user-attachments/assets/c011a26b-849b-40a5-b19c-2986b291c887)


### Feature Extraction:

Decide on the features that will be used for computing similarity (e.g., genres, user ratings).

Convert categorical features into numerical representations if necessary.

Normalize numerical features if required.

![image](https://github.com/user-attachments/assets/2927e2a6-4cf4-47c6-8eeb-6da5a1fa0577)

![image](https://github.com/user-attachments/assets/f25fcab4-079e-4450-a41f-77efed4e1322)


### Recommendation System:

Design a function to recommend anime based on cosine similarity.

Given a target anime, recommend a list of similar anime based on cosine similarity scores.

Experiment with different threshold values for similarity scores to adjust the recommendation list size.


### Evaluation:

Split the dataset into training and testing sets.

Evaluate the recommendation system using appropriate metrics such as precision, recall, and F1-score.


Analyze the performance of the recommendation system and identify areas of improvement.
