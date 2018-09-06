#  Dimension reduction (차원 축소)

Feature의 수가 많으면 -> 데이터 분석 어려움 / 시각화 어려움 / 연산량 많아짐 / 더 많은 양의 data 필요 

따라서 feature의 수를 줄이자!!

1. Feature selection

   데이터를 잘 나타내는 몇 개의 필드만을 선택

2. Feature extraction 

- PCA(Principle Component Analysis) - 주성분 분석

  - 새로운 필드를 생성 - 원본 데이터와의 관계 알기 어려움


  - 데이터의 변화 폭이 가장 큰 축(그것을 새 축으로)

  - ```

    ```

  - 그 축에 직교하는 축 중에서 변화 폭이 가장 큰 축

  - 데이터의 중심을 (0,0)으로 하여 축을 뒤트는 것과 같음

  - 몇 가지의 축만을 사용 -> 데이터의 특징 손실 있지만 전반적 특성 파악에 큰 영향 없음

- NMF(Non-negative Matrix Factorization) - 비음수 행렬 인수분해

  - 새로운 필드를 생성 - 원본 데이터와의 관계 확인 가능
  - 원본 행렬을 두 개의 행렬로 분리(Weight matrix - 제목과의 관계 / Feature matrix - 특성과의 관계)



