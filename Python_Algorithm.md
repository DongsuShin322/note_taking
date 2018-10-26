# Python을 이용한 알고리즘 해결

### 1번문제 - 카카오 비밀지도

1. 10진수 & 10진수 --> bitwise operation

- example

  a = 60            # 60 = 0011 1100 

  b = 13            # 13 = 0000 1101

  ​                      a & b = 0000 1100

  c = a & b

  print (c) --> 12

2. 10진수를 2진수로

- "{0:b}".format(10진수).zfill(원하는 자릿수에 맞게 0으로 채움)

### 2번문제 - 카카오 다트게임

1. 문자열에서 숫자만 가져오기 -> 리스트로 만들기

- list.append( ' '.join(x for x in string if x.isnumeric()))

2. list[-1] 은 끝의 element!! -> 원소가 하나여도 적용

- ex a = [1] / a[0] = a[-1]

### 기타문제

- range(1,1000) : 1000 미포함

- set(list) : 유일한 원소만 뽑아줌 set - set : possible / list - list : impossible

- random.randint() / random.randrange() 

- 올림을 구해라 : 나머지가 0이 아니면 int +1

- map(function --> lambda function과 함께 자주 쓰임, sequence --> 대부분 list) : map의 return 값은 iterator이므로, list(map(function, sequence)) 이렇게 output 출력함

  조건이 True인 원소만 뽑고 싶을 때, map대신에 filter 사용 list(filter(function, sequence))

- 연속된 정수로 이루어진 리스트 : list(range(10)) or [i for i in range(10)]

- 함수안에서 전역변수 사용하지 말것 (global 쓸 수 있으나 비추)

  - 함수 안에서 return 값을 전역변수로 대입
  - ex)  sum, x, y = sum(x,y)

- 0으로 초기화 된 N X N Matrix 생성

  [[0 for i in range(n)] for i in range(n)]

### insertion sort

- i = 0 ~ len(array)

  i = k 일때, result[k-1] > array[k] 이면 k-1하면서 계속 진행!!

- list에서 원하는 곳에 원소 삽입하는 방법 --> insert(index, value)이용

- unsorted = [1,100,40,73,5,1,2,534,61,120,11,1,3]

  result = [unsorted[0]]

  for i in range(1,len(unsorted)):
      index = i
      while result[index-1] > unsorted[i]:
          index -= 1
          if index == 0: break
      result.insert(index, unsorted[i])        

  result

### 2016 인하대 프로그래밍 경진대회 B번

- 약수의 갯수가 홀수인 것 : 약수의 갯수를 카운팅 하고 그것이 홀수인지 확인!

- ex) count = 0

         for j in range(1,i+1):
             if i % j == 0:
                 count += 1
         if not count % 2 == 0:
             num += 1

- 우리가 구하고자 하는 것은 num 값!

### Smallest Range - 구글 입사문제

- 각 리스트들의 최솟값으로 이루어진 list에서 

  최솟값과 최댓값으로 이루어진 구간설정, 최솟값만들 update (이때, list의 pop 함수 사용)

  all(모두가 True)이면 True / any(하나라도 True)이면 True


### Tic-Tac-Toe Game - 아마존 입사문제

- a = [[1,2,3],[5,5,5],[7,8,9]] 에서 2번째 컬럼을 선택하는 법  [2,5,8]

  1. np.array 에서는 a[:,1] 로 추출가능
  2. 그냥 리스트에서 처리하려면 [k[1] for k in a] 로 해야함!!! 

- a에서 [5,5,5]가 모두 5인지 확인하는 법

  all(x==5 for x in a[1])

### 숫자야구

- list.remove(value) / list.pop(index) 

- for 문에서 remove나 pop 시 주의사항! 

  ex) for i in list:

  ​	list.remove(value)   

   --> remove로 인해서 list 자체가 바뀌므로 for문의 index도 바뀌므로 원하는 결과를 얻을 수 없음

### 프로그래머 사이트 1번 정수제곱근 판별

- root = n ** (1/2)
- 정수인지 확인하는 법
  1. float(n).is_integer()
  2. n % 1 == 0

### 프로그래머 사이트 2번 문자열 다루기 기본

- 문자열의 모든 문자가 숫자인지 확인 : all(i.isnumeric() for i in s)

### 프로그래머 사이트 문제 - 가장 큰 정사각형 찾기

- 특정 index를 시작점으로 하는 K X K matrix 를 뽑는 함수를 생성
- matrix를 sliding 하기 위해 index를 for i=0 ..... for j=0 .... 로 변화 시키는 for문 작성

### 프로그래머 사이트 문제 - 내 기준으로 문자열 정렬하기

- sorted(strings, key=lambda x: x[n번째 문자 기준으로 정렬])

### 프로그래머 사이트 문제 - 행렬 곱 연산하기

1. 결과 dimension 에 해당하는 matrix 초기화 및 생성
2. Column Vector 를 다시 만든다
3. 리스트 간 Element-wise 하게 곱해서 sum하는 함수 생성
4. sum한 결과를 matrix에 대입 

### 프로그래머 사이트 문제 - 핸드폰 번호 가리기

- 문자열은 객체이므로 변경 불가능!! - 새로 string 만들어야 함

### 프로그래머 사이트 문제 - 최대공약수 & 최소 공배수

- 최대 공약수는 작은 수보다 같거나 작은 숫자들 중에서 공통으로 나눠떨어지는 수 중 최댓값
- 최소 공배수는 큰 수의 배수 중에서 작은 수로 나눠떨어지는 수 중 최솟값

### 프로그래머 사이트 문제 - N개의 최소 공배수

- 두 수의 최소 공배수 구하는 함수 이용함!
- step by step 으로 update하며 N개의 최소 공배수 구함

### 프로그래머 사이트 문제 - 가장 긴 팰린드롬

- 연속되는 경우가 문자의 수가 홀수인 경우와 짝수인 경우 나눠서 생각!!
- 인덱스는 하나씩 증가 / 길이는 홀수와 짝수인 경우에 따라 증가율 다름

### 프로그래머 사이트 문제 - 피보나치 수열

1. recursive function 이용하여 풀기
2. 리스트의 마지막 두 원소의 합을 append하는 식으로 처리

### 프로그래머 사이트 문제 - 사전 정렬

- for k, v in dictionary.items(): 키와 값을 불러와서 list에 append 할 것 (k,v) 튜플로
- sorted(list, key=lambda x: x[0] or x[1])  x[0]는 key, x[1]은 value

### 프로그래머 사이트 문제 - 최솟값 만들기

- 두 수의 곱의 합을 최소로 만들기 위해서는, 최댓값은 최솟값과 곱한다!

### 프로그래머 사이트 문제 - 소수 찾기

1. 약수의 갯수 구하는 함수를 정의
2. 그 함수의 return값이 2개이면 그 수는 소수임 (즉 약수의 갯수가 오직 2개인 것이 소수이다)

###  프로그래머 사이트 문제 - 시저 암호

- 밀려주는 n의 값을 0~25로 고정시킬것!! -- 넘으면 나중에 index error

### 프로그래머 사이트 문제 - 멀리뛰기

- N을 1과 2로 조합으로 표현하기(2를 중심으로 생각해서 1을 줄여나감)
- 각 조합별로 factorial 이용하여 경우의 수를 계산

### 프로그래머 사이트 문제 - 다음 큰 숫자

- N을 2진수로 변환했을 때, 1의 갯수가 동일한 수 중 N보다 크고 가장 작은 수
  1. N을 2진수로 변환하여 1의 갯수를 세는 함수 정의
  2. N을 1부터 더해가며 while문을 돌면서 1의 갯수가 동일하면 stop

### 프로그래머 사이트 문제 - 야근지수

- 제곱의 합을 최소화하기 위해서는 각 원소들이 Even해야 함
- 최댓값을 줄여가는 방식으로 해결

### 프로그래머 사이트 문제 - 공항건설

- 특정 도시에 공항이 건설될 때, 인구 X 거리 의 합을 계산한다.
- 그 중 최소가 되는 도시를 구한다.

###  프로그래머 사이트 문제 - 순열구하기

- 주의할 점 : list는 function 후에 원래의 list가 바뀐다 - copy 해서 쓰려면 list[:] 후 사용!!!!
- 재귀 함수 사용
- list 의 insert 와 append 로 N-1 순열에 하나의 원소 더하는 경우로 생각 

### 프로그래머 사이트 문제 - 최고의 집합

- 원소의 곱이 최대가 되려면 각 원소들이 Even해야 함
- 모두 같도록 초기화 한 후 나머지 값을 1씩 더해준다

### 프로그래머 사이트 문제 - 숫자의 표현

- 연속된 N개의 자연수의 합일 때, 연속된 자연수를 아래와 같은 식으로 놓는다.

  N이 홀수 일때 : n-2, n-1, n, n+1, n+2 (N=5일 때, 연속된 자연수의 합은 5n)

  N이 짝수 일때 : n-1, n, n+1, n+2 (N=4일 때, 연속된 자연수의 합은 4n+2)



# Codility

1. 2진수에서는 0아니면 1이므로 숫자를 세는 것은 나머지 숫자를 뺀 나머지의 갯수(index 이용)

2. 순환되는 list에서 index 조심할 것!! - 나머지 이용해서 index는 항상 0~length-1로 고정시킬 것!!

3. set으로 부터 key를 받고 0 으로 value 초기화 된 dictionary 생성하기

   dict.fromkeys(set(A),0) / dict[value]=key 넣으면 추가 됨

