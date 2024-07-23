# Git 명령어 정리
## Working directory (1단계)

: 실제 작업 중인 파일이 있는 일종의 폴더

### git init

초기화 (like 변수 초기화 / 나 뭐 만들거야~)
git 저장소 생성

### git clone (github 주소)

로컬 저장소(디렉토리) <-> 원격 저장소(디렉토리) 연결, 가져오기

### cd (이동하고픈 저장소 위치)

저장소의 해당 위치로 이동

- change directory

### ls

디렉토리의 내용 확인

### ls -l

디렉토리의 파일과 디렉토리 목록을 자세히(long format) 출력

### mkdir (디렉토리이름)

디렉토리(폴더) 생성
make directory

### touch (생성하고픈 파일(예))a.txt))

파일 생성

### git status

로컬 저장소의 파일 상태 확인 (습관화!)

### git commit —amend

바로 직전 생성한 commit 수정하기

### git log

: commit 내역 확인

### cat (파일이름)

파일 내용을 출력

---

## Staging Area (2단계)

: 변경된 파일 중 다음 버전에 포함될 파일을 선택적으로 추가

### git add 파일이름

### git add . (폴더 안에 든 파일 전체 add)

파일을 Staging Area(2)에 저장

### git commit -m "message"

파일을 (Staging Area(2)>>)Repository(3)에 저장

- commit(버전) : 변경된 파일을 저장하는 행위 / 버전 기록

---

## Repository (3단계)

: 버전 이력과 파일들이 영구적으로 저장되는 영역

### git remote (github 주소)

로컬 저장소에서 원격 저장소 연결

전에 git init을 해야함

### git remote -v

원격 저장소(Repository) 확인

### git remote add origin (깃헙주소)

별칭을 사용해 로컬 저장소 한 개에 여러 원격 저장소를 추가

- origin (추가하는 원격 저장소 별칭 / 다른 이름써도 됨)

### git push origin master

원격 저장소에 업로드(push) (이미 연결된 상태)
원격 저장소의 master 브랜치에 업로드

**원격 저장소에는 파일이 아니라  commit이 올라간다**

- master : 브랜치(branch) 이름

### git pull origin master

원격 저장소의 변경사항만을 받아옴 (업데이트)

### git clone remote_repo_url

(원격저장소에 있는 레포지토리를 로컬저장소에 가져옴)

한 번도 연결한 적 없는 레포지토리 가져오는 것git
클론으로 받은 프로젝트는 이미 git init이 되어있음

### git push

로컬저장소 to 원격저장소

### git pull

원격저장소 to 로컬저장소

---

## git config

### git config --global [user.name](http://user.name/) "홍길동"

### git config --global user.email "[name@naver.com](mailto:name@naver.com)"

git config 설정

### git config --unset [user.name](http://user.name/)

### git config --unset user.email

git config 삭제
