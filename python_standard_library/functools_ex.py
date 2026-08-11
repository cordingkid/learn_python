## functools.reduce
# functools.reduce(function, iterable)은 함수 (function)를 반복 가능한 객체의
# 요소에 차례대로 (왼쪽에서 오른쪽으로) 누적 적용하여 이 객체를 하나의 값으로 줄이는 함수다.

def add(data):
    result = 0
    for i in data:
        result += i
    return result
data = [1, 2, 3, 4, 5]
result = add(data)
print(result)

# 위의 함수를 functools.reduce()를 사용하여 코드 수정
import functools

reuslt = functools.reduce(lambda x, y: x + y, data)
print(result)

# 최댓값 구하기
num_list = [3, 2, 8, 1, 6, 7]
max_num = functools.reduce(lambda x, y: x if x > y else y, num_list)
print(max_num)