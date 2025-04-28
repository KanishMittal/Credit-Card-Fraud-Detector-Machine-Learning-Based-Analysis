from flask import Flask, render_template, request, jsonify
import numpy as np
import joblib
from tensorflow.keras.models import load_model
from fraud_detector import preprocess_input

app = Flask(__name__)

# Load model and scalers
model = load_model('models/oversample_model.h5')
scaler_amount = joblib.load('models/standard_scaler_amount.pkl')
scaler_time = joblib.load('models/standard_scaler_time.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Extract and preprocess
    features = preprocess_input(data, scaler_time, scaler_amount)

    # Make prediction
    prob = model.predict(features)[0][0]
    prediction = "Fraud" if prob > 0.5 else "Not Fraud"

    return jsonify({'prediction': prediction, 'probability': float(prob)})

if __name__ == '__main__':
    app.run(debug=True)
