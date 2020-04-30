# ML
from FlowRecoder import get_data, gen_json

if __name__ == "__main__":
    data = get_data("pcap_files/example.pcap")
    print(gen_json(data))
