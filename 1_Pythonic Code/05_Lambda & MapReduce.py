## Lambda & MapReduce

# general function
def f(x, y):
    return x+y

print(f(1, 4))

# lambda function
f = lambda x, y: x+y
print(f(1, 4))

# map function: seq 자료형 각 element에 동일한 function 적용
ex = [1, 2, 3, 4, 5]
f = lambda x:x ** 2
print(list(map(f, ex)))

# 두 개 이상의 list에도 적용 가능함.
f = lambda x, y: x + y
print(list(map(f, ex, ex)))
