# Network Anomaly Detection System

<p align=center>
  <img src="https://github.com/Xenia101/Network-Anomaly-Detection-System/blob/master/img/img1.PNG?raw=true">
</p>

## Train / Test 데이터 상세
- Train Dataset

Local에서 모은 웹서핑, 게임 등 기타 작업 시의 네트워크 패킷(`.pcap`)에 대한 64,368개의 정상 세션 데이터(`.csv`)

- Test Dataset 

비정상 세션 데이터

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

|    File   name    	|                                 Type                                	|    Source    	|    Number   of outlier    	|    outlier   percentage    	|
|:-----------------:	|:-------------------------------------------------------------------:	|:------------:	|:-------------------------:	|:--------------------------:	|
|    Normal–1       	|                         Web   surfing / Game                        	|     Local    	|             13            	|           16.04%           	|
|    Normal–2       	|                         Web   surfing / Game                        	|     Local    	|             13            	|           16.25%           	|
|    Attack–1       	|                              http-flood                             	|     Link     	|            249            	|           59.56%           	|
|    Attack–2       	|                           Mirai   malware                           	|     Link     	|            312            	|           51.23%           	|
|    Attack–3       	|    The   major fraud and hacking criminal    case   "B 8322-16".    	|     Link     	|            519            	|           57.92%           	|
|    Attack-4       	|                      Packet   Injection Attacks                     	|     Link     	|            478            	|           93.90%           	|

## 결론
본 기술에서는 네트워크가 정상일 때, Flow기반으로 IP별 네트워크 세션을 수집하여 학습 데이터셋을 만들었다. 

이를 바탕으로 모델을 학습시킨 후, 테스트 데이터인 비정상 네트워크 세션에 대한 이상 행위 탐지를 수행하였다.

학습을 실시하고 성능을 분석해 본 결과 **평균 86%**의 정확도로 네트워크 이상행위 탐지가 가능했다.


