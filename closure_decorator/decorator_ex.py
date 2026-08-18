## 데코레이터
"""
데코레이터는 클로저를 활용하여 기존 함수를 수정하지 않고 기능을 덧붙이는 기법
"""
"""
import time
def elapsed(original_func):         # 기존 함수를 인수로 받는다.
    def wrapper():
        start = time.time()
        result = original_func()    # 기존 함수를 수행
        end = time.time()
        print("함수 수행시간: %f 초" % (end - start)) # 기존 함수의 수행시간 출력
        return result
    return wrapper

def myfunc():
    print("함수가 실행됩니다.")

decorated_myfunc = elapsed(myfunc)
decorated_myfunc()
"""
"""
elapsed 함수로 클로저를 만들었다. 
이 함수는 함수를 인수로 받는다. 
파이썬은 함수도 객체이므로 함수 자체를 인수로 전달할 수 있다.

이제 decorated_myfunc = elapsed(myfunc)로 생성한 decorated_myfunc를 decorated_myfunc()로 
실행하면 실제로는 elapsed 함수 내부의 wrapper 함수가 실행되고, 
이 함수는 전달받은 myfunc 함수를 실행하면서 실행 시간을 함께 출력한다.
"""


"""
클로저를 이용하면 기존 함수에 기능을 덧붙이기가 매우 편리하다.
이렇게 기존 함수를 바꾸지 않고 기능을 추가할 수 있게 만드는 elapsed 함수와 같은 클로저를 데코레이터라고 한다.

파이썬 데코레이터는 다음처럼 @ 문자를 이용해 함수 위에 적용하여 사용할 수도 있다.
"""
import time 
def elapsed(original_func):         # 기존 함수를 인수로 받는다.
    def wrapper(*args, **kwargs):   # *args, **kwargs 매개변수 추가
        start = time.time()
        result = original_func(*args, **kwargs)    # 전달받은 *args, **kwargs를 입력하라미터로 기존함수 수행
        end = time.time()
        print("함수 수행시간: %f 초" % (end - start)) # 기존 함수의 수행시간 출력
        return result
    return wrapper

@elapsed
def myfunc(message):
    print("'%s'을 출력합니다." % message)

myfunc("You need python")
"""
myfunc 함수 바로 위에 @elapsed라는 데코레이터를 추가했다. 
파이썬은 함수 위에 @함수명이 있으면 데코레이터 함수로 인식한다. 
따라서 이제 myfunc 함수는 elapsed 데코레이터를 통해 수행될 것이다.
"""

"""
myfunc 함수는 입력 인수가 필요하지만, elapsed 함수 안의 wrapper 함수는 전달받은 myfunc 함수를 입력 인수 없이 호출해 오류가 발생한 것이다. 
그러므로 데코레이터 함수는 기존 함수의 입력 인수에 상관없이 동작하도록 만들어야 한다. 
데코레이터는 기존 함수가 어떤 입력 인수를 취할지 알 수 없기 때문이다. 
이렇게 전달받아야 하는 기존 함수의 입력 인수를 알 수 없는 경우에는 *args와 **kwargs 매개변수를 이용하면 된다. 
*args는 입력 인수의 개수에 상관없이 모든 입력을 받을 수 있고, 
**kwargs는 키=값 형태의 모든 입력을 받을 수 있는 매개변수이다.
"""


"""
*args와 **kwargs

*args는 모든 입력 인수를 튜플로 변환하는 매개변수, 
**kwargs는 모든 '키=값' 형태의 입력 인수를 딕셔너리로 변환하는 매개변수이다. 
다음과 같은 형태의 호출을 살펴보자.

>>> func(1, 2, 3, name='foo', age=3)
func 함수가 입력 인수의 개수와 형태에 상관없이 모든 입력을 처리하려면 어떻게 해야 할까?

>>> def func(*args, **kwargs):
...     print(args)
...     print(kwargs)
... 
>>> func(1, 2, 3, name='foo', age=3)
(1, 2, 3)
{'age': 3, 'name': 'foo'}
이처럼 func 함수에 *args, **kwargs라는 매개변수를 지정하면 다양한 입력 인수를 모두 처리할 수 있다. 
이렇게 하면 1, 2, 3 같은 일반 입력은 args 튜플, name = 'foo'와 같은 '키=값' 형태의 입력은 kwargs 딕셔너리로 저장한다.
"""