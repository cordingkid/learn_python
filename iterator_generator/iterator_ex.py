## 이터레이터
"""
이터레이터는 next() 함수로 값을 하나씩 꺼낼 수 있는 객체다.
모든 값을 꺼내면 StopIteration예외가 발생

>>> a = [1, 2, 3]
>>> ia = iter(a)
>>> type(ia)
<class 'list_iterator'>

이터레이터 next함수로 호출해보기
>>> next(ia)
1
>>> next(ia)
2
>>> next(ia)
3
>>> next(ia)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
"""

## 이터레이터 만들기
"""
이터레이터 클래스의 필수 매서드
1. __iter__ : 이터레이터 객체 자신을 반환한다.
2. __next__ : 다음 값을 반환하고, 더 이상 값이 없으면 StopIteration 예외를 발생
"""
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.position = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.position >= len(self.data):
            raise StopIteration
        result = self.data[self.position]
        self.position += 1
        return result

if __name__ == "__main__":
    i = MyIterator([1,2,3])
    for item in i:
        print(item)
"""
동작 원리
1. __init__ 메서드: 이터레이터를 초기화한다.

self.data: 반복할 데이터를 저장한다.
self.position: 현재 위치를 추적하는 변수이다(0부터 시작).
2. __iter__ 메서드: 이터레이터 객체 자신을 반환한다.

이 메서드가 있어야 파이썬이 해당 객체를 반복 가능한 객체로 인식한다.
for 문, iter() 함수, next() 함수 등에서 사용하려면 반드시 구현해야 한다.
보통 return self로 자기 자신을 반환한다.
3. __next__ 메서드: 다음 값을 반환한다.

self.position을 이용해 현재 위치의 값을 가져온다.
위치를 하나씩 증가시킨다.
더 이상 값이 없으면 StopIteration 예외를 발생시킨다.
"""