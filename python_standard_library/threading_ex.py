## threading
"""
import time
def long_task():
    for i in range(5):
        time.sleep(1)
        print(f"working:{i}\n")
print('== Start ==')
for i in range(5):
    long_task()
print('== End ==')
"""
# 위에 코드를 실행하면 총 25초의 시간이 걸린다.


# 스레드를 사용하면 5초가 걸리는 long_task 함수를 동시에 실행할 수 있다.
#스레드를 사용한 예제
import time
import threading

def long_task():
    for i in range(5):
        time.sleep(1)
        print(f"working:{i}\n")

print('== Start ==')

threads = []
for i in range(5):
    t = threading.Thread(target=long_task) # 스레드를 생성한다.
    threads.append(t)

for t in threads:
    t.start() # 스레드 실행

for t in threads:
    t.join() # join으로 스레드가 종료될때까지 기다린다.

print('== End ==')
    