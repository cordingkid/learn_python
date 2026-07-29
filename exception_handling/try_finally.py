# finally 절 실행 순서
try:
    print("나누기 전")
    4 / 0
    print("나누기 후")
except ZeroDivisionError:
    print("오류 발생")
finally:
    print("finally 실행")
