import sys
import hashlib
import json
from hashlib import md5
from scapy.all import *
from tcp_stream import TCPStream
import argparse
from entropy import kolmogorov, shannon

attrs = ['src','sport','dst',
         'dport','proto','push_flag_ratio',
         'average_len','average_payload_len',
         'pkt_count','flow_average_inter_arrival_time']

def proto_name(sport,dport,use_dpi=False,payload=None):
    if dport == 80 or sport == 80:
        return "http"
    if dport == 3306 or sport == 3306:
        return "mysql"
    if dport == 22 or sport == 22:
        return "ssh"
    return "None"

def create_forward_flow_key(pkt):
    return "%s:%s->%s:%s:%s"%(pkt.src,pkt.sport,pkt.dst,pkt.dport,pkt.proto)

def create_reverse_flow_key(pkt):
    return "%s:%s->%s:%s:%s"%(pkt.dst,pkt.dport,pkt.src,pkt.sport,pkt.proto)

def create_flow_keys(pkt):
    return create_forward_flow_key(pkt),create_reverse_flow_key(pkt)

def gen_json(flows):
    result = dict()
    index = 1
    for flow in flows.values():
        data = dict()
        data['proto_name']              = proto_name(flow.sport,flow.dport)
        data['src']                     = flow.src
        data['sport']                   = flow.sport
        data['dst']                     = flow.dst
        data['dport']                   = flow.dport
        data['proto']                   = flow.proto
        data['push_flag_ratio']         = round(flow.push_flag_ratio(),2)
        data['avrg_len']                = round(flow.avrg_len(),2)
        data['avrg_payload_len']        = round(flow.avrg_payload_len(),2)
        data['pkt_count']               = flow.pkt_count
        data['avrg_inter_arrival_time'] = flow.avrg_inter_arrival_time()

        result[index] = data
        index += 1
    return json.dumps(result, indent=4, sort_keys=False)
    
def get_data(path):
    packets = rdpcap(path)
    flows = dict()
    packets = [ pkt for pkt in packets if IP in pkt for p in pkt if TCP in p ]
    for pkt in packets:
        flow_tuple = reverse_flow_tuple = key_to_search = None
        flow_tuple,reverse_flow_tuple = create_flow_keys(pkt[IP])

        if flow_tuple in flows.keys():
            flow_key,tcp_stream = flow_tuple, flows[flow_tuple]
        elif reverse_flow_tuple in flows.keys():
            flow_key,tcp_stream = reverse_flow_tuple, flows[reverse_flow_tuple]
        else:
            flow_key,tcp_stream = flow_tuple, None

        if tcp_stream is None:
            tcp_stream = TCPStream(pkt[IP])
        else:
            tcp_stream.add(pkt[IP])
        flows[flow_key] = tcp_stream
    return flows
