import numpy as np

def preprocess_input(data, scaler_time, scaler_amount):
    time = scaler_time.transform([[data['time']]])[0][0]
    amount = scaler_amount.transform([[data['amount']]])[0][0]

    v_features = [data[f'V{i}'] for i in range(1, 29)]

    final_input = [time] + v_features + [amount]
    return np.array([final_input])
