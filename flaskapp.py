from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

# Load the best model
with open('best_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.form.to_dict()
        
        # Convert categorical variables
        features = [
            float(data['age']),
            int(data['diabetes']),
            int(data['blood_pressure']),
            int(data['transplants']),
            int(data['chronic_diseases']),
            float(data['height']),
            float(data['weight']),
            int(data['allergies']),
            int(data['cancer_history']),
            int(data['major_surgeries'])
        ]
        
        # Make prediction
        prediction = model.predict([features])
        
        return jsonify({'prediction': prediction[0]})
    
    except Exception as e:
        # Print error for debugging
        print(e)
        
        # Return error response
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
