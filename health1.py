# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 11:43:11 2020

@author: kavin
"""



import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('test.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('insurance.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    '''
    For rendering results on HTML GUI
    '''
    x_test = [[float(x) for x in request.form.values()]]
    
    prediction = model.predict(x_test)
    print(prediction)
    output=prediction[0][0]
    return render_template('insurance.html', prediction_text='Health Insurance Charges in USD {}'.format(output))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.y_predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)