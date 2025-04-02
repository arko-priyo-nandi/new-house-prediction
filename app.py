from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

# Load model and columns
model = pickle.load(open('bangalore_home_prices_model.pkl', 'rb'))
data_columns = pickle.load(open('columns.pkl', 'rb'))  # Ensure this has 243 features

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse input data
        data = request.get_json()
        sqft = float(data['sqft'])
        bath = int(data['bath'])
        bhk = int(data['bhk'])
        location = data['location']

        # Prepare input vector
        x = np.zeros(len(data_columns))  # Ensure this matches 243 features
        x[0] = sqft
        x[1] = bath
        x[2] = bhk

        # Handle one-hot encoding for location
        if location in data_columns:
            loc_index = data_columns.index(location)
            x[loc_index] = 1
        else:
            return jsonify({'error': f"Location '{location}' not found in training data"}), 400

        # Predict price
        prediction = model.predict([x])[0]
        return jsonify({'estimated_price': round(prediction, 2)})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get_locations', methods=['GET'])
def get_locations():
    locations = data_columns[3:]  # Skip numerical features (first three columns)
    return jsonify({'locations': sorted(locations)})

if __name__ == '__main__':
    app.run(debug=True)
