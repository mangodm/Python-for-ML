## Pythonic code 예시

# Split 함수(String 값을 나눠서 List 형태로 변환) 활용
items = 'zero one two three'.split() # 공백을 기준으로 문자열 나누기
print(items)

example = 'python, jquery, javascript' # ','을 기준으로 문자열 나누기
example.split(',')

a, b, c = example.split(',') # 리스트에 있는 각 값을 a, b, c 변수로 unpacking

example = 'cs50.gacheon.edu'
subdomain, domain, tld = example.split('.') # '.'을 기준으로 문자열 나누고 unpacking

# join 함수(string list를 합쳐 하나의 string으로 반환) 활용
colors = ['red', 'blue', 'green', 'yellow']
result = ''.join(colors)
print(result)

result = ' '.join(colors) # 연결 시 빈칸으로 연결
print(result)

result = ', '.join(colors) # 연결 시 ', '으로 연결
print(result)

result = '-'.join(colors) # 연결 시 '-'으로 연결
print(result)