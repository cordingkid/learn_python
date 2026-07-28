"""
파이썬 메서드의 첫 번째 매개변수 이름은 관례적으로 self를 사용한다. 
객체의 메서드를 호출할 때 호출한 객체 자신이 전달되기 때문에 self라는 이름을 사용한 것이다. 
물론 self 말고 다른 이름을 사용해도 상관없다.
"""
class FourCal:
    ## 생성자
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setData(self, first, second):
        self.first = first
        self.second = second

    # 더하기 함수
    def add(self):
        return self.first + self.second
    def mul(self):
        return self.first * self.second
    def sub(self):
        return self.first - self.second
    def div(self):
        return self.first / self.second

## a = FourCal() 생성자 때문에 에러 남
a = FourCal(4, 2)
a.setData(4, 2)
print(a.first)
print(a.second)
print(a.add())


## 클래스 상속
class MoreFourCal(FourCal):
    def pow(self):
        return self.first ** self.second

b = MoreFourCal(5, 10)
print(b.add())
print(b.mul())
print(b.sub())
print(b.div())
print(b.pow())


## 매서드 오버라이딩
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

c = SafeFourCal(4, 0)
print(c.div())


## 클래스 변수
class Family:
    lastname = "김"

f = Family()
print(f.lastname)

# f 객체에 변수가 새롭게 생성됨
f.lastname = "최"
print(f.lastname)