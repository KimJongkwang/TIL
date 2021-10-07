### NFS를 통해 nas서버 마운트

서버내 nas서버를 마운트하기 위해서는 NFS프로그램을 필요로 합니다.

nas에서 NFS 서버가 실행중임을 가정하겠습니다.

1. 먼저 NFS 프로그램 설치유무를 확인하고 없다면, 프로그램을 설치하겠습니다.
    
    `$ rpm -qa | grep nfs-utils`
    
    `$ yum -y install nfs-utils`


2. nas를 붙일 디렉토리를 생성하고 nfs를 통해 마운트합니다.

    `$ mkdir -p /data/nas`
    
    `$ mount -t nfs [nas ip]:[nas dir] /data/nas`

3. 서버 부팅시 자동으로 마운트 설정

    `$ vi /etc/fstab`
    
    `[nas ip]:[nas dir] /data/nas nfs defalut 0 2`

    - 위 순서대로 `마운트 대상` `마운트 경로` `파일시스템 종류` `마운트 옵션` `Dump 유무` `무결성 검사 우선순위` 입니다.
    - 이 중 마운트 옵션은 아래와 같습니다
        + default : rw, nouser, auto, exec, suid속성을 모두 설정
        + auto : 부팅시 자동마운트
        + noauto : 부팅시 자동마운트를 하지않음
        + exec : 실행파일이 실행되는것을 허용
        + noexec : 실행파일이 실행되는것을 불허용
        + suid : SetUID, SetGID 사용을 허용
        + nosuid : SetUID, SetGID 사용을 불허용
        + ro : 읽기전용의 파일시스템으로 설정
        + rw : 읽기/쓰기전용의 파일시스템으로 설정
        + user : 일반사용자 마운트 가능
        + nouser : 일반사용자 마운트불가능, root만 가능
        + quota : Quota설정이 가능
        + noquota : Quota설정이 불가능

        > 출처: https://movenpick.tistory.com/34 [MoVenPick]
