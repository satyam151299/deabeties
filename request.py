import requests

url = 'http://localhost:5000/predict'
r = requests.post(url,json={'Pregnancies':0, 'Glucose':90, 'BloodPressure':126,'SkinThickness':122,'Insulin':100,'BMI':90,'DiabetesPedigreeFunction':2,'age':40})

print(r.json())
