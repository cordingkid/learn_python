"""
try:
    a = [1, 2]
    print(a[3])
    4 / 0
except ZeroDivisionError as e:
    print("0으로 나눌 수 없음")
except IndexError as e:
    print("인덱싱 할 수 없습니다.")
"""

# 위에 코드를 아래처럼도 가능
try:
    a = [1, 2]
    print(a[3])
    4 / 0
except (ZeroDivisionError, IndexError) as e:
    print(e)