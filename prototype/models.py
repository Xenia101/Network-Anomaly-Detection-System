# ML
from FlowRecoder import get_data
from FlowRecoder import gen_json

if __name__ == "__main__":
    data = get_data("pcap_files/example.pcap")
    print(gen_json(data))
