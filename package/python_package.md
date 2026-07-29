패키지란 관련 있는 모듈의 집합이다.
패키지를 사용하면 파이썬 모듈을 계층적으로 관리할 수 있다.
# 파이썬에서 모듈은 하나의 .py 파일임

# Ex
game/
    __init__.py
    sound/
        __init__.py
        echo.py
        wav.py
    graphic/
        __init__.py
        screen.py
        render.py
    play/
        __init__.py
        run.py
        test.py

패키지 구조로 만드는 것이 공동 작업이나 유지 보수에 유리함
또한 패키지 구조로 모듈을 만들면 다른 모듈과 이름이 겹치더라도 안전하게 사용가능

__init__.py 파일의 용도
__init__.py 파일은 해당 디렉터리가 패키지의 일부임을 알려주는 역할을 한다. 만약 game, sound, graphic 등 패키지에 포함된 디렉터리에 __init__.py 파일이 없다면 패키지로 인식되지 않는다.

python 3.3 버전부터는 __init__.py 파일이 없어도 패키지로 인식한다. 하지만 __init__.py 파일을 생성하는 것이 파이썬 커뮤니티의 일반적인 관례이므로 항상 만들어 주는 것이 좋다.

