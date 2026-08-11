## opertator.itemgetter
"""
operator.itemgetter는 주로 sorted와 같은 함수의 key 매개변수에 적용하여 다양한 기준으로 정렬할 수 있도록 도와주는 모듈이다.

예를 들어 학생의 이름, 나이, 성적 등의 정보를 저장한 다음과 같은 students 리스트가 있다고 가정해 보자.

students = [
    ("jane", 22, 'A'),
    ("dave", 32, 'B'),
    ("sally", 17, 'B'),
]
students 리스트에는 3개의 튜플이 있으며 각 튜플은 순서대로 이름, 나이, 성적에 해당하는 데이터로 이루어졌다. 이 리스트를 나이순으로 정렬하려면 어떻게 해야 할까?
"""
from operator import itemgetter
students = [
    ("jane", 22, 'A'),
    ("dave", 32, 'B'),
    ("sally", 17, 'B'),
]
result = sorted(students, key=itemgetter(1))
print(result)

# 이번엔 딕셔너리 일때 정렬하는 방법
students = [
    {"name": "jane", "age": 22, "grade": 'A'},
    {"name": "dave", "age": 32, "grade": 'B'},
    {"name": "sally", "age": 17, "grade": 'B'},
]
result = sorted(students, key=itemgetter('age'))
print(result)

"""
operator.attrgetter()

students 리스트의 요소가 튜플이 아닌 Student 클래스의 객체라면 다음처럼 attrgetter()를 적용하여 정렬해야 한다.

# attrgetter1.py
from operator import attrgetter

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

students = [
    Student('jane', 22, 'A'),
    Student('dave', 32, 'B'),
    Student('sally', 17, 'B'),
]

result = sorted(students, key=attrgetter('age'))
attrgetter('age')는 Student 객체의 age 속성으로 정렬하겠다는 의미이다. attrgetter('grade')와 같이 사용하면 성적순으로 정렬한다.
"""