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

y = labels

from sklearn.metrics import confusion_matrix 
from sklearn.model_selection import train_test_split
from sklearn.metrics import plot_confusion_matrix
from sklearn import svm, datasets
from sklearn.svm import SVC

class_names = y
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0) 
classifier = svm.SVC(kernel='linear', C=0.01).fit(X_train, y_train)
np.set_printoptions(precision=4)

titles_options = [("Confusion matrix, without normalization", None), ("Normalized confusion matrix", 'true')]
for title, normalize in titles_options:
    disp = plot_confusion_matrix(classifier, X_test, y_test,
                                 display_labels=class_names,
                                 cmap=plt.cm.Blues,
                                 normalize=normalize)
    disp.ax_.set_title(title)
    print(title)
    print(disp.confusion_matrix)
plt.show()
