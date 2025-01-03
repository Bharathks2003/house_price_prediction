from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model and scaler
model = joblib.load('models/linear_regression_model.pkl')
scaler = joblib.load('models/scaler.pkl')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    form_values = list(request.form.values())
    features = [
        float(form_values[0]),  # area
        float(form_values[1]),  # bedrooms
        float(form_values[2]),  # bathrooms
        float(form_values[3]),  # stories
        1 if form_values[4].lower() == 'yes' else 0,  # mainroad
        1 if form_values[5].lower() == 'yes' else 0,  # guestroom
        1 if form_values[6].lower() == 'yes' else 0,  # basement
        1 if form_values[7].lower() == 'yes' else 0,  # hotwaterheating
        1 if form_values[8].lower() == 'yes' else 0,  # airconditioning
        float(form_values[9]),  # parking
        1 if form_values[10].lower() == 'yes' else 0,  # prefarea
        1 if form_values[11].lower() == 'semi-furnished' else 0,  # furnishingstatus_semi-furnished
        1 if form_values[11].lower() == 'unfurnished' else 0  # furnishingstatus_unfurnished
    ]

    features = np.array(features).reshape(1, -1)

    features_scaled = scaler.transform(features)

    prediction = model.predict(features_scaled)

    return render_template('result.html', prediction_text=f'Predicted House Price: ₹{prediction[0]:,.2f}')


if __name__ == "__main__":
    app.run(debug=True)
