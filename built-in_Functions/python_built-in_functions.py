"""
## abs(x)
숫자의 절대값을 반환하는 함수
ex)
>>> abs(3)
3
>>> abs(-3)
3
>>> abs(-1.2)
1.2


## all(x)
all(x)는 반복 가능한 데이터 x를 입력값으로 받아 x의 요소가 모두 참이면 True,
거짓이 하나라도 있으면 False를 반환
반복 가능한 데이터란 for 문에서 사용할 수 있는 자료형을 의미한다.
리스트, 튜플, 문자열, 딕셔너리, 집합 등이 있다.
ex)
>>> all([1, 2, 3])
True

>>> all([1, 2, 3, 0])
False

>>> all([])
True
빈 값인 경우에는 True를 반환


## any(x)
any(x)는 반복 가능한 데이터 x를 입력으로 받아 x의 요소 중 
하나라도 참이 있으면 True를 반환하고, x가 모두 거짓일 때만 False를 반환한다. 
즉, all(x)의 반대로 작동한다.
ex)
>>> any([1, 2, 3, 0])
True

>>> any([0, ""])
False


## chr(x)
chr(i)는 유니코드 숫자 값을 입력받아 그 코드에 해당하는 문자를 반환하는 함수이다.
ex)
>>> chr(97)
'a'
>>> chr(44032)
'가'


## dir(x)
dir은 객체가 지닌 변수나 함수를 보여 주는 함수이다. 
다음 예는 리스트와 딕셔너리가 지닌 함수(메서드)를 보여 준다.
ex)
>>> dir([1, 2, 3])
['append', 'count', 'extend', 'index', 'insert', 'pop',...]
>>> dir({'1':'a'})
['clear', 'copy', 'get', 'items', 'keys', 'values', ...]


## divmod(a, b)
divmod(a, b)는 2개의 숫자 a, b를 입력으로 받아 a를 b로 나눈 몫과 나머지를 튜플로 반환한다.
ex)
>>> divmod(7, 3)
(2, 1) # (몫, 나머지)


## enumerate(x)
enumerate는 '열거하다'라는 뜻이다. 
이 함수는 순서가 있는 데이터(리스트, 튜플, 문자열)를 
입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 반환한다.

보통 enumerate 함수는 for 문과 함께 사용한다.
ex)
>>> for i, name in enumerate(['body', 'foo', 'bar']):
...     print(i, name)
...
0 body
1 foo
2 bar
인덱스 값과 함께 body, foo, bar가 순서대로 출력되었다. 
즉, enumerate를 for 문과 함께 사용하면 자료형의 현재 순서(index)와 그 값을 쉽게 알 수 있다.

for 문처럼 반복되는 구간에서 객체가 현재 어느 위치에 있는지 
알려 주는 인덱스 값이 필요할 때 enumerate 함수를 사용하면 매우 유용하다.
"""