"""
itertools.zip_longest(*iterables, fillvalue=None) 함수는 같은 개수의 
자료형을 묶는 파이썬 내장 함수인 zip 함수와 똑같이 동작한다. 
하지만 itertools.zip_longest() 함수는 전달한 반복 가능 객체(*iterables)의 길이가 
서로 다르면 긴 객체의 길이에 맞춰 fillvalue에 설정한 값을 짧은 객체에 채울 수 있다.
"""
import itertools

students = ['한민서', '황지민', '이영철', '이광수', '김승민']
snacks = ['사탕', '초콜릿', '젤리']

result = zip(students, snacks)
print(list(result))


## itertools.zip_longest
"""
students의 요소 개수가 snacks보다 많을 때 그만큼을 '새우깡'으로 채우려면 어떻게 해야 할까? 
이럴 때 요소 개수가 많은 것을 기준으로 자료형을 묶는 itertools.zip_longest()를 사용하면 된다. 
부족한 항목은 None으로 채우는데, 다음처럼 fillvalue로 값을 지정하면 None 대신 다른 값으로 채울 수 있다.
"""
result = itertools.zip_longest(students, snacks, fillvalue="새우깡")
print(list(result))

## itertools.permutations
# itertools.permutations(iterable, r)은 반복 가능 객체중에서
# r개를 선택한 순열을 이터레이터로 반환하는 함수다.

# 1,2,3 이라는 숫자가 적힌 3장의 카드에서 2장의 카드를 꺼내 만들 수 있는 2자리 숫자 구하기
# [순열]
print(list(itertools.permutations(['1', '2', '3'], 2)))

# 3장의 카드에서 순서에 상관없이 2장을 고르는 조합
# 조합
print(list(itertools.combinations(['1', '2', '3'], 2)))

# 조합2 45개의 숫자 중 6개를 선택하는 경우의 수 구하기
it = itertools.combinations(range(1, 46), 6)
print (len(list(it)))


# 중복 조합을 사용하는 함수
# 로또 복권이 숫자 중복을 허용하도록 규칙이 변경되면?
# 같은 숫자를 허용하는 중복 조합은 itertools.combinations_with_replacement()를 사용하면 된다.
result = itertools.combinations_with_replacement(range(1, 46), 6)
print(len(list(result)))