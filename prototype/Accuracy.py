import numpy as np
import pandas as pd
import Preprocessing
import matplotlib.pyplot as plt
from sklearn.neighbors import LocalOutlierFactor
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

def NormalAccuracy(X, y):
    clf = LocalOutlierFactor(n_neighbors=2)
    clf.fit_predict(X)
    y_pred = clf.fit_predict(X)
    accuracy = accuracy_score(y, y_pred)
    print(accuracy)

path = "./CIC-output/1.csv"
X = Preprocessing.load_df(path)
y = np.array([0 for x in range(len(X[0:910]))] + [1 for x in range(len(X[910:1806]))] + [2 for x in range(len(X[1806:]))])
