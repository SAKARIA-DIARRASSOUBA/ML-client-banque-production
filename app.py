import sklearn
import pandas as pd
import numpy as np
import joblib
from flask import Flask, request, render_template
from Home_fonctions import Proportion_donnees,Over_sampling,convert_int,Augmenter_Data
from maisons import Build_predict

model=joblib.load("Banque.model")

app=Flask('__name__')

@app.route('/')
def home():
	
    return render_template('index2.html')


decision=["Reste", "Part"]

@app.route('/predict',methods=['POST'])
def predict():
	int_feature=[x for x in request.form.values()]
	finale_features=Build_predict(int_feature)
	prediction=model.predict(finale_features)
	status=decision[list(prediction)[0]]

	return render_template('index2.html',prediction_text='Prediction= {} donc le client "{}" de la banque'.format(list(prediction)[0],status))
	


@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict(Build_predict(list(data.values())))

    status=decision[list(prediction)[0]]
    return jsonify(status)



if __name__=="__main__":
  app.run(debug=True)