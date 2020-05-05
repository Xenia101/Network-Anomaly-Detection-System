import Preprocessing

if __name__ == "__main__":
    path = "./CIC-output/http-flood.pcap_Flow.csv"
    data = Preprocessing.RemoveCol(path, 1)

    print(data)
