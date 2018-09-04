## Asterisk

# 1) 곱셈
print(3 * 8)

# 2) 제곱
print(3 ** 4)

# 3) *: 한 번에 여러 개의 변수를 넘겨줄 때 사용
def asterisk_test(a, *args):
    print(a, args)
    print(type(args))

asterisk_test(1, 2, 3, 4, 5, 6) # tuple로 반환
asterisk_test(1, (2, 3, 4, 5, 6)) # 괄호는 하나의 인자로 반환

def asterisk_test(a, *args):
    print(a, args[0])
    print(type(args))
asterisk_test(1, (2, 3, 4, 5, 6)) # tuple 안의 tuple


# 4) **: 키워드 전달인자를 넘겨줄 때 사용
def asterisk_test(a, **kargs):
    print(a, kargs)
    print(type(kargs))

asterisk_test(1, b= 2, c = 3, d = 4) # dict로 반환

# 5) unpacking a container
def asterisk_test(a, args):
    print(a, *args)
    print(type(args))
asterisk_test(1, (2, 3, 4, 5, 6)) # 변수 unpacking

a, b, c = ([1, 2], [3, 4], [5, 6])
print(a, b, c)

data = ([1, 2], [3, 4], [5, 6])
print(*data)

for data in zip(*([1, 2], [3, 4], [5, 6])):
    print(sum(data))

def asterisk_test(a, b, c, d, e = 0):
    print(a, b, c, d, e)

data = {'d':1, 'c':2, 'b':3, 'e':56}
asterisk_test(10, **data) ## dict type의 요소를 풀어서 넣어줌