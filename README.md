**STEP-BY-STEP GUIDE FOR SETTING UP AND VERIFYING THE FUNCTIONING OF THE PROJECT**

**PROJECT TITLE:** Student Performance Prediction

**STREAMLIT LINK (TO SEE THE ML WEB APP DEPLOYED):**
 https://mlproject-davidetestiscorepredict.streamlit.app/

**AWS LINK (TO SEE THE ML WEB APP DEPLOYED WITH AWS ECR, EC2, WITH CI/CD WORKFLOWS):**
(please consider the AWS could be down due to servicing costs)
 http://16.170.215.133:8080/predictdata

**CANVA LINK (TO SEE A PICTURE PRESENTATION OF THE ML WEB APP DEPLOYED WITH AWS ECR, EC2, WITH CI/CD WORKFLOWS):**
 https://www.canva.com/design/DAGHMrbyF6g/q4YL8JIChFYvcdET8LXdZw/edit?utm_content=DAGHMrbyF6g&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

----------------------------------------------

**Project Overview**
This project showcases my abilities in developing and deploying a Machine Learning application using various technologies and best practices in a collaborative environment. Below is a summary of the project's scope and the technologies used:

**Scope:** This project aims to predict a student's math score based on various input parameters such as gender, race/ethnicity, parental level of education, lunch type, test preparation course, reading score, and writing score. The model has been trained on a dataset of student performance and utilizes various machine learning algorithms to make predictions.

**Candidate's abilities showcased in this project**
    Collaborative Development with GitHub:
        - Demonstrated the use of GitHub for collaborating with team members, ensuring synchronization and efficient version control.

    Isolated Development Environment:
        - Set up a separate environment for developing the project to maintain isolation and manage dependencies effectively.

    Organized Folder Structure:
        - Implemented a proper folder structure for developing and deploying a Machine Learning application, ensuring clarity and ease of navigation.
    
    Exploratory Data Analysis and Model Training:
        - Utilized Jupyter Notebooks to perform Exploratory Statistical Analysis and Model Training, showcasing data visualization and model evaluation techniques.
    
    Data Handling and Model Training Pipeline:
        - Developed pipelines for data ingestion, data transformation, and model training, including hyperparameter tuning for optimizing model performance.
    
    Web Application Development:
        - Created a web application with a basic HTML script to serve as the prediction endpoint, providing an interface for user interaction.
    
    Streamlit Deployment:
        - Demonstrated how to host the web application on Streamlit, making the app accessible through a web browser.
    
    Containerization with Docker:
        - Used Docker to containerize the application locally, ensuring consistency across different environments.
    
    CI/CD with Docker, AWS ECR, and AWS EC2:
        - Implemented Continuous Integration and Continuous Deployment (CI/CD) using Docker, AWS Elastic Container Registry (ECR), and AWS Elastic Compute Cloud (EC2) via GitHub Actions.
        - Managed user permissions with AWS Identity and Access Management (IAM) specifically for ECR and EC2.

**Technologies Used**
    - GitHub: For version control and collaboration.

    - Jupyter Notebooks: For Exploratory Data Analysis and Model Training.
    
    - Python: For the files, models and app functioning
    
    - HTML: For creating the web application's prediction endpoint.
    
    - Streamlit: For hosting the web application.
    
    - Docker: For containerizing the application.
    
    - AWS ECR: For storing Docker images.
    
    - AWS EC2: For deploying and running the web application.
    
    - AWS IAM: For managing user permissions related to ECR and EC2.
    
    - GitHub Actions: For setting up CI/CD pipelines.

----------------------------------------------

**CLONING AND SETUP STEPS**

    Open a cmd terminal and clone the Repository into C:\Users\User:

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

----------------------------------------------

**DEPLOYMENT METHODS**

METHOD 1 FOR RUNNING THE APPLICATION LOCALLY

    Run the Application:

        python app.py

    Test the endpoints:

        http://127.0.0.1:5000/
        http://127.0.0.1:5000/predictdata

METHOD 2 FOR RUNNING THE APPLICATION NOT LOCALLY VIA STREAMLIT

    Run the Application: 

        streamlit run app_streamlit.py

    Test the web app on streamlit:
        
        https://mlproject-davidetestiscorepredict.streamlit.app/

METHOD 3 FOR RUNNING THE APPLICATION LOCALLY WITH DOCKER (WITHOUT STREAMLIT)

    Build the Docker Image (be sure to have docker engine on with Docker Desktop):

        docker build -t student-performance-prediction .

    Run the Docker Container:

        docker run -p 5000:5000 student-performance-prediction

    Test the endpoints: 

        http://localhost:5000/
        http://localhost:5000/predictdata


METHOD 4 FOR RUNNING THE APPLICATION WITH DOCKER (WITH AWS ECR, EC2, CI/CD WORKFLOWS)

    Here the documents steps in a picture slideshow on canva:
    
        https://www.canva.com/design/DAGHMrbyF6g/q4YL8JIChFYvcdET8LXdZw/edit?utm_content=DAGHMrbyF6g&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton


----------------------------------------------

**FOLDER STRCUTRE DETAILED**

    mlproject/
    |-- .gitignore                       # Specifies files and directories to be ignored by Git.
    |-- app_streamlit.py                 # Streamlit application script for predicting student performance.
    |-- app.py                           # Flask application script for predicting student performance.
    |-- Dockerfile                       # Dockerfile for creating a Docker image for the application.
    |-- list_directory_structure.py      # Script to list the directory structure of the project.
    |-- project_setup.py                 # Script to set up the project environment and generate initial artifacts.
    |-- README.md                        # Project documentation file.
    |-- requirements.txt                 # List of Python dependencies required for the project.
    |-- setup.py                         # Script for packaging and installing the project.
    |-- .git/                            # Directory containing Git metadata.
    |   |-- ...                          # Various Git configuration and tracking files.
    |-- .github/
    |   |-- workflows/
    |       |-- main.yaml                # GitHub Actions workflow configuration for CI/CD.
    |-- artifacts/                       # Directory to store generated artifacts.
    |   |-- data.csv                     # Raw data file.
    |   |-- model.pkl                    # Serialized machine learning model.
    |   |-- preprocessor.pkl             # Serialized preprocessor for data transformation.
    |   |-- test.csv                     # Test dataset.
    |   |-- train.csv                    # Training dataset.
    |-- catboost_info/                   # Directory containing CatBoost training logs and information.
    |   |-- ...                          # Various CatBoost log files and directories.
    |-- logs/                            # Directory to store log files.
    |   |-- ...                          # Various log files generated during model training and testing.
    |-- mlproject.egg-info/              # Metadata about the package generated by setup.py.
    |   |-- ...                          # Various package information files.
    |-- notebook/                        # Directory containing Jupyter notebooks for data exploration and model training.
    |   |-- 1. EDA STUDENT PERFORMANCE .ipynb  # Notebook for Exploratory Data Analysis (EDA).
    |   |-- 2. MODEL TRAINING.ipynb      # Notebook for model training.
    |   |-- data/
    |       |-- stud.csv                 # Dataset used for training and testing.
    |-- src/                             # Directory containing the main source code for the project.
    |   |-- exception.py                 # Custom exception handling.
    |   |-- logger.py                    # Logging configuration.
    |   |-- utils.py                     # Utility functions.
    |   |-- __init__.py                  # Init file to make this directory a package.
    |   |-- components/                  # Directory containing components for data ingestion, transformation, and model training.
    |       |-- data_ingestion.py        # Script for data ingestion.
    |       |-- data_transformation.py   # Script for data transformation.
    |       |-- model_trainer.py         # Script for model training.
    |       |-- __init__.py              # Init file for components package.
    |   |-- pipeline/                    # Directory containing the pipeline scripts.
    |       |-- predict_pipeline.py      # Script for making predictions using the trained model.
    |       |-- train_pipeline.py        # Script for running the complete training pipeline.
    |       |-- __init__.py              # Init file for pipeline package.
    |-- templates/                       # Directory containing HTML templates for the Flask application.
    |   |-- home.html                    # Template for the prediction input form.
    |   |-- index.html                   # Template for the homepage.

----------------------------------------------

**ETL Pipeline Structure**
1. Extraction: data_ingestion.py
 - Purpose: This script is responsible for extracting data from various sources and loading it into the project for further processing.
 - Key Functions:
 - Reading raw data from source files (like CSV).
 - Splitting data into training and test sets.
Saving the split datasets into specified directories (artifacts/).
2. Transformation: data_transformation.py
 - Purpose: This script handles the transformation of raw data into a format suitable for machine learning model training.
 - Key Functions:
 - Data cleaning (handling missing values, encoding categorical variables, scaling numerical features).
 - Feature engineering (creating new features from existing ones if necessary).
 - Saving the transformation pipeline (preprocessor) as a serialized object (preprocessor.pkl).
3. Loading: model_trainer.py
 - Purpose: This script trains the machine learning model using the transformed data and saves the trained model for later use.
 - Key Functions:
 - Loading transformed training data.
 - Training the machine learning model.
 - Evaluating the model on validation or test data.
 - Saving the trained model as a serialized object (model.pkl).
