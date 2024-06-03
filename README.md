**STEP-BY-STEP GUIDE FOR SETTING UP AND VERIFYING THE FUNCTIONING OF THE PROJECT**

**Project Title:** Student Performance Prediction

**STREAMLIT LINK (TO SEE THE ML WEB APP DEPLOYED):** https://mlproject-davidetestiscorepredict.streamlit.app/

**Scope:** This project aims to predict a student's math score based on various input parameters such as gender, race/ethnicity, parental level of education, lunch type, test preparation course, reading score, and writing score. The model has been trained on a dataset of student performance and utilizes various machine learning algorithms to make predictions.


Clone the Repository:

    git clone https://github.com/your-username/mlproject.git
    cd mlproject/mlproject


Set Up a Virtual Environment (Optional but recommended):

    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the Required Packages:

    pip install -r requirements.txt

Run the Project Setup Script:
This script will install the dependencies and create the necessary artifacts (like the trained model, processed data, etc.).

    python project_setup.py


METHOD 1 FOR RUNNING THE APPLICATION LOCALLY
Running the Application (if applicable):
If your project includes a web application or some other entry point, they can run it as follows:

    python app.py

Tests the endpoints 

    http://127.0.0.1:5000/
    http://127.0.0.1:5000/predictdata

METHOD 2 FOR RUNNING THE APPLICATION NOT LOCALLY VIA STREAMLIT
Run the Application: Start the Streamlit application by executing the following command in your terminal:

    streamlit run app_streamlit.py

This command will start a local server, and Streamlit will provide a URL (usually http://localhost:8501) or (https://mlproject-davidetestiscorepredict.streamlit.app/) that you can open in your web browser to view and interact with the app.

METHOD 3 FOR RUNNING THE APPLICATION NOT LOCALLY WITH DOCKER (WITHOUT STREAMLIT)

Build the Docker Image (be sure to have docker engine on with Docker Desktop):

    docker build -t student-performance-prediction .

Run the Docker Container:

    docker run -p 5000:5000 student-performance-prediction

Tests the endpoints 

    http://localhost:5000/
    http://localhost:5000/predictdata



