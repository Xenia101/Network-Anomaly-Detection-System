import numpy as np
import pandas as pd
import Preprocessing
import matplotlib.pyplot as plt
from sklearn.neighbors import LocalOutlierFactor
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
from   sklearn.discriminant_analysis import LinearDiscriminantAnalysis

def NormalAccuracy(X, y):
    clf = LocalOutlierFactor(n_neighbors=2)
    clf.fit_predict(X)
    y_pred = clf.fit_predict(X)
    accuracy = accuracy_score(y, y_pred)
    print(accuracy)

path = "./CIC-output/1.csv"
X = Preprocessing.load_df(path)
y = np.array([0 for x in range(len(X[0:910]))] + [1 for x in range(len(X[910:1806]))] + [2 for x in range(len(X[1806:]))])

X = X.to_numpy()

scaler = StandardScaler().fit(X)
X = scaler.transform(X)

lda = LinearDiscriminantAnalysis(n_components=2)
X_r = lda.fit(X, y).transform(X)

colors = ['blue', 'red', 'red']
target_names = ['normal','attack - 1','attack - 2']
lw = 2

plt.figure()
for color, i, target_name in zip(colors, [0, 1,2], target_names):
    plt.scatter(X_r[y == i, 0], X_r[y == i, 1], alpha=.4, color=color, label=target_name, s=5)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('LDA of dataset')

plt.show()
