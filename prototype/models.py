# ML
import FlowRecoder

if __name__ == "__main__":
    data = FlowRecoder.get_data("pcap_files/example.pcap")
    print(FlowRecoder.gen_json(data))
