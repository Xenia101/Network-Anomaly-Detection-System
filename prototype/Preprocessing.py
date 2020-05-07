import pandas as pd
import numpy as np

S_data = ['Flow ID', 'Src IP', 'Src Port', 'Dst IP', 'Timestamp', 'Label']
L_data = ['Flow ID', 'Src Port', 'Timestamp', 'Label']

def RemoveCol(path, mode):
    if mode is 1:
        df = pd.read_csv(path, encoding="ISO-8859-1")
        df.drop(S_data, axis='columns', inplace=True)
        return df
    elif mode is 2:
        df = pd.read_csv(path, encoding="ISO-8859-1")
        df.drop(L_data, axis='columns', inplace=True)
        return df
    else:
        return "mode [1 : small amounts of data] [2 : Large amounts of data]"

def load_data(path):
    df = RemoveCol(path, 1)
    if df.isnull().values.any():
        df = df[~df.isin([np.nan, np.inf, -np.inf]).any(1)]
        df = df[df['Flow Byts/s'] != 'Infinity']
        df = df[df['Flow Byts/s'] != 'Nan']
        df = df[df['Flow Pkts/s'] != 'Infinity']
        df = df[df['Flow Pkts/s'] != 'Nan']
    X = df.values
    return X

def load_df(path):
    df = RemoveCol(path, 1)
    if df.isnull().values.any():
        df = df[~df.isin([np.nan, np.inf, -np.inf]).any(1)]
        df = df[df['Flow Byts/s'] != 'Infinity']
        df = df[df['Flow Byts/s'] != 'Nan']
        df = df[df['Flow Pkts/s'] != 'Infinity']
        df = df[df['Flow Pkts/s'] != 'Nan']
    return df
