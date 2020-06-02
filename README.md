# Network Anomaly Detection System

<p align=center>
  <img src="https://github.com/Xenia101/Network-Anomaly-Detection-System/blob/master/img/img1.PNG?raw=true">
</p>

> Flow Based netwrok anomaly detection system

## Train / Test 데이터 상세
- **Train Dataset**

Local에서 모은 웹서핑, 게임 등 기타 작업 시의 네트워크 패킷(`.pcap`)에 대한 64,368개의 정상 세션 데이터(`.csv`)

- **Test Dataset**

비정상 세션 데이터

| File name 	| Total number of Sessions 	|                          Type                         	| Extension 	| Source 	|
|:---------:	|:------------------------:	|:-----------------------------------------------------:	|:---------:	|:------:	|
|  Normal-1 	|            81            	|                   Web surfing / Game                  	|    `.csv`   	|  Local 	|
|  Normal-2 	|            80            	|                   Web surfing / Game                  	|    `.csv`   	|  Local 	|
|  Attack-1 	|            418           	|                       http-flood                      	|    `.csv`   	|  [Link](https://www.netresec.com/?page=PcapFiles)  	|
|  Attack-2 	|            609           	|                     Mirai malware                     	|    `.csv`   	|  [Link](https://ieee-dataport.org/open-access/iot-network-intrusion-dataset)  	|
|  Attack-3 	|            896           	| The major fraud and hacking criminal case "B 8322-16" 	|    `.csv`   	|  [Link](https://www.cert.se/2017/09/cert-se-tekniska-rad-med-anledning-av-det-aktuella-dataintrangsfallet-b-8322-16)  	|
|  Attack-4 	|            509           	|                Packet Injection Attacks               	|    `.csv`   	|  [Link](https://github.com/fox-it/quantuminsert/blob/master/presentations/brocon2015/pcaps/id1.cn-inject.pcap)  	|

## 데이터 수집 - CICFlowMeter로 나온 84개의 Features.csv
<p align=center>
  <img src="https://github.com/Xenia101/Network-Anomaly-Detection-System/blob/master/img/img2.PNG?raw=true">
</p>

## Feature Importance
- Random Forest Classifier를 이용한 Feature들의 중요도 계산 결과

<p align=center>
  <img src="https://github.com/Xenia101/Network-Anomaly-Detection-System/blob/master/img/img3.PNG?raw=true">
</p>
<p align=center>
  <img src="https://github.com/Xenia101/Network-Anomaly-Detection-System/blob/master/img/img4.PNG?raw=true">
</p>

## Feature 선정
- CICFlowMeter로 나온 84개의 Feature 중 아래 **78개의 Features** 사용

|         Flow   duration        	|       Total   Fwd Packet       	|      Total   Bwd Packets      	|    Total   Length of Fwd Packet    	|    Total   Length of Bwd Packet    	|     Fwd   Packet Length Min    	|
|:------------------------------:	|:------------------------------:	|:-----------------------------:	|:----------------------------------:	|:----------------------------------:	|:------------------------------:	|
|    Fwd   Packet Length Max     	|    Fwd   Packet Length Mean    	|    Fwd   Packet Length Std    	|       Bwd   Packet Length Min      	|       Bwd   Packet Length Max      	|    Bwd   Packet Length Mean    	|
|     Bwd   Packet Length Std    	|         Flow   Bytes/s         	|       Flow   Packets/s        	|           Flow   IAT Mean          	|           Flow   IAT Std           	|         Flow   IAT Max         	|
|         Flow   IAT Min         	|          Fwd   IAT Min         	|         Fwd   IAT Max         	|           Fwd   IAT Mean           	|            Fwd   IAT Std           	|        Fwd   IAT Total         	|
|          Bwd   IAT Min         	|          Bwd   IAT Max         	|         Bwd   IAT Mean        	|            Bwd   IAT Std           	|           Bwd   IAT Total          	|         Fwd   PSH flags        	|
|         Bwd   PSH Flags        	|         Fwd   URG Flags        	|        Bwd   URG Flags        	|         Fwd   Header Length        	|         Bwd   Header Length        	|         FWD   Packets/s        	|
|         Bwd   Packets/s        	|      Packet   Length Min       	|      Packet   Length Max      	|        Packet   Length Mean        	|         Packet   Length Std        	|    Packet   Length Variance    	|
|        FIN   Flag Count        	|        SYN   Flag Count        	|        RST   Flag Count       	|          PSH   Flag Count          	|          ACK   Flag Count          	|        URG   Flag Count        	|
|        CWE   Flag Count        	|        ECE   Flag Count        	|        down/Up   Ratio        	|        Average   Packet Size       	|       Fwd   Segment Size Avg       	|     Bwd   Segment Size Avg     	|
|      Fwd   Bytes/Bulk Avg      	|      Fwd   Packet/Bulk Avg     	|      Fwd   Bulk Rate Avg      	|        Bwd   Bytes/Bulk Avg        	|        Bwd   Packet/Bulk Avg       	|       Bwd   Bulk Rate Avg      	|
|      Subflow   Fwd Packets     	|       Subflow   Fwd Bytes      	|     Subflow   Bwd Packets     	|         Subflow   Bwd Bytes        	|        Fwd   Init Win bytes        	|      Bwd   Init Win bytes      	|
|       Fwd   Act Data Pkts      	|       Fwd   Seg Size Min       	|          Active   Min         	|            Active   Mean           	|            Active   Max            	|          Active   Std          	|
|           Idle   Min           	|           Idle   Mean          	|           Idle   Max          	|             Idle   Std             	|                                    	|                                	|

## 데이터 전처리
- 자료의 오버플로우 또는 언더플로우를 방지 하기 위해 Standard Scaler를 수행하여 전체 데이터의 분포를 평균 0, 분산 1이 되도록 데이터 전처리

<p align=center>
  <img src="https://github.com/Xenia101/Network-Anomaly-Detection-System/blob/master/img/img5.PNG?raw=true">
</p>

## Local Outlier Factor
- Anomaly Detection을 위한 LOF 수행 과정

<p align=center>
  <img src="https://github.com/Xenia101/Network-Anomaly-Detection-System/blob/master/img/img6.PNG?raw=true">
</p>

- 학습데이터(정상)에 대해 Local Outlier Factor 수행 결과(`.csv`)
<p align=center>
  <img src="https://github.com/Xenia101/Network-Anomaly-Detection-System/blob/master/img/img7.PNG?raw=true">
</p>

- 학습데이터(정상)에 대해 테스트데이터(비정상) 추가 후 Local Outlier Factor 수행 결과(`.csv`)
<p align=center>
  <img src="https://github.com/Xenia101/Network-Anomaly-Detection-System/blob/master/img/img8.PNG?raw=true">
</p>

## Latent Dirichlet Allocation

<p align=center>
  <img src="https://github.com/Xenia101/Network-Anomaly-Detection-System/blob/master/img/img9.PNG?raw=true">
</p>

## 시험 결과

|    File   name    	|    Total   number of Sessions    	|    Number   of inliner    	|    Number   of outlier    	|    outlier   percentage    	|
|:-----------------:	|:--------------------------------:	|:-------------------------:	|:-------------------------:	|:--------------------------:	|
|    Normal–1       	|                81                	|             68            	|             13            	|           16.04%           	|
|    Normal–2       	|                80                	|             67            	|             13            	|           16.25%           	|
|    Attack–1       	|                418               	|            169            	|            249            	|           59.56%           	|
|    Attack–2       	|                609               	|            297            	|            312            	|           51.23%           	|
|    Attack–3       	|                896               	|            377            	|            519            	|           57.92%           	|
|    Attack-4       	|                509               	|             31            	|            478            	|           93.90%           	|

| File   name 	|                              Type                              	| Source 	|
|:-----------:	|:--------------------------------------------------------------:	|:------:	|
| Normal–1    	|                      Web   surfing / Game                      	|  Local 	|
| Normal–2    	|                      Web   surfing / Game                      	|  Local 	|
| Attack–1    	|                           http-flood                           	|  [Link](https://www.netresec.com/?page=PcapFiles)  	|
| Attack–2    	|                         Mirai   malware                        	|  [Link](https://ieee-dataport.org/open-access/iot-network-intrusion-dataset)  	|
| Attack–3    	| The   major fraud and hacking criminal     case   "B 8322-16". 	|  [Link](https://www.cert.se/2017/09/cert-se-tekniska-rad-med-anledning-av-det-aktuella-dataintrangsfallet-b-8322-16)  	|
| Attack-4    	|                   Packet   Injection Attacks                   	|  [Link](https://github.com/fox-it/quantuminsert/blob/master/presentations/brocon2015/pcaps/id1.cn-inject.pcap)  	|

## 결론
본 기술에서는 네트워크가 정상일 때, Flow기반으로 IP별 네트워크 세션을 수집하여 학습 데이터셋을 만들었다. 

이를 바탕으로 모델을 학습시킨 후, 테스트 데이터인 비정상 네트워크 세션에 대한 이상 행위 탐지를 수행하였다.

학습을 실시하고 성능을 분석해 본 결과 **평균 86%** 의 정확도로 네트워크 이상행위 탐지가 가능했다.

## 결과물 활용 방안

- 네트워크상의 데이터 흐름에 대한 탁월한 가시성 제공으로 효율적인 모니터링 가능

- 모니터링과 더불어 실시간 패킷 분석을 통해 신속한 대응 가능

- 네트워크 IP별 패킷에 대한 데이터를 학습하고 이상 징후 탐지 가능

→ 통합보안관제 적용시, 실시간 침해 처리, 범위 확대 및 인력과 시간 단축을 할 수 있으며, 알려지지 않은 위협에 대해서도 탐지 및 대응 가능

## 설치 및 운영 방안

<p align=center>
  <img src="https://github.com/Xenia101/Network-Anomaly-Detection-System/blob/master/img/img10.PNG?raw=true">
</p>

- 간단하고 빠른 결과 분석 및 즉각적인 피드백

- 보다  빠른 연산을 위해 GPU 연산 수행

- 데이터의 수가 막대할 경우, Feature 선택시 IP 주소 추가

## Feature & Descriptions

|            Flow   duration          	|                                     Duration   of the flow in Microsecond                                   	|
|:-----------------------------------:	|:-----------------------------------------------------------------------------------------------------------:	|
|          total   Fwd Packet         	|                                   Total   packets in the forward direction                                  	|
|          total   Bwd packets        	|                                   Total   packets in the backward direction                                 	|
|     total   Length of Fwd Packet    	|                                  Total   size of packet in forward direction                                	|
|     total   Length of Bwd Packet    	|                                 Total   size of packet in backward direction                                	|
|       Fwd   Packet Length Min       	|                                 Minimum   size of packet in forward direction                               	|
|        Fwd   Packet Length Max      	|                                 Maximum   size of packet in forward direction                               	|
|       Fwd   Packet Length Mean      	|                                  Mean   size of packet in forward direction                                 	|
|        Fwd   Packet Length Std      	|                           Standard   deviation size of packet in forward direction                          	|
|        Bwd   Packet Length Min      	|                                Minimum   size of packet in backward direction                               	|
|        Bwd   Packet Length Max      	|                                Maximum   size of packet in backward direction                               	|
|       Bwd   Packet Length Mean      	|                                  Mean   size of packet in backward direction                                	|
|        Bwd   Packet Length Std      	|                           Standard   deviation size of packet in backward direction                         	|
|            Flow   Bytes/s           	|                                       Number   of flow bytes per second                                     	|
|           Flow   Packets/s          	|                                     Number   of flow packets per second                                     	|
|            Flow   IAT Mean          	|                               Mean   time between two packets sent in the flow                              	|
|            Flow   IAT Std           	|                        Standard   deviation time between two packets sent in the flow                       	|
|            Flow   IAT Max           	|                              Maximum   time between two packets sent in the flow                            	|
|            Flow   IAT Min           	|                              Minimum   time between two packets sent in the flow                            	|
|             Fwd   IAT Min           	|                       Minimum   time between two packets sent in the forward direction                      	|
|             Fwd   IAT Max           	|                       Maximum   time between two packets sent in the forward direction                      	|
|            Fwd   IAT Mean           	|                         Mean   time between two packets sent in the forward direction                       	|
|             Fwd   IAT Std           	|                  Standard   deviation time between two packets sent in the forward direction                	|
|            Fwd   IAT Total          	|                        Total   time between two packets sent in the forward direction                       	|
|             Bwd   IAT Min           	|                       Minimum   time between two packets sent in the backward direction                     	|
|             Bwd   IAT Max           	|                       Maximum   time between two packets sent in the backward direction                     	|
|            Bwd   IAT Mean           	|                        Mean   time between two packets sent in the backward direction                       	|
|             Bwd   IAT Std           	|                 Standard   deviation time between two packets sent in the backward direction                	|
|            Bwd   IAT Total          	|                        Total   time between two packets sent in the backward direction                      	|
|            Fwd   PSH flags          	|      Number   of times the PSH flag was set in packets travelling in the forward direction   (0 for UDP)    	|
|            Bwd   PSH Flags          	|     Number   of times the PSH flag was set in packets travelling in the backward direction   (0 for UDP)    	|
|            Fwd   URG Flags          	|      Number   of times the URG flag was set in packets travelling in the forward direction   (0 for UDP)    	|
|            Bwd   URG Flags          	|     Number   of times the URG flag was set in packets travelling in the backward direction   (0 for UDP)    	|
|          Fwd   Header Length        	|                            Total   bytes used for headers in the forward direction                          	|
|          Bwd   Header Length        	|                           Total   bytes used for headers in the backward direction                          	|
|            FWD   Packets/s          	|                                    Number   of forward packets per second                                   	|
|            Bwd   Packets/s          	|                                    Number   of backward packets per second                                  	|
|         Packet   Length Min         	|                                         Minimum   length of a packet                                        	|
|          Packet   Length Max        	|                                         Maximum   length of a packet                                        	|
|         Packet   Length Mean        	|                                           Mean   length of a packet                                         	|
|          Packet   Length Std        	|                                    Standard   deviation length of a packet                                  	|
|       Packet   Length Variance      	|                                         Variance   length of a packet                                       	|
|           FIN   Flag Count          	|                                         Number   of packets with FIN                                        	|
|           SYN   Flag Count          	|                                         Number   of packets with SYN                                        	|
|           RST   Flag Count          	|                                         Number   of packets with RST                                        	|
|           PSH   Flag Count          	|                                         Number   of packets with PUSH                                       	|
|           ACK   Flag Count          	|                                         Number   of packets with ACK                                        	|
|           URG   Flag Count          	|                                         Number   of packets with URG                                        	|
|           CWE   Flag Count          	|                                         Number   of packets with CWE                                        	|
|           ECE   Flag Count          	|                                         Number   of packets with ECE                                        	|
|            down/Up   Ratio          	|                                          Download   and upload ratio                                        	|
|        Average   Packet Size        	|                                           Average   size of packet                                          	|
|        Fwd   Segment Size Avg       	|                               Average   size observed in the forward direction                              	|
|        Bwd   Segment Size Avg       	|                         Average   number of bytes bulk rate in the backward direction                       	|
|         Fwd   Bytes/Bulk Avg        	|                         Average   number of bytes bulk rate in the forward direction                        	|
|         Fwd   Packet/Bulk Avg       	|                        Average   number of packets bulk rate in the forward direction                       	|
|         Fwd   Bulk Rate Avg         	|                            Average   number of bulk rate in the forward direction                           	|
|         Bwd   Bytes/Bulk Avg        	|                         Average   number of bytes bulk rate in the backward direction                       	|
|         Bwd   Packet/Bulk Avg       	|                        Average   number of packets bulk rate in the backward direction                      	|
|          Bwd   Bulk Rate Avg        	|                            Average   number of bulk rate in the backward direction                          	|
|         Subflow   Fwd Packets       	|                    The   average number of packets in a sub flow in the forward direction                   	|
|          Subflow   Fwd Bytes        	|                     The   average number of bytes in a sub flow in the forward direction                    	|
|         Subflow   Bwd Packets       	|                    The   average number of packets in a sub flow in the backward direction                  	|
|          Subflow   Bwd Bytes        	|                     The   average number of bytes in a sub flow in the backward direction                   	|
|         Fwd   Init Win bytes        	|                  The   total number of bytes sent in initial window in the forward direction                	|
|         Bwd   Init Win bytes        	|                 The   total number of bytes sent in initial window in the backward direction                	|
|          Fwd   Act Data Pkts        	|             Count   of packets with at least 1 byte of TCP data payload in the forward direction            	|
|          Fwd   Seg Size Min         	|                           Minimum   segment size observed in the forward direction                          	|
|             Active   Min            	|                             Minimum   time a flow was active before becoming idle                           	|
|             Active   Mean           	|                              Mean   time a flow was active before becoming idle                             	|
|             Active   Max            	|                             Maximum   time a flow was active before becoming idle                           	|
|             Active   Std            	|                       Standard   deviation time a flow was active before becoming idle                      	|
|              Idle   Min             	|                             Minimum   time a flow was idle before becoming active                           	|
|              Idle   Mean            	|                              Mean   time a flow was idle before becoming active                             	|
|              Idle   Max             	|                             Maximum   time a flow was idle before becoming active                           	|
|              Idle   Std             	|                       Standard   deviation time a flow was idle before becoming active                      	|

## References

- 머신러닝을 이용한 개인용pc 악성코드 감염 예측
- 네트워크에서 SVM을 기반으로하는 DDoS 공격 탐지 방법
- MAML 알고리즘을 활용한 Ddos 공격 탐지 시스템
- Machine Learning 알고리즘을 적용한 인터넷 애플리케이션
- Intrusion Detection System
- Likelihood of a Personal Computer to Be Infected with Malware
- Anomaly based unknown Intrusion Detection in Endpoint environments
- Network traffic features for anomaly detection in specific industrial control system network
