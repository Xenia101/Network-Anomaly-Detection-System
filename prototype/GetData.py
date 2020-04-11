import pyshark
cap = pyshark.LiveCapture('이더넷')

def network_conversation(packet):
  try:
    protocol = packet.transport_layer
    source_address = packet.ip.src
    source_port = packet[packet.transport_layer].srcport
    destination_address = packet.ip.dst
    destination_port = packet[packet.transport_layer].dstport
    return (f'{protocol} {source_address}:{source_port} --> {destination_address}:{destination_port}')
  except AttributeError as e:
    pass

for packet in cap.sniff_continuously():
  #print(packet)
  #break
  #try:
   #if packet.transport_layer is not None:
      #print(packet.ip)
  #except AttributeError as e:
  #  pass
  results = network_conversation(packet)
  if results != None:
      print(results)

