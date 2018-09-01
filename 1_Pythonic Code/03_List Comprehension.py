## List Comprehension

# 1. 0부터 9까지의 숫자를 원소로 갖는 리스트 생성
# for loop + append 사용
result = []
for i in range(10):
    result.append(i)

print(result)

# list comprehension 사용
result = [i for i in range(10)]
print(result)

# 2. 0부터 9까지의 숫자 중 2로 떨어지는 숫자
# list comprehension 사용
result = [i for i in range(10) if i % 2 == 0]
print(result)

# 3. 두 단어의 각 요소를 합쳐 원소로 하는 리스트 생성
# Nested for loop
word_1 = 'Hello'
word_2 = 'World'
result = [i+j for i in word_1 for j in word_2]
print(result)

# 4. list의 각 원소를 합쳐 요소로 하는 list 생성
# Nested for loop
case_1 = ['A', 'B', 'C']
case_2 = ['D', 'E', 'A']
result = [i+j for i in case_1 for j in case_2]
print(result)

# 5. list의 각 원소를 합쳐 요소로 하는 list 생성(두 원소가 같은 경우 제외)
result = [i+j for i in case_1 for j in case_2 if not (i == j)]
print(result)
# 리스트 요소를 알파벳 순으로 정렬
result.sort()
print(result)

# 6. 문장의 각 단어를 요소로 구분하여 list 생성
# split + list comprehension
words = 'The quick brown fox jumps over the lazy dog'.split()
print(words)

# 대문자, 소문자, 글자수를 요소로 하는 list 생성
stuff = [[w.upper(), w.lower(), len(w)] for w in words]

# list의 요소를 순서대로 출력
for i in stuff:
    print(i)