import pandas as pd

def RemoveCol():
    df = pd.read_csv("./CIC-output/http-flood.pcap_Flow.csv", encoding="ISO-8859-1")
    df.drop(['Flow ID', 'Src Port', 'Label'], axis='columns', inplace=True)
    return df
