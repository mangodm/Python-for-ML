## 1. Vector 계산
# vector: 대부분 list로 표현

# 1) vector의 합

## DON'T
u = [2, 2]
v = [2, 3]
z = [3, 5]
result = []
for i in range(len(u)):
    result.append(u[i] + v[i] + z[i])
print(result)

## DO
result = [sum(t) for t in zip(u, v, z)]
print(result)

# 2) scalar-vector product
u = [1, 2, 3]
v = [4, 5, 6]
alpha = 2
result = [alpha*sum(t) for t in zip(u, v)]
print(result)

## 2. Matrix 계산
# 1) Matrix addition
matrix_a = [[3, 6], [4, 5]]
matrix_b = [[5, 8], [6, 7]]
result = [[sum(row) for row in zip(*t)] for t in zip(matrix_a, matrix_b)]
print(result)

# 2) scalar-matrix product
alpha = 4
result = [[alpha * element for element in t] for t in matrix_a]
print(result)

# 3) Matrix transpose
matrix_a = [[1, 2, 3], [4, 5, 6]]
result = [[element for element in t] for t in zip(*matrix_a)]
print(result)

# 4) Matrix Product
matrix_a = [[1, 1, 2], [2, 1, 1]]
matrix_b = [[1, 1], [2, 1], [1, 3]]
result = [[sum(a * b for a, b in zip(row_a, column_b))
          for column_b in zip(*matrix_b)] for row_a in matrix_a]
print(result)