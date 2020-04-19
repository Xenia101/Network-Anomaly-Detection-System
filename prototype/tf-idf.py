from FlowRecoder import get_data
from FlowRecoder import gen_json
import json
from sklearn.feature_extraction import DictVectorizer

data = get_data("pcap_files/example.pcap")
data = json.loads(gen_json(data))

measurements = [x for x in data.values()]

vec = DictVectorizer()
result = vec.fit_transform(measurements).toarray()
print(vec.fit_transform(measurements))
#print(vec.get_feature_names())
