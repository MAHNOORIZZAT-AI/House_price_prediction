import numpy as np 
import pickle
from flask import Flask, render_template, request, jsonify
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

app = Flask(__name__)
model = pickle.load(open('model.pickle', 'rb'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    val1 = request.form['bedrooms']
    val2 = request.form['bathrooms']
    val3 = request.form['floors']
    val4 = request.form['yr_built']
    arr = np.array([val1, val2, val3, val4])
    arr = arr.astype(np.float64)
    pred = model.predict([arr])

    return render_template('index.html', data=int(pred))


if __name__ == '__main__':
    app.run(debug=True)

