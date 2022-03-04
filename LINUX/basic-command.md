- 하나씩 업데이트

### Linux 시스템 시간

국가별 시간 기본 설정파일이 존재(/usr/share/zoneinfo)하여 `/etc/localtime`에 링크생성하여 시간 설정

- UTC
  - `sudo ln -sf /usr/share/zoneinfo/UTC /etc/localtime`
- KTC
  - `sudo ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime`

### Crond

crontab -e # 크론탭 설정
crontab -l # 크론 확인
cat /var/log/cron # 크론 로그

```
* * * * * /home/cron/test.sh # 1분간격 실행
0 * * * * /home/cron/test.sh # 1시간간격 실행
# 1 * * * * 보다는 아래와 같이 01로 표기
01 * * * * /home/cron/test.sh

# 가장 중요한 것! 항상 크론을 수정하면, 재가동 필수!
service crond restart
```
