import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

def model_1():
         '''
          data = pd.read_csv("finaldata.csv")


          # Feature Scaling 
          X_train = data.iloc[:,2:8] 
          for i in range(len(X_train.columns)):
             X_train.iloc[:,i]= X_train.iloc[:,i]/(np.max(X_train.iloc[:,i])-np.min(X_train.iloc[:,i])) - (np.mean(X_train.iloc[:,i])/(np.max(X_train.iloc[:,i])-np.min(X_train.iloc[:,i]))) 
          X_train = X_train.fillna(0)

          Y_train = data.iloc[:,-1]

          from sklearn.linear_model import LinearRegression

          model = LinearRegression()


          lr=model.fit(X_train,Y_train)

          predict = lr.predict(X_train)
          pred = abs(predict)
          predict1 = np.zeros(132)

          for i in range(len(pred)):
             predict1[i] = pred[i]/(1+pred[i])

          cities = data.iloc[:,0]'''
          return "hi"
          

          