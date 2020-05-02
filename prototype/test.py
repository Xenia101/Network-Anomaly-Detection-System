from FlowRecoder import get_data, gen_json
import pandas as pd
import numpy as np
from sklearn.feature_extraction import DictVectorizer
import json
import matplotlib.pyplot as plt
from sklearn.neighbors import LocalOutlierFactor

data = get_data("pcap_files/example.pcap")
data = json.loads(gen_json(data))

##DictVectorizer
measurements = [x for x in data.values()]
vec = DictVectorizer()
X = vec.fit_transform(measurements).toarray()

clf = LocalOutlierFactor(n_neighbors=20, contamination=0.1)
y = clf.fit_predict(X)

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
print(kmeans.labels_)
