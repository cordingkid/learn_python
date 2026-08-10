import time
"""
time.time()은 UTC(universal time coordinated, 협정 세계 표준시)를 사용하여 현재 시간을 
실수 형태로 반환하는 함수이다. 1970년 1월 1일 0시 0분 0초를 기준으로 지난 시간을 초 단위로 반환한다.
"""
print(time.time())


## time.localtime
"""
time.localtime은 time.time()이 반환한 실숫값을 연 월 일 시 분 초
형태로 바꿔주는 함수다.
time.struct_time(tm_year=2026, tm_mon=8, tm_mday=10, tm_hour=22, tm_min=32, tm_sec=49, tm_wday=0, tm_yday=222, tm_isdst=0)
"""
print(time.localtime(time.time()))


## time.asctime
"""
time.asctime은 time.localtime이 반환한 튜플 형태의 값을 인수로 받아서 날짜와 시간을 알아보기 쉬운 형태로 반환하는 함수이다.
"""
print(time.asctime(time.localtime(time.time())))


## time.ctime
"""
time.asctime(time.localtime(time.time()))은 간단하게 time.ctime()으로 표시할 수 있다. ctime이 asctime과 다른 점은 항상 현재 시간만을 반환한다는 점이다.
"""
print(time.ctime())


## time.strftime
"""
strftime 함수는 시간에 관계된 것을 세밀하게 표현하는 여러 가지 포맷 코드를 제공한다.

time.strftime('출력할 형식 포맷 코드', time.localtime(time.time()))

포맷코드	설명	예
%a	요일의 줄임말	Mon
%A	요일	Monday
%b	달의 줄임말	Jan
%B	달	January
%c	날짜와 시간을 출력함.	Thu May 25 10:13:52 2023
%d	일(day)	[01,31]
%H	시간(hour): 24시간 출력 형태	[00,23]
%I	시간(hour): 12시간 출력 형태	[01,12]
%j	1년 중 누적 날짜	[001,366]
%m	달	[01,12]
%M	분	[00,59]
%p	AM or PM	AM
%S	초	[00,59]
%U	1년 중 누적 주(일요일 시작)	[00,53]
%w	숫자로 된 요일	[0(일), 6(토)]
%W	1년 중 누적 주(월요일 시작)	[00,53]
%x	현재 설정된 지역에 기반한 날짜 출력	05/25/23
%X	현재 설정된 지역에 기반한 시간 출력	17:22:21
%Y	연도 출력	2023
%Z	시간대 출력	대한민국 표준시
%%	문자 %	%
%y	세기 부분을 제외한 연도 출력	01
"""

print(time.strftime('%x', time.localtime(time.time())))
print(time.strftime('%c', time.localtime(time.time())))


## time.sleep
"""
time.sleep 함수는 주로 루프 안에서 많이 사용
이 함수를 사용하면 일정한 시간 간격을 두고 루프를 실행할 수 있다.
"""
for i in range(10):
    print(i)
    time.sleep(1) # 실수 형태로 씀 1 이면 1초 0.5면 0.5초