# Model & Model Filed

### Model

: DB의 테이블을 정의하고 데이터를 조작할 수 있는 기능 제공 

**(즉, 데이터베이스 관리를 Model이 함)**

>> 테이블 구조를 설계하는 청사진

### Model Field

: DB 테이블의 **필드(열)**를 정의하며, 헤딩 필드에 저장되는 **데이터 타입(Filed types)**과 **제약조건(Filed options)**을 정의

## model class

```python
from django.db import models

# Create your models here.
class Article(models.Model): # 부모클래스인 모델 클래스(Model)를 상속 받음
    title = models.CharField(max_length=10)
    content = models.TextField # models 모듈 안에 있는 클래스인 TextField
```

- 클래스 변수명

: `title` `content`

: 테이블 각 “필드(열) 이름”

- Model Filed

: `CharField` `TextField`

: 데베 테이블의 **열(filed)**을 나타냄

---

- Model Filed의 구성

: **데이터 타입 (Field types)**.. 필드 유형

: **제약 조건 (Field options)** (필드의 필터링 같은 것)..필드의 인자로 나타냄을 정의

## Field types (필드 유형)


DB에 저장될 “데이터의 종류”를 정의

(model 모듈의 클래스로 정의 ㅇ)python [manage.py](http://manage.py/) makemigrations

---

- 자주 사용하는 필드

: 필드에 따라 필드 옵션이 필수일 수도 ㅇ

### 문자열 필드

`CharField()`

제한된 길이의 문자열 저장 

(필드의 최대 길이를 결정하는 max_lenght(=필드 옵션)는 필수 옵션)

 `TextField()`

길이 제한이 없는 대용량 텍스트 저장

(무한대는 아님, 사용하는 시스템에 따라 달라짐)

### 숫자 필드

`IntegerFiled` `FloatField`

### 날짜 / 시간 필드

`DateField` `TimeField` `DateTimeField`

---

<aside>
💡

### `DateTimeField`의 필드 옵션 (시험)

`auto_now`

: 데이터가 **저장될 때마다** 자동으로 현재 날짜시간 저장

`auto_now_add`

: 데이터가 **처음 생성될 때만** 자동으로 현재 날짜시간을 저장

</aside>

### 파일 관련 필드

`FileField`  `ImageField`

## Field option (필드 옵션)


필드(column)의 “동작”과 “제약 조건”을 정의

---

### 제약 조건 (constraint)

특정 규칙을 강제하기 위해 테이블의 열이나 행에 적용되는 규칙

예)) 숫자만 저장되도록, 문자 100자 이내만 저장되도록..

# Migrations

model 클래스의 변경사항 (필드 생성, 수정 삭제 등)을 DB에 최종 반영하는 방법

: Model에 의해 만든 설계도를 Migreations로 실현

<aside>
💡

- db는 원격저장소에 올라가지 않음
- 설계도는 올라감
</aside>

---

- **2단계**로 나눠짐

```python
python manage.py makemigrations
```

: model class를 기반으로 최종 설계도(migrations)를 작성

```python
python manage.py migrate
```

: 최종 설계도를 DB에 전달하여 반영

---

## 이미 생성된 테이블에 필드 추가하기

>> 입력창에 1, 2를 입력하면 됨

---

초기에 생성된 설계도에 의존(dependencies)해서 다른 설계도 추가

---


---

### 정리

>> model class에 변경사항이 생기면, 반드시 새로운 설계도를 생성하고 이를 db에 반영해야 함 (이 3가지 과정이 migrations)


---

## Admin site

### Automatic admin interface

장고가 추가 설치, 설정 없이 자동으로 제공하는 관리자 인터페이스

>> 데이터 확인 및 테스트 등을 진행

<aside>
💡

**migrations 을 해야 admin 계정이 만들 수 있다!!**

>> 관리자 계정 정보가 저장되려면 테이블이 있어야하는데 migrations을 해야 테이블이 생기니까..

</aside>

---

### 1. admin 계정 생성

: Username

: email은 선택사항

: 비밀번호 입력 시, 보안상 터미널에 출력되지 않으니 무시하고 입력 이어가도 됨

```python
python manage.py createsuperuser
```

### 2. DB에 생성된 admin 계정 확인


: `auth_user` 에 admin 계정 ㅇ

### 3. admin에 모델 클래스 등록


```python
from django.contrib import admin
#from . import models.Article
from .models import Article # 명시적 경로 / 현재 경로에 있는 model파일에서 Article을 불러온다

# Register your models here.
# admin site에 등록한다
admin.site.register(Article)

```

### 4. admin site 로그인 후 등록된 모델 클래스 확인


### 5. 데이터 생성, 수정, 삭제 테스트


### 6. 테이블 확인

  
## 데이터베이스 초기화


>> 설계도, DB 삭제

## Migrations 관련

```python
python managr.py showmigration
```

: 설계도의 migration상태를 알 수 ㅇ

```python
python managr.py sqlmigration articles 0001
```

: 0001 설계도를 보여줘
