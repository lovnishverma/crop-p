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

    N = float(request.form["N"])
    P = float(request.form["P"])
    K = float(request.form["K"])
    ph = float(request.form["ph"])
    EC = float(request.form["EC"])
    S = float(request.form["S"])
    Cu = float(request.form["Cu"])
    Fe = float(request.form["Fe"])
    Mn = float(request.form["Mn"])
    Zn = float(request.form["Zn"])
    B = float(request.form["B"])

    prediction = model.predict([
        [N, P, K, ph, EC, S, Cu, Fe, Mn, Zn, B]
    ])

    return render_template("index.html", prediction=prediction[0])


@app.route('/aboutme')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
