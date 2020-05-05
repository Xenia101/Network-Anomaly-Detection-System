import Preprocessing
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def get_X(path):
    data = Preprocessing.RemoveCol(path, 1)
    X = data.values
    return X

normal = get_X("./CIC-output/smallFlows.pcap_Flow.csv")
anomaly = get_X("./CIC-output/http-flood.pcap_Flow.csv")
X = np.r_['0',normal,anomaly]

inertias = list()
for x in range(1,10):
    kmeans = KMeans(n_clusters=x, random_state=0).fit(X)
    inertias.append(kmeans.inertia_)

plt.plot(range(1,10), inertias, '-o')
plt.xlabel('number of clusters, k')
plt.ylabel('inertia')
plt.xticks(range(1,10))
plt.show()
