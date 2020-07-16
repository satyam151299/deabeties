import numpy as np
import pandas as pd
import pickle
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
df=pd.read_csv("diabetes.csv")
x=df.iloc[:,0:-1]
y=df.iloc[:,-1]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)

knn=KNeighborsClassifier(n_neighbors=2)
knn.fit(x_train,y_train)
pred_train=knn.predict(x_train)
pickle.dump(knn, open('model1.pkl','wb'))
model = pickle.load(open('model1.pkl','rb'))
print(model.predict([[0, 100, 92,35,55,33.2,0.22,18]]))
