# 다른 경로의 파일 또는 모듈 import

파이썬은 기본적으로 메인으로 실행하는 스크립트의 위치를 기준으로 경로를 잡는다.

종종 다른 경로에서 작성한 코드가 필요한 경우가 있을 때, 똑같은 코드를 중복하여 작성하는 것은 낭비일 것이라 생각된다.

이를 위해 다른 경로에서 모듈을 import 하는 방법을 알아보도록 한다.

아래와 같이 디렉토리가 구성되어 있다고 했을 때, main.py에서 다른 패키지를 import 하는 방법을 알아보자.

```
$ tree

project
├─main
│  ├─main.py
│  ├─same_dir.py
│  └─sub_dir
│       └─sub_module.py
└─upper_dir
   └─upper_module.py
```

## 동일, 하위 경로

동일한 위치의 모듈과 하위에 위치한 모듈을 import 하는 것은 간단하다. 현재의 위치보다 아래에 있기 때문에 import 에서 선언하는 것으로 가능하다.

> python3.3 이전 버전의 파이썬에서는 하위 디렉토리에서 `__init__.py`를 작성하여 디렉토리가 모듈로 인지하게끔 유도하였다. 현재는 없어도 패키지로 인지되지만, 하위버전과 호환을 위해 생성하는 것이 좋다고 한다.

```python
# import same_dir.py
import same_dir
from . import same_dir
...

# import sub_module.py
import sub_dir
from sub_dir import sub_module
...

from sub_dir.sub_module import function, Class
...

```

## 상위 경로

현재 메인 실행파일보다 상위에 위치한 경로에서 타고들어가는 모듈을 import 하는 방법은 단순히 선언하는 것으로는 어렵다.

여러 방법들이 있겠지만, 최상위 경로를 현재 파일 경로에 추가해주는 것으로 작성해보겠다.

```python
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from upper_dir import upper_module.py
...

```

위와 같이 `__file__` 메서드로 현재 경로를 가져와 상위의 절대경로를 시스템 경로에 추가해줄 수 있다.

또한, 전혀 다른 경로에 위치한 파일의 절대경로로 넣는다면 동일한 방법으로 가능하다.

## 참고

> https://codechacha.com/ko/how-to-import-python-files/
