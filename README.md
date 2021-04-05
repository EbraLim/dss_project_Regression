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
* New_Price 컬럼은 총 데이터 6019개 중 결측치 5195개 → New_Price 컬럼 삭제
* New_Price 컬럼을 제외한 전체 데이터에서 결측치 44개 확인 → 결측치 44개 제거
#### (2) 이상치 확인 및 제거/대체
\
<img width="1019" alt="스크린샷 2021-03-28 오후 5 40 21" src="https://user-images.githubusercontent.com/78460759/112746845-ae0be100-8fec-11eb-9fd1-42e433557f31.png">
* Kilometers_Driven 이상치 확인 → 2017년식이고 주행거리 650만km, 이상치라고 판단하여 제거
* Mileage가 0인 데이터 56개 → 결측치로 판단하고 데이터 제거
* Seats가 0인 데이터 1개 → 해당 차종 구글링해서 Seat 값 대치
* Price 이상치 확인결과 해당 차종의 정상 가격 → 해당 데이터 유지
#### (3) feature에 따른 데이터 분포 파악
* Brand와 price의 상관관계
\
\
  ![image](https://user-images.githubusercontent.com/78460759/112920515-13261a80-9144-11eb-870a-fdcf8462fe85.png)
\
► boxplot을 활용하여 브랜드별 가격 확인


* 연도에 따른 브랜드별 Power(마력)과 Price의 상관관계
\
\
  <img width="971" alt="Screen Shot 2021-03-30 at 11 05 07 AM" src="https://user-images.githubusercontent.com/78460759/112922649-ccd2ba80-9147-11eb-8af1-edf516a96794.png">
\
► x축은 Power의 중간값, y축은 Price의 평균값으로 나눠서 4분면으로 분할(가성비 파악)\
► 제1사분면 → 최신 연식의 차량과 고급 브랜드 분포\
► 제2사분면 → 가성비가 좋지않은 차량 소수 분포\
► 제3사분면 → 연식이 오래된 차종과 인도 국산차량 다수 분포\
► 제4사분면 → 가성비는 좋으나 연식이 오래된 고급 브랜드 다수 분포
### 2) Pipeline 구축 및 모델링
#### (1) Pipeline 구축
\
  ![image](https://user-images.githubusercontent.com/78460759/112746107-cf1e0300-8fe7-11eb-99e6-cb416d373d19.png)
* preprocess_X
  * X라벨의 ‘훈련/테스트 데이터’를 각각 pipeline에 input으로 입력  
    → 설정한 scaler와 encoder가 적용되어 output으로 반환
* LinearRegressionReport
  * X라벨과 Y라벨 각각의 ‘훈련/테스트 데이터’, 총 4개의 input을 입력  
    → 9번의 교차검증 결과를 반환
#### (2) 모델링
* preprocess_X 모듈
\
\
  <img width="1125" alt="스크린샷 2021-03-28 오후 4 59 17" src="https://user-images.githubusercontent.com/78460759/112745961-f0caba80-8fe6-11eb-86ae-1f9bddae7e53.png">
\
  * X_train과 Object, 총 두 개의 인자를 input으로 받음  
  * X_train으로 파이프라인을 fit시킨 후, 해당 파이프라인에 Object를 통과시켜 변환된 결과를 output으로 반환

* LinearRegressionReport 모듈
\
\
  <img width="1705" alt="스크린샷 2021-03-28 오후 5 08 36" src="https://user-images.githubusercontent.com/78460759/112746174-3f2c8900-8fe8-11eb-9aa0-fd5ed22bf814.png">
\
  * 훈련 데이터로 교차검증한 후, 동일한 모델에 테스트 데이터를 적용
  * fold 수에 따른 교차검증 결과, 그리고 모델별 훈련 데이터와 테스트 데이터의 rmse값 등을 output으로 반환

### 3) 교차검증 후 최적 모델 선택
#### (1) 교차검증 절차 및 기준
* 교차검증은 폴더 수를 2~10으로 하여, 총 9번에 걸쳐 진행
* 훈련데이터(train data)와 검증(validation data)데이터의 rmse의 평균값 (mean_of_rmse_train)은 차이가 0.5 이하는 무차별하다고 간주  
  (사유: Y라벨값 0.5는 한화 약 75만에 해당하며, 중고차 가격에서 이 정도 크기의 차이는 허용가능하다고 판단)
* 훈련데이터(train data)와 검증(validation data)데이터의 rmse의 표준편차값 (std_of_rmse_train)은 작을수록 우수하다고 간주  
  (사유: 훈련 시 과적합을 방지하기 위해 편차는 작을수록 좋다고 판단)
* 총 9번의 시행결과 중 최다 득표한 모델을 최적 모델로 간주  
\
#### (2) 교차검증 결과
![image](https://user-images.githubusercontent.com/78460759/112746264-a8ac9780-8fe8-11eb-9692-e66f4622e937.png)
* 스케일러별 교차검증결과는 아래와 같음
  * MinMax : 4표
  * Robust : 3표
  * Standard : 2표

----
## 4. 결론
* MinMax 스케일러를 사용한 모델이 최적 모델이라고 판단
* 이 때 테스트 데이터의 RMSE는 5.21 로 나타남
----
## 5. 멤버 & 수행업무
* 임현수
  * 데이터 전처리
  * Pipeline 구축 및 모델링
  * 교차검증 및 최적모델 결정
  * 프레젠테이션 자료 제작
  * 리드미 작성 (메인)

* 최민권
  * 데이터 전처리
  * 데이터 시각화
  * 프레젠테이션 자료 제작
  * 리드미 작성 (서브)

----
※ 본 프로젝트는 패스트캠퍼스 데이터사이언스 취업스쿨 16th 크롤링 프로젝트로 진행되었습니다.
