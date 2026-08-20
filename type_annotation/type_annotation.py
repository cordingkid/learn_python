## 파이썬 타입 어노테이션
# 파이썬은 동적 언어의 단점을 극복하기 위해 3.5버전부터 타입 어노테이션 기능을 지원하기 시작
# 다만 정적 언어처럼 강제로 타입을 체크하지 않고, 타입 어노태이션 즉 타입에 대한 힌트를 제공하는 정도의 기능만 지원
# 이는 동적 언어의 장점을 잃지 않으면서 기존 코드와의 호환성을 유지하려는 선택이다.


# 변수에 타입 지정하기
num: int = 1
name: str = "홍길동"
numbers: list = [1, 2, 3]


# 함수에 타입 지정하기
def add(a: int, b: int) -> int:
    return a + b

def greet(name: str) -> str:
    return f"Hi, {name}!"

def get_user_info(user_id: int) -> dict:
    return {"id": user_id, "name": "홍길동"}

# 함수의 매개변수에도 같은 규칙을 적용하여 타입을 명시할 수 있다.
# -> int 처럼 화살표 기호를 사용해 함수의 반환값 타입도 명시할 수 있다.
# 이렇게 하면 함수를 사용하는 사람이 어떤 타입의 인수를 넘겨야 하고,
# 어떤 타입의 값을 반환하는지 쉽게 알 수 있다.
# 기본 어노테이션 타입으로 정수는 int, 문자열은 str, 리스트는 list, 튜플은 tuple, 딕셔너리는 dict, 집합은 set, 불은 bool을 사용한다.

numbers: list[int] = [1, 2, 3]                  # int를 담는 리스트
user_info: dict[str, int] = {"age": 30}         # 키는 str, 값은 int인 딕셔너리
coordinates: tuple[float, float] = (3.5, 7.2)  # float 2개를 담는 튜플
# list[int]처럼 대괄호 안에 타입을 넣는 문법은 파이썬 3.9 이상에서 사용할 수 있다.


# typing 모듈이 여전히 필요한 경우
from typing import Optional, Union

# 1. Optional - None이 가능한 경우
user_name: Optional[str] = None         # str 또는 None
# 2. Union - 여러 타입이 가능한 경우
user_id: Union[int, str] = "jenny"      # 정수 또는 문자열


# typing 모듈의 고급 타입
"""
typing 모듈에는 Optional과 Union 외에도 다양한 타입이 있다.

from typing import Callable, Any

# Callable - 함수 타입 지정
def process_data(callback: Callable[[int], str]) -> str:
    return callback(42)

# Any - 모든 타입 허용
unknown_data: Any = {"key": "value"}
Callable[[int], str]은 int를 인수로 받아 str을 반환하는 함수를 의미한다. Any는 어떤 타입이든 허용한다는 의미이다.
"""


# 실무에서의 권장사항
# 파이썬 3.9 이상을 사용한다면
from typing import Optional, Union  # 필요한 것만 가져오기

# 기본 타입은 내장 타입 사용
scores: list[int] = [95, 87, 92]
user_data: dict[str, str] = {"name": "홍길동"}

# 특별한 경우에만 typing 모듈 사용
def find_user(user_id: int) -> Optional[dict[str, str]]:
    # 사용자를 찾으면 딕셔너리 반환, 없으면 None 반환
    if user_id > 0:
        return {"name": "홍길동", "email": "hong@example.com"}
    return None
