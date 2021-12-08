* 하나씩 업데이트

### Linux 시스템 시간
국가별 시간 기본 설정파일이 존재(/usr/share/zoneinfo)하여 `/etc/localtime`에 링크생성하여 시간 설정

- UTC
  - `sudo ln -sf /usr/share/zoneinfo/UTC /etc/localtime`
- KTC
  - `sudo ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime`
