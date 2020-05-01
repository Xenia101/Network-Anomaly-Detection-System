# ML
from FlowRecoder import get_data, gen_json
import requests
import json

if __name__ == "__main__":
    data = get_data("pcap_files/example.pcap")

    for param in json.loads(gen_json(data)).values():
        URL = "http://withme.xyz:5000/flow"
        data = requests.post(URL, data = param)
        print(data.json())
        break
