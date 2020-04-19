from sklearn.cluster import KMeans
import numpy as np
import csv

with open("output/examplef.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

X = np.array([x[4:] for x in data[1:]])

kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
