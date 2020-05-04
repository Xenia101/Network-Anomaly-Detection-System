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

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=2).fit(X)
labels = kmeans.labels_
centers = kmeans.cluster_centers_
