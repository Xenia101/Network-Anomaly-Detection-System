# Network Anomaly Detection System

<p align=center>
  <img src="https://github.com/Xenia101/Network-Anomaly-Detection-System/blob/master/img/img1.PNG?raw=true">
</p>

## Train / Test 데이터 상세
- Train Dataset
  - Local에서 모은 웹서핑, 게임 등 기타 작업 시의 네트워크 패킷(`.pcap`)에 대한 64,368개의 정상 세션 데이터(`.csv`)

- Test Dataset (비정상 세션 데이터)

| File name 	| Total number of Sessions 	|                          Type                         	| Extension 	| Source 	|
|:---------:	|:------------------------:	|:-----------------------------------------------------:	|:---------:	|:------:	|
|  Normal-1 	|            81            	|                   Web surfing / Game                  	|    .csv   	|  Local 	|
|  Normal-2 	|            80            	|                   Web surfing / Game                  	|    .csv   	|  Local 	|
|  Attack-1 	|            418           	|                       http-flood                      	|    .csv   	|  Link  	|
|  Attack-2 	|            609           	|                     Mirai malware                     	|    .csv   	|  Link  	|
|  Attack-3 	|            896           	| The major fraud and hacking criminal case "B 8322-16" 	|    .csv   	|  Link  	|
|  Attack-4 	|            509           	|                Packet Injection Attacks               	|    .csv   	|  Link  	|

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
- CICFlowMeter로 나온 84개의 Feature 중 아래 78개의 Features 사용

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
