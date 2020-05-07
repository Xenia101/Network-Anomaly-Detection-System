import numpy as np
import pandas as pd
import Preprocessing
import matplotlib.pyplot as plt
from sklearn.neighbors import LocalOutlierFactor

def percentage(p, w):
    return int(p*w/100)

path = "./CIC-output/packet-0507.pcap_Flow.csv"

X = Preprocessing.load_df(path)

clf = LocalOutlierFactor(n_neighbors=3, contamination=0.1)
y_pred = clf.fit_predict(X.values)
X_scores = clf.negative_outlier_factor_
X_scores = np.array(X_scores, dtype=np.float64)

X['scores'] = -X_scores

## to CSV
#X.to_csv('output.csv', index=False)

number1_percent = percentage(1, len(X_scores))
print(X.sort_values(by='scores', ascending=False).head(number1_percent)['scores'])

