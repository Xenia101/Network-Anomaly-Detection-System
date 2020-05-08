import matplotlib.pyplot as plt
import Preprocessing
import pandas as pd
import numpy as np
import random

path = "./CIC-output/normal-1.pcap_Flow.csv"
X = Preprocessing.load_df(path)
y = [random.randint(0, 1)  for x in range(len(X))]

labels = X.columns

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X, y)

importance = model.feature_importances_

f=plt.figure()
ax=f.add_subplot(1,1,1)
ax.bar(labels[:], importance[:])
plt.rcParams['lines.linewidth'] = 10
plt.xticks(ha='right', rotation=45)
plt.ylabel('Importance')
plt.show()

