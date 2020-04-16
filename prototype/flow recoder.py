import sys
import hashlib
from hashlib import md5
from scapy.all import *
from tcp_stream import TCPStream
import argparse

packets=rdpcap("pcap_files/example.pcap")

# flows 변경
flows = dict()

attrs = ['src','sport','dst','dport','proto','push_flag_ratio','average_len','average_payload_len','pkt_count','flow_average_inter_arrival_time','kolmogorov','shannon']

packets = [ pkt for pkt in packets if IP in pkt for p in pkt if TCP in p ]

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
def lookup_stream(key,reverse_key):
    if key in flows.keys():
        return key,flows[key]
    elif reverse_key in flows.keys():
        return reverse_key,flows[reverse_key]
    else:
        return key,None
    
for pkt in packets:
    flow_tuple = reverse_flow_tuple = key_to_search = None
    flow_tuple,reverse_flow_tuple = create_flow_keys(pkt[IP])
    flow_key,tcp_stream = lookup_stream(flow_tuple,reverse_flow_tuple)

    if tcp_stream is None:
        tcp_stream = TCPStream(pkt[IP])
    else:
        tcp_stream.add(pkt[IP])
    flows[flow_key] = tcp_stream

for flow in flows.values():
    print("%s,%s,%s,%s,%s,%s,%.3f,%s,%s,%s,%s"%(proto_name(flow.sport,flow.dport),flow.src,flow.sport,flow.dst,flow.dport,flow.proto,flow.push_flag_ratio(),flow.avrg_len(),flow.avrg_payload_len(),flow.pkt_count,flow.avrg_inter_arrival_time()))
