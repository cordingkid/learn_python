## 예외 만들기
class MyError(Exception):
    # 오류메세지 출력 하기 print(e)
    def __str__(self):
        return "허용되지 않는 별명입니다."


# 예외 발생
def say_nick(nick):
    if nick == "바보":
        raise MyError()
    print(nick)

try:    
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)