"""
try 블록 안에 그냥 넣으면 되지 않나?"라고 생각할 수 있다. 
하지만 else 절에 넣은 코드는 except의 대상이 되지 않는다. 
따라서 try 블록에서 발생할 수 있는 오류만 정확히 잡고, 
나머지 코드에서 발생하는 의도치 않은 오류가 except에 잡히는 것을 방지할 수 있다.
"""

try:
    age = int(input('나이 입력:  '))
except:
    print('입력이 정확하지 않습니다.')
else:
    if age <= 18:
        print("미성년자는 출입금지")
    else:
        print("입장가능")