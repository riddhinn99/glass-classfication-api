from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)
PORT = 56565


@app.route("/")
def base():
    return "Base Page"


@app.route("/predict", methods=["GET"])
def predict():
    df = pd.DataFrame(request.json)
    print(df)
    predictions = model.predict(df)
    print()
    return jsonify({"predictions": [int(pred) for pred in predictions]})


if __name__ == "__main__":
    model = joblib.load("finalized_model.sav")
    app.run(port=PORT, debug=True)
