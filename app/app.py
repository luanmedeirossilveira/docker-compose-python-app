from flask import Flask, jsonify # type: ignore

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Bem-vindo a aplicacao Python com Docker Compose!")

@app.route('/api/data')
def get_data():
    return jsonify(data={"id": 1, "name": "Fulano"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
