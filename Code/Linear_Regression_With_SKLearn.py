import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import warnings as warn

class Linear_Regression_sk:

    def __init__(self):
        self.df : pd.DataFrame
        self.x : pd.DataFrame
        self.y : pd.DataFrame
        self.y_pred : np.ndarray 
        warn.filterwarnings("ignore")
    
    def load(self):
        self.df : pd.DataFrame = pd.read_csv("Salary_dataset.csv")
        self.x : pd.DataFrame = self.df[["YearsExperience"]]
        self.y : pd.DataFrame = self.df["Salary"]
    
    def predict(self,x : np.ndarray):
        model = LinearRegression()
        model.fit(self.x,self.y)
        return model.predict(x)
    
lr = Linear_Regression_sk()
lr.load()
print("The predicted Salary is : ",round(lr.predict([[8.0]])[0]))
