import Preprocessing
import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

def percentage(p, w):
    return 100 * float(p)/float(w)

X = Preprocessing.load_data("./CIC-output/packet-new.pcap_Flow.csv")

scaler = StandardScaler()
scaler.fit(X)
X_scaled = scaler.transform(X)

db = DBSCAN(eps=3, min_samples=10).fit(X_scaled)
labels = db.labels_
n_data_ = len(list(labels))
n_noise_ = list(labels).count(-1)

print("number of total data : {}".format(n_data_))
print("number of noise data : {}".format(n_noise_))
print("percentage of noise from total data : {:.2f}%".format(percentage(n_noise_,n_data_)))
