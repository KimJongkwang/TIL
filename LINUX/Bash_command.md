# Bash Script

shell_scripts.sh 에서 .sh 를 통해 쉘스크립트 선언

최상단 `#!/bin/bash` `#!/bin/csh` `#!/bin/tcsh` 등 사용할 쉘 선언해준다.

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

TBD

## DATE 관련

#### `date` 시스템 datetime 표출

```bash
$ date
Wed Mar  2 17:35:38 KST 2022  # KST, UTC 시스템 시간에 따라 다름
```

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
