from FlowRecoder import get_data
from FlowRecoder import gen_json
import csv
import json
import pandas as pd

#fInput = "malware/http-flood.pcap"
fInput = "example.pcap"

data = get_data("pcap_files/" + fInput)
data = gen_json(data)

attrs = ['proto_name','src','sport','dst',
         'dport','proto','push_flag_ratio',
         'average_len','average_payload_len',
         'pkt_count','flow_average_inter_arrival_time']

data = json.loads(data)

datas = list()
for x in dict(data).values():
    datas.append([xi for xi in x.values()])

df = pd.DataFrame(datas)
df.to_csv('output/' + (fInput.split('/')[-1]).split('.')[0] + ".csv", index=False, header=attrs)
