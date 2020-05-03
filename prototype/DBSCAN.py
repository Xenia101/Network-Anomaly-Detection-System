from FlowRecoder import get_data, gen_json
import json
import pandas as pd
import numpy as np
from sklearn.feature_extraction import DictVectorizer
import matplotlib.pyplot as plt

data = get_data("pcap_files/example.pcap")
data = json.loads(gen_json(data))

measurements = [x for x in data.values()]
vec = DictVectorizer()
X = vec.fit_transform(measurements).toarray()

# DBSCAN
from sklearn.cluster import DBSCAN
eps = 4
min_samples = 2
db=DBSCAN(eps=eps, min_samples=min_samples, metric='euclidean')
y_db = db.fit_predict(X)
print("Number of Data : {0}\n".format(len(db.labels_)))
print("params : eps = {0}, min_samples = {1}\n". format(eps,min_samples))
print('※ cluster labels : -1 is noise point\n')
print('> OUTPUT')
print(db.labels_)

print('\nnumber of clusters : ', end='')
labels = db.labels_
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
print(n_clusters_)
