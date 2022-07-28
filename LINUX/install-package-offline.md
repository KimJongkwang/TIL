# 패키지 오프라인 설치(Centos)

## 오프라인 설치 준비

### rpm 다운로드

온라인 환경에서 다운받을 rpm 파일을 다운로드한다.

`yum -y install [package-name] --downloadonly --downloaddir=[directory]`

위와 같이 `--downloadonly` 옵션으로 해당 패키지 rpm파일만 설치할 수 있다.

해당 패키지 설치에 필요한 의존 패키지들도 함께 설치된다. 하지만 모든 의존성이 해결되는 것은 아니니 주의해야한다.

### 오프라인 설치

위에서 다운받은 rpm 파일들을 오프라인으로 설치할 서버에 옮겨놓고, 

해당 위치에서 `yum install [package.rpm]`의 명령어로 rpm 파일들을 하나씩 설치해주면 된다.
