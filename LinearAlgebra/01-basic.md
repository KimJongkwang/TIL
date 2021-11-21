# 선형대수(Linear Algebra) 기초

> [인공지능을 위한 선형대수, 주재걸 교수님](https://www.boostcourse.org/ai251) 강의를 보고 작성한 내용입니다.

## Scalar, Vector, and Matrix
- Scalar(스칼라) : 단일 값(수치), 방향이 없는 크기의 물리량
- Vector(벡터) : an ordered list of numbers(array), 단, 첫번째, 두번째 위치가 있는 배열(ordered array) * unordered array : set
- Matrix(행렬) : a two-dimensional array of numbers, 2차원의 행렬
    - Matrix size : 3 X 2 는 3행 2열
    - Row vector : a horizontal vector 행렬의 각각의 행
    - Column vector : a vertical vector 행렬의 각각의 열
        - Column is Vertical vector * column: 기둥
            * 일반적으로 컬럼벡터가 default(선형대수학내 약속)
        - column vector = x = n X 1
        - row vector = x<sup>_T_</sup> = 1 X n
    
### 행렬 표기법(Matrix Notations)
- Square Matrix
    - 정사각형의 행렬
    - 가로, 세로의 길이가 같은 행렬
    - 2 x 2, 4 x 4 행렬
- Rectangular Matrix
    - 직사각형 행렬
    - 3 x 2 행렬
- Transpose of Matrix
    - 전치행렬
    - 행과, 열을 교환 

- A<sub>ij</sub> : 행렬 A의 i행j열 값((i, j)-th component of A)
- A<sub>i,</sub> : i행 전체(i-th row vector of A)
- A<sub>,j</sub> : j열 전체(j-th column vector of A)

### 벡터, 행렬 사칙연산(Vector/Matrix Additions and Multiplications)
- C = A + B : Element-wise addition, i.e., C<sub>ij</sub> = A<sub>ij</sub> + B<sub>ij</sub>
    - 두 행렬의 요소들을 모두 더한다.
    - 두 행렬의 크기는 같아야한다.
    - 뺄셈(subtraction)도 마찬가지
- Scalar multiple of vector/matrix
    - 벡터 또는 행렬의 상수 곱셈
        - 모든 요소들에 덧셈, 또는 곱셈

- Matrix-Matrix multiplication
    - 매트릭스간의 곱셈(내적)
        - 행렬간 크기 제약
        - x, y 행렬의 내적에서 x의 열과 y의 행 크기는 같아야 곱셈이 성립
        - x<sub>i,j</sub>, y<sub>j,i</sub>간 곱의 합 행렬
        - 행렬간 곱의 결과는 가운데 열, 행이 소거된 나머지 행, 열의 크기를 가짐
            - (3 X 2)(2 X 2) = 3 X 2, (1 X 3)(3 X 1) = 1 X 1
    - Matrix multiplication is NOT commutative(매트릭스 곱셈은 교환법칙이 성립되지 않는다!)
        - AB != BA, 행렬간의 크기가 내적을 할 수 있더라도, 교환할 시 row vector와 column vector 계산의 순서가 바뀌기 때문에 결과도 일반적으로 달라진다.

- Other Properties
    - A(B + C) = AB + AC : Distributive 분배법칙
    - A(BC) = (AB)C : Associative 결합법칙
    - (AB)<sup>_T_</sup> = B<sup>_T_</sup>A<sup>_T_</sup> : Property of transpose
        - 전치의 특성 : 두 행렬의 곱을 전치할 경우, A, B의 각 전치행렬을 곱한 것 과 같다.
    - (AB)<sup>_-1_</sup> = B<sup>_-1_</sup>A<sup>_-1_</sup> : 역행렬도 마찬가지