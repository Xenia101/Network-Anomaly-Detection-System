import pyshark
pcap_reader = pyshark.LiveCapture('이더넷')
for packet in pcap_reader.sniff_continuously():
    print(packet)
