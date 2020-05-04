from FlowRecoder import get_data, gen_json
import pandas as pd
import numpy as np
import json
from sklearn.feature_extraction import DictVectorizer

data = get_data("pcap_files/example.pcap")
data = json.loads(gen_json(data))

measurements = [x for x in data.values()]
vec = DictVectorizer()
X = vec.fit_transform(measurements).toarray()

# DBSCAN
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn import metrics

eps = 4
min_samples = 2
db=DBSCAN(eps=eps, min_samples=min_samples, metric='euclidean').fit(X)

core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True

print("Number of Data : {0}\n".format(len(db.labels_)))
print("params : eps = {0}, min_samples = {1}\n". format(eps,min_samples))
print('※ cluster labels : -1 is noise point\n')
print('> OUTPUT')
print(db.labels_)

labels = db.labels_
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)

## Plot
unique_labels = set(labels)
colors = [plt.cm.Spectral(each)
          for each in np.linspace(0, 1, len(unique_labels))]
for k, col in zip(unique_labels, colors):
    if k == -1: col = [0, 0, 0, 1]

    class_member_mask = (labels == k)
    
    xy = X[class_member_mask & core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
             markeredgecolor='k', markersize=14)
    xy = X[class_member_mask & ~core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
             markeredgecolor='k', markersize=6)

plt.title('Estimated number of clusters: %d' % n_clusters_)
plt.show()
