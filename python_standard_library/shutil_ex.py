"""
shutil은 파일을 복사(copy)하거나 이동(move)할 때 사용하는 모듈이다.

작업 중인 파일을 자동으로 백업하는 기능을 구현하고자 c:\doit\a.txt를 c:\temp\a.txt.bak이라는 이름으로 복사하는 프로그램을 만들고자 한다. 어떻게 만들어야 할까? c:\doit 디렉터리에 a.txt를 만드는 중이며 백업용 c:\temp 디렉터리는 이미 만들었다고 가정한다.

다음은 shutil을 사용한 방법이다.

# shutil_copy.py
import shutil

shutil.copy("c:/doit/a.txt", "c:/temp/a.txt.bak")
점프 투 파이썬
shutil.move로 삭제 기능 만들기

휴지통으로 삭제하는 기능을 구현하고자 c:\doit\a.txt 파일을 c:\temp\a.txt로 이동하려면 다음과 같이 코드를 작성해야 한다.

# shutil_move.py
import shutil

shutil.move("c:/doit/a.txt", "c:/temp/a.txt")
"""