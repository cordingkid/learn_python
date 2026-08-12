## traceback
# traceback은 프로그램 실행 중 발생한 오류를 추적하고자 할 떄 사용하는 모듈이다.
import traceback

def a():
    return 1/0

def b():
    a()

def main():
    try:
        b()
    except:
        print("오류가 발생했습니다.")
        print(traceback.format_exc())

main()

"""
오류 추적을 통해 main() 함수에서 b() 함수를 호출하고 b() 함수에서 다시 a() 함수를 호출하여
 1 / 0을 실행하려 하므로 0으로 나눌 수 없다는 ZeroDivisionError가 발생했다는 것을 로그를 통해 정확하게 확인할 수 있다.
"""
