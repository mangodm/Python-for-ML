## Pythonic coding의 효율성

# 일반적인 코드
colors = ['a', 'b', 'c', 'd', 'e']
result = ''

for s in colors:
    result += s

print(result)

# Pythonic 코드
result = ''.join(colors)
print(result)