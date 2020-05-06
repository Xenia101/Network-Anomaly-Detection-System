import Preprocessing
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
import mglearn

def get_X(path):
    df = Preprocessing.RemoveCol(path, 1)
    if df.isnull().values.any():
        df = df[~df.isin([np.nan, np.inf, -np.inf]).any(1)]
        df = df[df['Flow Byts/s'] != 'Infinity']
        df = df[df['Flow Pkts/s'] != 'Infinity']
    X = df.values
    return X

X = get_X("./CIC-output/packet-1.pcap_Flow.csv")

scaler = StandardScaler()
scaler.fit(X)
X_scaled = scaler.transform(X)

dbscan = DBSCAN()
clusters = dbscan.fit_predict(X_scaled)

from sklearn.decomposition import PCA
pca = PCA(n_components=2)
pc = pca.fit_transform(X_scaled)
plt.scatter(pc[:,0],pc[:,1], c=clusters, cmap=mglearn.cm2, s=10, edgecolors='black')
plt.show()
