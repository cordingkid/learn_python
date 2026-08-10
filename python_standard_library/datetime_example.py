import datetime
day1 = datetime.date(2022, 12, 14)
day2 = datetime.date(2026, 4, 5)
print(day1)
print(day2)

diff = day2 - day1
# day2에서 day1을 빼면 datetime 모듈의 timedelta 객체가 반환된다
print(diff.days)

# 0은 월요일을 의미 순서대로 1 화 ... 6은 일요일을 뜻함
print(day2.weekday())

# 월요일을 1부터 반환하게 하려면 아래 함수 사용하면됨
print(day2.isoweekday())