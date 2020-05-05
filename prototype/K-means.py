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
