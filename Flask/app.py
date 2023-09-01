from flask import Flask, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
# Sample data for the API
data = [
    {"id": 1, "name": "Manoj"},
    {"id": 2, "name": "Sanjay"},
    {"id": 3, "name": "Magesh"},
]

@app.route('/api/members', methods=['GET'])
def get_items():
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
