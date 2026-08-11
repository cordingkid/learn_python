"""
os

os 모듈은 환경 변수나 디렉터리, 파일 등의 OS 자원을 제어할 수 있게 해 주는 모듈이다.

내 시스템의 환경 변숫값을 알고 싶을 때 - os.environ
시스템은 제각기 다른 환경 변숫값을 가지고 있는데, os.environ은 현재 시스템의 환경 변숫값을 반환한다. 다음을 따라 해 보자.

>>> import os
>>> os.environ
environ({'PROGRAMFILES': 'C:\\Program Files', 'APPDATA': … 생략 …})
이 결괏값은 필자의 시스템 정보이다. os.environ은 환경 변수에 대한 정보를 딕셔너리 형태로 구성된 environ 객체로 반환한다. 자세히 보면 여러 가지 유용한 정보를 찾을 수 있다.

반환받은 객체는 다음과 같이 호출하여 사용할 수 있다. 다음은 필자 시스템의 PATH 환경 변수 내용이다.

>>> os.environ['PATH']
'C:\\ProgramData\\Oracle\\Java\\javapath;...생략...'
디렉터리 위치 변경하기 - os.chdir
os.chdir를 사용하면 다음과 같이 현재 디렉터리의 위치를 변경할 수 있다.

>>> os.chdir("C:\\WINDOWS")
디렉터리 위치 돌려받기 - os.getcwd
os.getcwd는 현재 자신의 디렉터리 위치를 반환한다.

>>> os.getcwd()
'C:\WINDOWS'
시스템 명령어 호출하기 - os.system
시스템 자체의 프로그램이나 기타 명령어를 파이썬에서 호출할 수도 있다. os.system("명령어")처럼 사용한다. 다음은 현재 디렉터리에서 시스템 명령어 dir을 실행하는 예이다.

>>> os.system("dir")
실행한 시스템 명령어의 결괏값 돌려받기 - os.popen
os.popen은 시스템 명령어를 실행한 결괏값을 읽기 모드 형태의 파일 객체로 반환한다.

>>> f = os.popen("dir")
읽어 들인 파일 객체의 내용을 보려면 다음과 같이 하면 된다.

>>> print(f.read())
이 밖에 유용한 os 관련 함수는 다음과 같다.

함수	설명
os.mkdir(디렉터리)	디렉터리를 생성한다.
os.rmdir(디렉터리)	디렉터리를 삭제한다. 단, 디렉터리가 비어 있어야 삭제할 수 있다.
os.remove(파일)	파일을 지운다.
os.rename(src, dst)	src라는 이름의 파일을 dst라는 이름으로 바꾼다.

"""