# 리눅스 에러 모음집

## shell script

### /bin/sh^M: bad interpreter

- 스크립트 실행시 아래와 같은 에러가 발생하는 경우가 있다.

`-bash: ./file.sh: /bin/sh^M: bad interpreter: No such file or directory`

- 윈도우에서 스크립트를 작성하고 리눅스에서 작성할 때 나타나는 오류라고 한다.
- 윈도우의 줄 바꿈을 의미하는 개행문자(^M)가 스크립트에 남아있어 리눅스에서 인식하지 못한다.
- 해결은 간단하다. vi 편집기를 binary 모드(-b)로 실행하여 붙어있는 ^M를 제거해준다.

`vi -b file.sh`
