## PIP(Package Installer for Pyhton) 없이 패키지 설치

### 인터넷 환경에서 pip 설치

인터넷 환경에서 설치시에는 yum(centos)이나 apt-get(ubuntu)으로 설치가능합니다.
```bash
# centos
yum install python-pip
# ubuntu
apt-get install python-pip
apt-get install python3-pip
```
또는 https://pip.pypa.io/en/stable/installation/ 에서 제공하는 `get-pip.py`를 파이썬으로 실행하여 pip를 설치가능합니다.


### 폐쇄망에서 pip 설치

다만 인터넷이 되지 않는 폐쇄망의 경우에는 pip와 설치하고자 하는 패키지의 wheel파일을 오프라인으로 설치해야합니다.

먼저 마찬가지로 [https://pip.pypa.io/en/stable/installation/](https://pip.pypa.io/en/stable/installation/)에서 pip wheel과 패키지 wheel을 다운받아 폐쇄망 로컬에 옮겨놓습니다.

```
get https://files.pythonhosted.org/packages/0f/74/ecd13431bcc456ed390b44c8a6e917c1820365cbebcb6a8974d1cd045ab4/pip-10.0.1-py2.py3-none-any.whl
```

이후 설치된 환경에서 `python pip-10.0.1-py2.py3-none-any.whl install --no-index [package wheel].whl`과 같이 설치해주면 됩니다.


