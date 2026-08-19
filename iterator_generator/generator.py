## 제너레이터
"""
제너레이터는 이터레이터를 쉽게 만들어 주는 함수

이터레이터를 클래스로 만들려면 __iter__와 __next__ 메서드를 구현해야 한다.
하지만 제너레이터를 사용하면 함수 하나로 간단하게 이터레이터를 만들 수 있다.

제너레이터의 핵심 특징

일반 함수와 비슷하지만 return 대신 yield 키워드를 사용한다.
yield를 만나면 값을 반환하고 함수 실행을 일시 정지한다.
다시 호출하면 일시 정지했던 지점부터 계속 실행한다.
마치 음악 플레이어의 재생/일시 정지 기능처럼 동작한다.
"""
def mygen():
    for i in range(1, 1000):
        result = i * i
        yield result

gen = mygen()

print(next(gen))
print(next(gen))
print(next(gen))

# 더 간단하게 제너레이터 만들기
simple_gen = (i * i for i in range(1, 1000))
print(next(simple_gen))
print(next(simple_gen))
print(next(simple_gen))

# 이 표현식은 리스트 컴프리헨션 구문과 비슷하지만,
# 대괄호 [] 대신 소괄호 () 를 사용한다.
# 이를 '제너레이터 표현식'이라고 함
# 소괄호를 사용하지만 튜플을 만드는 것이 아니라 제너레이터 객체를 만든다는 점에 주의