import Preprocessing
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
import mglearn

X = Preprocessing.load_data("./CIC-output/packet-new.pcap_Flow.csv")

scaler = StandardScaler()
scaler.fit(X)
X_scaled = scaler.transform(X)

dbscan = DBSCAN(eps=0.01, min_samples=3)
clusters = dbscan.fit_predict(X_scaled)

from sklearn.decomposition import PCA
pca = PCA(n_components=3)
pc = pca.fit_transform(X_scaled)
plt.scatter(pc[:,0],pc[:,1], c=clusters, cmap=mglearn.cm2, s=10, edgecolors='black')
plt.show()
