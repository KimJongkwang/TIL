# branch

#### branch 생성

- `git branch` # 현재 생성된 브랜치 조회
- `git branch {branch name}` # 생성
- `git switch -c {branch name}` # 생성 후 전환
  - `git switch -c {생성할 브랜치} main` # 위와 동일
  - `git switch -c {생성할 브랜치} {기준 브랜치}`

#### PR 후 업로드

- `git add {file/folder}`
- `git commit -m "commit masage"`
- `git push origin {브랜치 이름}`

#### branch 삭제

- `git branch -d {브랜치 이름}`
- `git branch -D {브랜치 이름}` # 강제 삭제

- `git push origin --delete {브랜치 이름}` # 원격 저장소 브랜치 삭제
  - `error: unable to delete [BRANCH NAME] : remote ref does not exist` 에러 발생시
    - 로컬PC에 기록된 remote 서버 브랜치 정보와 실제 원격 서버의 브랜치 정보가 일치하지 않기 때문.
    - 로컬PC에서는 이미 브랜치가 삭제되었으나, 원격 서버에서는 남아있는 경우 또는 반대의 상황에서 발생
    - `git fetch -p origin` 하여 원격 서버의 정보를 주기적으로 fetch

## git stash

브랜치내에서 작업을 하다 다른 브랜치로 옮겨야 할 경우, 커밋이 하지 않은 상태로 브랜치를 옮겼다 다시 돌아오고 싶은 경우에 사용

stash 명령을 사용하면 워킹 디렉토리에서 수정한 파일만 저장. stash는 modified, tracked 이거나 staging area 에 있는 파일을 보관하는 장소이다.

- `git stash`

  - 작업 중인 파일은 stash 한다.
  - `git stash save` 도 동일하다.

- `git stash list`

  - stash 한 작업 목록을 보여준다.

- `git stash apply`

  - 기존 작업중이던 브랜치나 옮겨야할 브랜치로 온 상태에서 stash한 파일들을 적용한다.
