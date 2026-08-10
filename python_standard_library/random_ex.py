import random

## random
# random은 난수를 발생시키는 모듈이다.

# 0.0에서 1.0 사이의 실수 중에서 난수 값을 반환하는 코드
print(random.random())

# 특정 수 사이의 정수 중 난수 값을 반환하는 코드
print(random.randint(1, 100)) # 1에서 100 사이의 정수 난수를 반환


# 랜덤 모듈로 함수 만들어보기
def random_pop(data):
    number = random.randint(0, len(data) - 1)
    return data.pop(number)


# random.choice함수를 사용하여 직관적으로 만들수 있음
def random_pop2(data):
    number = random.choice(data)
    data.remove(number)
    return number


# 리스트의 항목을 무작위로 섞고 싶을 때는 random,sample 함수를 사용하면됨
data = [1, 2, 3, 4, 5]
print(random.sample(data, len(data)))

