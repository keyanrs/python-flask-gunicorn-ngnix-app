from flask import Flask, request
from model import Model

app = Flask(__name__)

model = Model()

@app.route("/")
def hello():
    print(request.data)
    return "<h1 style='color:blue'>To call ML Prediction send post request with JSON inputs</h1>"

@app.route("/", methods=['POST'])
def predict():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        return model.predict(json)
    else:
        return 'Content-Type not supported! Expected application/json Content-Type'

if __name__ == "__main__":
    app.run(host='0.0.0.0')