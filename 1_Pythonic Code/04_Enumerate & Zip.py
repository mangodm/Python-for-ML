## Enumerate & Zip

# 1. 리스트의 각 요소를 병렬적으로 추출
# zip
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']

for a, b in zip(alist, blist):
    print(a, b)

a, b, c = zip((1, 2, 3), (10, 20, 30), (100, 200, 300))
# 2. 각 tuple의 같은 index끼리 묶음
print(a, b, c)

# 3. 각 tuple의 index를 묶어 합을 list로 변환
print([sum(x) for x in zip((1, 2, 3), (10, 20, 30), (100, 200, 300))])

# 4. 리스트의 요소를 추출할 때 번호를 붙여 추출
# enumerate + zip
for i, (a, b) in enumerate(zip(alist, blist)):
    print(i, a, b)