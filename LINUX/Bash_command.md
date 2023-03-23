# Bash Script

## SheBang(#!)

- SheBang(#!) : 최상단 `#!/bin/bash` `#!/bin/csh` `#!/bin/tcsh` 등 사용할 쉘 선언
- `#! {interpreter} [optional-arg]` : interpreter는 절대경로로 지정
- 단 `#!/usr/bin/env python` 등의 경우 python 버전이 명시되지 않았지만, 현재 환경에서의 python 위치를 찾음(python 외로도 가능)

## String operator

### cut

- 기본 구문

```bash
$ string="abc"
$ echo $string | cut -c 1-2  # -c : 문자열 N-M 만큼 커팅
ab
$ string="010-1234-4567"
$ echo $string | cut -d "-" -f 1  # -d delimiter : 구분자 기준 커팅
010
$ echo $string | cut -d "-" -f 2  # -f delimiter로 만들어진 리스트의 인덱스번호
1234
```

## file

### sort

```bash
$ sort myfile.txt # 정렬
$ sort -u myfile.txt # 유니크 정렬
```

## Statements

### If statement

- 기본 구문

```bash
if [ "conditions" ]; then
    "commands"
elif [ "conditions" ]; then
    "commands"
else
    "commands"
fi
```

- conditions / expression

```bash
# integer comparison
if [ "$a" -eq "$b" ]  : 같음(equal to)
if [ "$a" -ne "$b" ]  : 다름(not equal to)
if [ "$a" -lt "$b" ]  : 작음(less than)
if (( "$a" < "$b" ))
if [ "$a" -gt "$b" ] : 큼(greater than)
if (( "$a" > "$b" ))
if [ "$a" -le "$b" ] : 작거나 같음(less than or equal to)
if (( "$a" <= "$b" ))
if [ "$a" -ge "$b" ] : 크거나 같음(greater than or equal to)
if (( "$a" >= "$b" ))

# string comparison
if [ "$a" == "$b" ]  : 같음(equal to)
if [ "$a" = "$b" ] ※ = 양쪽 모두 빈 칸 이여야 함
if [ "$a" != "$b" ]  : 다름(not equal to)
if [ -z "$a" ] : string 이 null 이 아님(즉, 0이 아닌 길이가 있는 string)

# If statement  Logical AND, OR 문법
if [[ condition1 && condition2 ]] : Logical AND
if [ condition1 ] && [ condition2 ]
if [ condition1 -a condition2 ]
if [[ condition1 || condition2 ]] : Logical OR
if [ condition1 ] || [ condition2 ]
if [ condition1 -o condition2 ]
```

> 참고 : https://chocoamond.tistory.com/56

### For statement

TBC

### Arguments

이 내용은 bash에만 국한된 것이 아니다. 적어도 내가 아는 쉘(csh, bash, tcsh 등)에 한해서는 공통이다.

스크립트 실행시 입력하고자 하는 arguments를 띄워쓰기로 구분하여 넣을 수 있다.

실행시 arguments를 `./sciprt.sh 111 222 333` 과 같이 넣을 수 있다.

그럴 때 사용하고자 하는 argument는 `$1` `$2` `$3`에 차례로 들어가게 된다.

```bash
## script.sh
#!/bin/bash

VAR0=$0  # $0을 넣으면 실행한 스크립트명
VAR1=$1
VAR2=$2
VAR3=$3
VAR_ALL=$*  # 입력인자 모두(문자열)
VAR_SHARP=$#  # 입력인자의 갯수
VAR_AT=$@  # 입력자를 모두 반환($1 ... $N)
VAR_QUESTIONMARK=$?  # 마지막 쉘 명령어의 종료 상태
VAR_UNDERSCORE=$_  # 마지막 반환 값을 반환
VAR_DOLLAR=$$  # 해당 명령어의 프로세스 ID

echo $VAR0
echo $VAR1 $VAR2 $VAR3
echo $VAR_ALL
echo $VAR_SHARP
echo $VAR_AT
echo $VAR_QUESTIONMARK
echo $VAR_UNDERSCORE
echo $VAR_DOLLAR

##
[user@ ~]$ ./sciprt.sh 111 222 333
./script.sh  # $0
111 222 333  # $1 $2 $3
111 222 333  # $* (문자열)
3            # $#
111 222 333  # $@
0            # $?
0            # $_  앞선 $? 출력이 0이기 때문
9900         # $$
```

다른 변수를 넣을 수도 있다.

```bash
[user@ ~]$ ./sciprt.sh 오늘날짜는 `date +\%Y-\%m-\%d` 입니다.
오늘날짜는 2022-03-03 입니다.
```

## DATE 관련

#### `date` 시스템 datetime 표출

```bash
$ date
Wed Mar  2 17:35:38 KST 2022  # KST, UTC 시스템 시간에 따라 다름
```

시스템 시간 설정은 [basic-command](https://github.com/KimJongkwang/TIL/blob/main/LINUX/basic-command.md)에 작성

#### `date` 포맷팅

````bash
$ echo `date +\%Y\%m\%d\%H\%M`   # YYYYMMDDHHMM
202203021736

# 문자열 커팅   ${VALUE:START_INDEX:CUT COUNT}
$ DATE=`date +\%Y\%m\%d`
$ echo $DATE
20220302

$ echo ${DATE:0:4}
2022

$ echo ${DATE:4:2}
03
```bash
#!/bin/bash

````

- 문자 시간 증가, 감소

```bash
$ DATETIME=2022010100
$ DATE=${DATETIME:0:8}  # 20220101
$ HH=${DATETIME:9:2}  # 00

$ echo `date -d "$DD $HH -1hour" +%Y%m%d%H`
2021123123
```

## timeout

TBC
