import streamlit as st
import pandas as pd
from src.pipeline.predict_pipeline import CustomData, PredictPipeline


# Title of the application
st.title("Student Performance Prediction")

# Sidebar for user input
st.sidebar.header("Input Parameters")

def user_input_features():
    gender = st.sidebar.selectbox('Gender', ('male', 'female'))
    race_ethnicity = st.sidebar.selectbox('Race/Ethnicity', ('group A', 'group B', 'group C', 'group D', 'group E'))
    parental_level_of_education = st.sidebar.selectbox('Parental Level of Education', 
                                                       ('bachelor\'s degree', 'some college', 'master\'s degree', 
                                                        'associate\'s degree', 'high school', 'some high school'))
    lunch = st.sidebar.selectbox('Lunch', ('standard', 'free/reduced'))
    test_preparation_course = st.sidebar.selectbox('Test Preparation Course', ('none', 'completed'))
    reading_score = st.sidebar.slider('Reading Score', 0, 100, 50)
    writing_score = st.sidebar.slider('Writing Score', 0, 100, 50)
    
    data = {
        'gender': gender,
        'race_ethnicity': race_ethnicity,
        'parental_level_of_education': parental_level_of_education,
        'lunch': lunch,
        'test_preparation_course': test_preparation_course,
        'reading_score': reading_score,
        'writing_score': writing_score
    }
    
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

# Main panel to display user input
st.subheader("User Input Parameters")
st.write(input_df)

# Prediction
if st.button("Predict"):
    predict_pipeline = PredictPipeline()
    prediction = predict_pipeline.predict(input_df)
    st.subheader("Prediction")
    st.write(f"Predicted Math Score: {prediction[0]}")

if __name__ == "__main__":
    st.write("Run this Streamlit app using the command: `streamlit run app_streamlit.py`")
