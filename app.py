from flask import Flask, jsonify, render_template, request, make_response
import pickle
import numpy as np

app = Flask(__name__, static_folder='static')

# Load the saved model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define a function to preprocess the user inputs
def preprocess_inputs(inputs):
    # Convert the inputs to numeric values
    numeric_inputs = [float(i) for i in inputs]
    
    # Reshape the inputs to match the expected input shape of the model
    processed_inputs = np.array(numeric_inputs).reshape(1, -1)
    
    return processed_inputs

# Define the home route
@app.route('/')
def home():
    return render_template('index.html')

# Define the predict route
@app.route('/getpredict', methods=['POST'])
def get_predict():
    req = request.get_json()
    
    age = int(req.get('age'))
    glucose = int(req.get('glucose'))
    
    insuline = int(req.get('insuline'))
    
    blood_pressure = int(req.get('blood_pressure'))
    
    skin_thickness = int(req.get('skin_thickness'))
    
    height = float(req.get('height'))  
    
    weight = float(req.get('weight'))   
    
    pregnancies = int(req.get('pregnancies'))
    
    #Calculate BMI
     # Convert height from cm to meters
    bmi= round(weight / (height / 100) ** 2 ,2)

     # Get family history data from the form
    parent_diabetes = int(req.get('parent_diabetes'))
    print("parent_diabetes",parent_diabetes)
    sibling_diabetes = int(req.get('sibling_diabetes'))
    grandparent_diabetes = int(req.get('grandparent_diabetes'))
    
    weights = {
            'parent': 0.2 if parent_diabetes else 0,
            'sibling': 0.15 if sibling_diabetes else 0,
            'grandparent': 0.1 if grandparent_diabetes else 0,
            
        }

       # Calculate DPF score
    dpf_score = round(sum(weights.values()),3)
    
    inputs = preprocess_inputs([glucose, blood_pressure, skin_thickness, insuline, bmi, dpf_score, age, pregnancies])
    
      #Make prediction
    prediction=[]
    prediction = model.predict(inputs)
    print(prediction[0])
    if prediction[0] == 1:
        result = "You are likely to have Diabetics."
    else:
        result ="You are unlikely to have Diabetics."
        
    res = make_response(jsonify({"message": result}), 200)
    return res
    
if __name__ == '__main__':
    app.run(debug=True) 
