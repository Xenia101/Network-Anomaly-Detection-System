import pandas as pd

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
