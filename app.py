from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample in-memory data store
data_store = []

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(data_store), 200

@app.route('/api/data', methods=['POST'])
def post_data():
    new_data = request.get_json()
    if not new_data:
        return jsonify({"error": "Invalid JSON"}), 400
    data_store.append(new_data)
    return jsonify({"message": "Data added", "data": new_data}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
