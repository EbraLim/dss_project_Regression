# 회귀분석을 통한 인도 중고차 가격 예측 모델링
## 프로젝트 개요
### 프로젝트 주제
* 인도 중고차데이터를 통한 중고차 가격 예측
### 분석 프로세스
* 데이터 수집 -> 전처리&시각화 -> Pipeline 구축 및 모델링
## 상세 프로세스
### 1) 데이터 수집
* [Kaggle](https://www.kaggle.com/avikasliwal/used-cars-price-prediction) \
데이터 6019건(컬럼 13개)
### 2) 전처리 & 시각화
* 결측치 확인 및 제거

\
<img width="942" alt="스크린샷 2021-03-28 오후 5 39 39" src="https://user-images.githubusercontent.com/78460759/112746836-959bc680-8fec-11eb-8634-4fdaca278161.png">
* 이상치 확인 및 제거 or 대체

\
<img width="1019" alt="스크린샷 2021-03-28 오후 5 40 21" src="https://user-images.githubusercontent.com/78460759/112746845-ae0be100-8fec-11eb-9fd1-42e433557f31.png">
* 시각화(어떤 자료를 넣을지)
## Pipeline 구축 및 모델링
### Pipeline 구조도
\
\
  ![image](https://user-images.githubusercontent.com/78460759/112746107-cf1e0300-8fe7-11eb-99e6-cb416d373d19.png)

### 모델링
* preprocess_X 모듈
\
\
  <img width="1125" alt="스크린샷 2021-03-28 오후 4 59 17" src="https://user-images.githubusercontent.com/78460759/112745961-f0caba80-8fe6-11eb-86ae-1f9bddae7e53.png">

* LinearRegressionReport 모듈
\
\
  <img width="1705" alt="스크린샷 2021-03-28 오후 5 08 36" src="https://user-images.githubusercontent.com/78460759/112746174-3f2c8900-8fe8-11eb-9aa0-fd5ed22bf814.png">

## 결론
### cv fold별 결과

![image](https://user-images.githubusercontent.com/78460759/112746264-a8ac9780-8fe8-11eb-9692-e66f4622e937.png)

### 예측 결과
#### 판단 기준:
1. 교차검증 결과 rmse의 평균 (mean_of_rmse_train)은 차이가 0.5 이하(한화 약 75만원)는 무차별
2. 교차검증 결과 rmse의 표준편차 (std_of_rmse_train)는 작을수록 우수(과적합을 방지하기 위해 편차는 작을수록 좋다고 판단했기 때문)
3. 총 9가지의 fold (cv=2~10) 중 최다 득표 모델 선정

#### 스케일링 방법별 결과
  * MinMax : 4표
  * Standard : 2표
  * Robust : 3표
\
\
► 결론: 4표로 최다 득표한 MinMax Scaler를 사용한 모델이 가장 우수한 모델
## 추후 개선 방향
### preprocess_X 함수 개선
* scaler 별로 반복문 돌도록 함수 하나로 합치기 또는 함수를 여러 개 만든 후 Preprocessing 모듈 내에 통합
### LinearRegressionReport 함수 개선
* model 별로 반복문 돌도록 함수 하나로 합치기 또는 함수를 여러 개 만든 후 MakeReport 모듈 내에 통합

## Reference

