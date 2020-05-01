from FlowRecoder import get_data, gen_json
import json
import pandas as pd
import numpy as np
from sklearn.feature_extraction import DictVectorizer
import matplotlib.pyplot as plt

#data = get_data("pcap_files/example.pcap")
data = get_data("pcap_files/normal/smallFlows.pcap")
data = json.loads(gen_json(data))

measurements = [x for x in data.values()]

vec = DictVectorizer()
X = vec.fit_transform(measurements).toarray()

## LOF scores
from sklearn.neighbors import LocalOutlierFactor
clf = LocalOutlierFactor(n_neighbors=3, contamination=0.1)
y_pred = clf.fit(X)
X_scores = clf.negative_outlier_factor_
X_scores = np.array(X_scores, dtype=np.float64)

print(-X_scores)

## Kmeans
#from sklearn.cluster import KMeans
#kmeans = KMeans(n_clusters=1).fit(X)
#labels = kmeans.labels_
#centers = kmeans.cluster_centers_
#plt.scatter(X[:,0], X[:,1],c = kmeans.fit_predict(X), cmap='rainbow')
#plt.show()






#print(vec.fit_transform(measurements))
#print(vec.get_feature_names())
