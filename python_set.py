fruits = {'apple', 'banana', 'orange'}
print(fruits)
fruits.add('mango')
print(fruits)

companies = set()
companies = {'apple', 'microsoft', 'google'}
print(type(fruits))
print(type(companies))

## 교집합
fruits & companies

## 합집합
fruits | companies

# 여러 세트를 리스트에 담은 뒤 set의 메서드를 쓸 수도 있다
list_of_sets = [fruits, companies]
print(set.intersection(*list_of_sets))  # 교집합
print(set.union(*list_of_sets))         # 합집합

## set은 중복 원소를 갖지 않음
## 또 순서가 유지되지 않는다.
alphabet = list('google')
print(alphabet)
print(set(alphabet))

## 집합끼리 뺄셈도 가능
S1 = {1, 2, 3, 4, 5, 6, 7, 8}
S2 = {3, 6, 9}
print(S1 - S2)