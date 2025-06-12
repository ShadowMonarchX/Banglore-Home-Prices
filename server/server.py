from flask import Flask, request, jsonify, send_from_directory
import util
import os

app = Flask(__name__, static_folder='../client', static_url_path='')

@app.route('/')
def serve_frontend():
    return send_from_directory(app.static_folder, 'app.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

@app.route('/api/get_location_names', methods=['GET'])
def get_location_names():
    try:
        locations = util.get_location_names()
        return jsonify({'locations': locations}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
        data = request.form
        total_sqft = float(data.get('total_sqft'))
        location = data.get('location')
        bhk = int(data.get('bhk'))
        bath = int(data.get('bath'))

        estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)
        return jsonify({'estimated_price': estimated_price}), 200

    except (ValueError, TypeError) as e:
        return jsonify({'error': 'Invalid input format', 'details': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Something went wrong', 'details': str(e)}), 500

if __name__ == "__main__":
    print("Starting Flask Server for Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(host='0.0.0.0', port=5050)
