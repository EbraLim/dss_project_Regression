[Regression Project]  
인도 중고차 가격예측 모델링
======================
## 목차
```
0. 요약
1. 소개
2. 분석 프로세스
3. 각 프로세스별 상세설명
4. 결론
5. 멤버 & 수행업무
```
----
## 0. 요약
```
1) 총 11개의 컬럼을 활용한 중고차 가격예측 모델링
2) 다중 선형회귀 모델 사용, 3가지 scaler (MinMax, Standard, Robust) 사용
3) 9개의 fold수 (2~10)를 적용하여 교차 검증 시행, 최다 득표 모델 선택
4) MinMax scaler가 4표로 최다 득표, test set의 RMSE는 약 5.21
```
----
## 1. 소개
### 1) 주제
* 회귀분석을 활용한 인도 중고차 가격예측 모델링
### 2) 데이터 출처
* [Kaggle](https://www.kaggle.com/avikasliwal/used-cars-price-prediction)
### 3) 데이터 형태
* 6019 rows x 13 columns
----
## 2. 분석 프로세스
### 1) 데이터 전처리 및 시각화
* 결측치/이상치 처리 및 feature에 따른 데이터 분포 파악
### 2) Pipeline 구축 및 모델링
### 3) 교차검증 후 최적 모델 선택
----
## 3. 각 프로세스별 상세설명
### 1) 데이터 전처리 및 시각화
#### (1) 결측치 확인 및 제거
\
<img width="942" alt="스크린샷 2021-03-28 오후 5 39 39" src="https://user-images.githubusercontent.com/78460759/112746836-959bc680-8fec-11eb-8634-4fdaca278161.png">
* New_Price 컬럼은 총 데이터 6019개 중 결측치 5195개 -> New_Price 컬럼 삭제
* New_Price 컬럼을 제외한 전체 데이터에서 결측치 44개 확인 -> 결측치 44개 제거
#### (2) 이상치 확인 및 제거/대체
\
<img width="1019" alt="스크린샷 2021-03-28 오후 5 40 21" src="https://user-images.githubusercontent.com/78460759/112746845-ae0be100-8fec-11eb-9fd1-42e433557f31.png">
* Kilometers_Driven 이상치 확인 -> 2017년식 주행거리 650만km, 이상치라고 판단하여 제거
* Mileage가 0인 데이터 56개 -> 결측치로 판단하고 데이터 제거
* Seats가 0인 데이터 1개 -> 해당 차종 구글링해서 Seat 값 대체
* Price 이상치 확인결과 해당 차종에 알맞는 가격 -> 해당 데이터 유지
#### (3) feature에 따른 데이터 분포 파악
* Brand와 price의 상관관계
\
\
  ![image](https://user-images.githubusercontent.com/78460759/112920515-13261a80-9144-11eb-870a-fdcf8462fe85.png)
\
► boxplot을 활용하여 브랜드별 가격 확인


* 년도에 따른 브랜드별 Power(마력)과 Price의 상관관계
\
\
  <img width="971" alt="Screen Shot 2021-03-30 at 11 05 07 AM" src="https://user-images.githubusercontent.com/78460759/112922649-ccd2ba80-9147-11eb-8af1-edf516a96794.png">
\
► x축은 Power의 중간값, y축은 Price의 평균값으로 나눠서 4분면으로 분할(가성비 파악)\
► 제1사분면 -> 최신 년식의 차량과 고급브랜드 분포\
► 제2사분면 -> 가성비가 좋지않은 차량 소수 분포\
► 제3사분면 -> 년식이 오랜된 차종과 인도 국산차량 다수 분포\
► 제4사분면 -> 가성비는 좋지만 년식이 오래된 고급브랜드 다수 분포
### 2) Pipeline 구축 및 모델링
#### (1) Pipeline 구축
\
  ![image](https://user-images.githubusercontent.com/78460759/112746107-cf1e0300-8fe7-11eb-99e6-cb416d373d19.png)
* (구조도 삽입 및 설명 간단하게 몇 줄로 요약하여 추가)
#### (2) 모델링
* preprocess_X 모듈
\
\
  <img width="1125" alt="스크린샷 2021-03-28 오후 4 59 17" src="https://user-images.githubusercontent.com/78460759/112745961-f0caba80-8fe6-11eb-86ae-1f9bddae7e53.png">

* LinearRegressionReport 모듈
\
\
  <img width="1705" alt="스크린샷 2021-03-28 오후 5 08 36" src="https://user-images.githubusercontent.com/78460759/112746174-3f2c8900-8fe8-11eb-9aa0-fd5ed22bf814.png">
* (두 개 각각의 모듈에 대해 간략히 설명 요약하여 추가)
### 3) 교차검증 후 최적 모델 선택
#### (1) 교차검증 절차 및 기준
* (“cv=2~10으로 했고, mean과 std에 어떤 기준을 적용했고, 최적 모델  판단 기준 (최다득표)”라는 내용을 짧게 요약하여 추가)
```
(예시, 수정필요)
판단 기준:
1. 교차검증 결과 rmse의 평균 (mean_of_rmse_train)은 차이가 0.5 이하(한화 약 75만원)는 무차별
2. 교차검증 결과 rmse의 표준편차 (std_of_rmse_train)는 작을수록 우수(과적합을 방지하기 위해 편차는 작을수록 좋다고 판단했기 때문)
3. 총 9가지의 fold (cv=2~10) 중 최다 득표 모델 선정
```
#### (2) 교차검증 결과
![image](https://user-images.githubusercontent.com/78460759/112746264-a8ac9780-8fe8-11eb-9692-e66f4622e937.png)
* (각 몇 표로 어떤 모델이 최적 모델로 선정되었는지 한 문장으로 요약하여 추가)
```
(예시, 수정필요)
스케일링 방법별 결과
  * MinMax : 4표
  * Standard : 2표
  * Robust : 3표
```

----
## 4. 결론
* (“Minmax가 4표로 최적 모델로 선정되었고, 이 때 test_set의 RMSE는 5.xx으로 나왔다”를 한 문장으로 추가)
```
► 결론: 4표로 최다 득표한 MinMax Scaler를 사용한 모델이 가장 우수한 모델
```
----
## 5. 멤버 & 수행업무
* 임현수
  * (내용)
  * (내용)

* 최민권
  * (내용)
  * (내용)

----
※ 본 프로젝트는 패스트캠퍼스 데이터사이언스 취업스쿨 16th 크롤링 프로젝트로 진행되었습니다.
