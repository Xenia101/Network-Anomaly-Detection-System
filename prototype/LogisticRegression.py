import numpy as np
import pandas as pd
import Preprocessing
from sklearn.neighbors import LocalOutlierFactor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

path = "./CIC-output/1.csv"
X = Preprocessing.load_df(path)
y = np.array([0 for x in range(len(X[0:910]))] + [1 for x in range(len(X[910:1806]))] + [2 for x in range(len(X[1806:]))])

X = X.to_numpy()

scaler = StandardScaler().fit(X)
X = scaler.transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression().fit(X_train, y_train)
print(logreg.score(X_test, y_test))
