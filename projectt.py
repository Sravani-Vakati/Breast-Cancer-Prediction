from flask import Flask,render_template,request
import numpy as np
import pickle

with open("ndata.pkl",'rb') as f:
    model = pickle.load(f)
#create an object instance
app = Flask(__name__)
@app.route('/sravani')
def check():
    return "Codegnan is in NBKR"
@app.route('/') #by default methods = ['GET']
def new():
    return render_template("index.html")
@app.route('/predict',methods=['POST'])
def predict():
    radius_mean = float(request.form['radius_mean'])
    area_mean = float(request.form['area_mean'])
    perimeter_mean = float(request.form['perimeter_mean'])
    symmetry_mean = float(request.form['symmetry_mean'])
    compactness_mean = float(request.form['compactness_mean'])
    concave_points_mean = float(request.form['concave_points_mean'])
    input_data = np.array([[radius_mean,  perimeter_mean, area_mean, symmetry_mean, compactness_mean,concave_points_mean]])
    predicted_price = model.predict(input_data)[0]
    
    if predicted_price == 1:
        prediction = 'Cancer is Malignant'
    else:
        prediction = 'Cancer is Benign'
    
    return render_template('index.html', prediction = prediction)
app.run()