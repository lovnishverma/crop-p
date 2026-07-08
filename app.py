from flask import Flask, render_template, request
import joblib

app = Flask(__name__)  # Initilize the Flask app

# load model

model = joblib.load('crop_model.joblib')


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/predict", methods=["POST"])
def predict():

    features = [
        float(request.form["N"]),
        float(request.form["P"]),
        float(request.form["K"]),
        float(request.form["ph"]),
        float(request.form["EC"]),
        float(request.form["S"]),
        float(request.form["Cu"]),
        float(request.form["Fe"]),
        float(request.form["Mn"]),
        float(request.form["Zn"]),
        float(request.form["B"])
    ]

    prediction = model.predict([features])[0]

    return render_template("index.html", prediction=prediction)


@app.route('/aboutme')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
