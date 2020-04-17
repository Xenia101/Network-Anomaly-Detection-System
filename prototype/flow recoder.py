import sys
import hashlib
import json
from hashlib import md5
from scapy.all import *
from tcp_stream import TCPStream
import argparse

attrs = ['src','sport','dst','dport','proto','push_flag_ratio','average_len','average_payload_len','pkt_count','flow_average_inter_arrival_time','kolmogorov','shannon']

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

def gen_json(flow):
    print(flow)
    #return json

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
    
    #for flow in flows.values():
    #    print(proto_name(flow.sport,flow.dport))
    #    print(flow.src)
    #    print(flow.sport)
    #    print(flow.dst)
    #    print(flow.dport)
    #    print(flow.proto)
    #    print(flow.push_flag_ratio())
    #    print(flow.avrg_len())
    #    print(flow.avrg_payload_len())
    #    print(flow.pkt_count)
    #    print(flow.avrg_inter_arrival_time())
    #    break
    
if __name__ == "__main__":
    data = get_data("pcap_files/example.pcap")
    gen_json(data)
