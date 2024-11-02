#!/usr/bin/env python
# coding: utf-8

# In[6]:


import warnings
warnings.filterwarnings("ignore")
import streamlit as st
import pandas as pd
import pickle

# Load the saved logistic regression model
with open('titanic_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Streamlit app title and description
st.title("Titanic Survival Prediction")
st.write("""
Predict whether a passenger survived or not based on their details.
""")

# Input fields
pclass = st.selectbox('Passenger Class (Pclass)', [1, 2, 3], index=2)
sex = st.selectbox('Sex', ['male', 'female'], index=0)
age = st.slider('Age', 1, 100, value=25)
sibsp = st.slider('Number of Siblings/Spouses Aboard (SibSp)', 0, 8, value=0)
parch = st.slider('Number of Parents/Children Aboard (Parch)', 0, 6, value=0)
fare = st.number_input('Fare', value=50.0)
embarked = st.selectbox('Embarked Port', ['C', 'Q', 'S'], index=0)

# Convert inputs to model-ready format
sex = 1 if sex == 'male' else 0

# Initialize Embarked dummy variables
embarked_Q = 0  # Default to 0 for 'C'
embarked_S = 0  # Default to 0 for 'C'

# Update Embarked dummy variables based on user input
if embarked == 'Q':
    embarked_Q = 1
    embarked_S = 0
elif embarked == 'S':
    embarked_Q = 0
    embarked_S = 1

# Create the input DataFrame for the model
# Ensure the order of the columns matches the training dataset
inputs = pd.DataFrame({
    'Pclass': [pclass],
    'Age': [age],
    'SibSp': [sibsp],
    'Parch': [parch],
    'Fare': [fare],
    'Sex_male': [sex],
    'Embarked_Q': [embarked_Q],
    'Embarked_S': [embarked_S]
})

# Debugging: Print the input DataFrame columns
st.write("Input DataFrame Columns:", inputs.columns.tolist())

# Predict and display the result
if st.button('Predict'):
    try:
        prediction = model.predict(inputs)[0]
        st.write(f"The passenger {'survived' if prediction == 1 else 'did not survive'}.")
    except ValueError as e:
        st.error(f"Error in prediction: {e}")


# In[ ]:




