from flask import Flask,request, url_for, redirect, render_template
import pickle
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
import numpy as np
app = Flask(__name__)

model = pickle.load(open('model1.pkl', 'rb'))
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [x for x in request.form.values()]
    final_features=[]
    for i in range(len(int_features)):
        if(i>=2):
            final_features.append(int(int_features[i]))
    print(final_features)  
    final_fe = [np.array(final_features)]
    print(final_fe)
    prediction = model.predict(final_fe)

    output = round(prediction[0], 2)
    temp=""
    if output==0:
        temp="You are not a patient of Diabetes"
    else:
        temp=" You are patient of Diabetes"
        

    return render_template('index.html', prediction_text=temp)
if __name__ == "__main__":
    app.run()
