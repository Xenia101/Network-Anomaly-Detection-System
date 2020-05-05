import Preprocessing
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
import math
import mglearn

def get_X(path):
    data = Preprocessing.RemoveCol(path, 1)
    X = data.values
    return X

def k_distances(x, k):
    dim0 = x.shape[0]
    dim1 = x.shape[1]
    p=-2*x.dot(x.T)+np.sum(x**2, axis=1).T+ np.repeat(np.sum(x**2, axis=1),dim0,axis=0).reshape(dim0,dim0)
    p = np.sqrt(p)
    p.sort(axis=1)
    p=p[:,:k]
    pm= p.flatten()
    pm= np.sort(pm)
    return p, pm

def graph_eps():
    m, m2= k_distances(X, 2)
    plt.plot(m2)
    plt.ylabel("k-distances")
    plt.grid(True)
    plt.show()

normal = get_X("./CIC-output/smallFlows.pcap_Flow.csv")
anomaly = get_X("./CIC-output/http-flood.pcap_Flow.csv")
X = np.r_['0',normal,anomaly]
X = StandardScaler().fit_transform(X)

dbscan = DBSCAN(eps=0.25, min_samples=20).fit(X)
y = dbscan.labels_

plt.scatter(X[:, 0], y, c=dbscan.fit_predict(X))
plt.show()

#n_clusters_ = len(set(clustering.labels_)) - (1 if -1 in clustering.labels_ else 0)
#print(n_clusters_)
