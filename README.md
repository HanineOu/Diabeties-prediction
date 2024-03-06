# Diabetes Prediction Web Application

## Description
This Flask application is designed to predict the likelihood of an individual having diabetes based on their input data. The frontend of the application is built using HTML and CSS to create a form, while JavaScript is utilized to capture form data and send it to the Flask backend. The backend utilizes an XGBoost model trained on relevant data to make predictions.

## Instructions
1. Clone this repository to your local machine.
2. Install the required dependencies by running:

   pip install -r requirements.txt
   
3. Run the Flask application by executing:
  
   python app.py

4. Access the application by navigating to `http://localhost:5000` in your web browser.

## Usage
1. Fill out the form with relevant information.
2. Click the submit button to send the data to the Flask backend.
3. The backend will utilize the trained XGBoost model to predict the likelihood of diabetes.
4. The prediction result will be displayed on the webpage.

## Model Training
- The model used in this application was trained using XGBoost.
- For detailed information about the model training process, including data visualization and experimentation with different algorithms, refer to the [Google Colab notebook](https://colab.research.google.com/drive/1kZmq4F7RLejLT2SkdLTENg_EDUXzCy--?usp=sharing)https://colab.research.google.com/drive/1kZmq4F7RLejLT2SkdLTENg_EDUXzCy--?usp=sharing) sharing provided in this repository.
