# 선형방정식(Linear Equation)과 선형시스템(Linear System)

> [인공지능을 위한 선형대수, 주재걸 교수님](https://www.boostcourse.org/ai251) 강의를 보고 작성한 내용입니다.
> _영문과 친숙해지기 위해 영문명을 함께 적습니다.._

##### 선형방정식(Linear Equation)

선형방정식은 흔히 수학에서 1차방정식과 같은 방정식

- 선형방정식의 값(상수)은 흔히 coefficients
- 1차방정식을 선형방정식에서, **a**<sup>_T_</sup>**x** = _b_ 로 표현
  - a계수들의 raw vector를 전치(transpose)하여 x변수로 이루어진 column vector와 내적

##### 선형시스템(Linear System: set of equations)

선형시스템은 선형방정식들의 집합으로 연립방정식을 나타낸다.(A system of linear equations, or a linear system)

## 선형시스템(Linear System Example)

선형시스템은 연립방정식 문제를 푸는 것과 유사하다.

##### 예시, 몸무게, 키, 흡연유무를 변수로 하는 수명 추정

![image](https://user-images.githubusercontent.com/74632423/143727181-e1ee4054-8fd6-422b-903a-e3522c38368e.png)

> 사진출처: [인공지능을 위한 선형대수, 주재걸 교수님](https://www.boostcourse.org/ai251/lecture/540312?isDesc=false)

선형시스템에서 위의 문제를 방정식으로 풀어놓는다면, 아래와 같이 표현할 수 있다.

1. 각 변수의 계수 matrix

- A = [[60, 5.5, 1], [65, 5.0, 0], [55, 6.0, 1]]

2. 변수 vector(x), 값 vector(b)

- x = [x1, x2, x3], b = [66, 74, 78]

3. A x 내적곱

이 문제를 풀기 위한 여러 선형대수 테크닉이 존재한다.

### 역행렬(Inverse Matrix)을 활용하는 방법

#### Identity Matrix(항등행렬)

역행렬을 이해하기 위해서는 항등행렬을 먼저 이해해야한다.
항등행렬은 **square matrix(정사각행렬)**며, **diagonal entries(대각성분)이 모두 1**이다.

- 또한, 어떠한 vector와 곱하더라도 자기자신을 만들어낸다.

#### 역행렬(Inverse Matrix)

역행렬을 이야기할때는 square matrix(정사각행렬)이며, 행렬과 역행렬의 곱은 항등행렬을 전제로 한다.

- _A_<sup>-1</sup>_A_ = _AA_<sup>-1</sup> = _I_<sub>n</sub>.

역행렬을 통해 위의 문제를 풀어본다면, 항등행렬의 성질을 이용하여 아래와 같이 풀 수 있다.
![image](https://user-images.githubusercontent.com/74632423/143727696-edacde09-0953-4f45-82e2-a78e09ca47bc.png)

### 역행렬이 존재하지 않는 경우

역행렬이 존재한다면, 위의 같은 방법으로 해결하면 된다.
역행렬이 존재하는 것에 대한 판단은 det(determinant) _A_ 행렬식 _A_ 이 0이면 역행렬이 존재하지 않는다.

역행렬이 존재하지 않는 경우의 해(x)는 전혀 없거나, 무수히 많게되는 특성이 있다.

- 무수히 많은 경우는 변수를 소거함에 있어 하나의 변수를 소거할 때, 다른 변수들도 모두 소거가 된다.
- 이런 경우 직선안에 무수히 많은 해가 존재하게 된다.
  - ex)1x + 2y = 3, 2x + 4y = 6
- 반대로 중복된 방정식에서 상수가 다른 경우에 해가 없게 된다.
  - ex)1x + 2y = 3, 2x + 4y = 4

### 직사각행렬(rectangular matrix)

변수의 개수를 n, 데이터의 개수를 m이라 볼 때, 직사각행렬은 n != m 인 꼴이다.

- 이때 m < n의 경우는 일반적으로 해가 무수히 많이 존재한다.(under-determined system)
  - Regularization 등의 방법
- 반대로 m > n의 경우는 해가 없게 된다.(over-determined system)
  - least square method(최소자승법) 등

위의 최적해를 찾고자 하는 노력을 위해 머신러닝, 딥러닝 기법이 있다.
