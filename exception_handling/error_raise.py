## 오류 발생시키기
class Bird:
    def fly(self):
        raise NotImplementedError # 자바랑 다르게 raise로 에러 빌생시킴

class Eagle(Bird):
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly() # 메서드 오버라이딩으로 인해 오류 발생안함