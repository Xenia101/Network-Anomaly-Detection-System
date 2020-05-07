import numpy as np
import pandas as pd
import Preprocessing
import matplotlib.pyplot as plt
from sklearn.neighbors import LocalOutlierFactor

def percentage(p, w):
    return int(p*w/100)

def to_CSV(X):
    X.to_csv('output.csv', index=False)

def train():
    path = "./CIC-output/packet-0507.pcap_Flow.csv"
    X = Preprocessing.load_df(path)

    clf = LocalOutlierFactor(n_neighbors=3, contamination=0.1)
    y_pred = clf.fit_predict(X.values)
    X_scores = clf.negative_outlier_factor_
    X_scores = np.array(X_scores, dtype=np.float64)

    X['scores'] = -X_scores
    
    number1_percent = percentage(10, len(X_scores))
    return X, X.sort_values(by='scores', ascending=False).head(number1_percent)['scores']

def test(X, cutline):
    X.drop("scores", axis='columns', inplace=True)
    anomaly_path = "./CIC-output/http-flood.pcap_Flow.csv"
    anomaly_data = Preprocessing.load_df(anomaly_path)

    for xi in range(len(anomaly_data)):
        
        nth_data = list()
        for x in list(anomaly_data.columns):
            nth_data.append(anomaly_data.loc[xi,x])
        X.loc[len(X)] = nth_data 

        clf = LocalOutlierFactor(n_neighbors=3, contamination=0.1)
        y_pred = clf.fit_predict(X.values)
        X_scores = clf.negative_outlier_factor_
        X_scores = np.array(X_scores, dtype=np.float64)

        print(-X_scores[-1])
        if -X_scores[-1] >= cutline:
            print('OUTtlier')
        else:
            print('INlier')
        print('=====')
        X = X.drop(X.index[len(X)-1])
        
    return ''

def cutline_score(scores):
    return scores.min(axis=0)

X, train_score_1per = train()
test(X, cutline_score(train_score_1per))

# to_CSV(X)