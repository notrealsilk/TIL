# ORM

object-relational-mapping

객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 데이터를 변환하는 기술

---

>> 장고와 db간에 언어가 다름 → 장고에 내장된 ORM이 중간에서 해석

# ORMSet API

ORM에서 데이터를 검색, 필터링, 정렬 및 그룹화 하는 데 사용하는 도구

**: 즉, 파이썬의 모델 클래스와 인스턴스를 활용해 DB에 데이터를 저장, 조회, 수정, 삭제 하는 것( = CRUD)**

>> API를 사용해서 파이썬 코드로 데이터 처리

>> **Queryset api 언어가 중요**!

## QuerySet API 구문

`모델클래스.매니저(=objects).명령어`

- article에 의해 생성된 테이블 모두를 가져와줘

>> 즉, 전체 조회를 하는 구문

```python
Article.objects.all()
```

---

- 동작 예시

- 데이터 타입을  QuerySet 방식으로 전달

---

### Query

db에 특정한 데이터를 보려 달라는 요청

: 파이썬으로 작성한 코드가 ORM에 의해 SQL로 변환, DB에 전당됨 -> DB의 응답 데이터를 ORM이 QuerySet이라는 자료 형태로 변환하여 사용자에게 전달

### QuerySet

DB에게서 전달 받은 객체 목록(데이터 모음)

(순회가 가능한 데이터로써, 1개 이상의 데이터를 불러와 사용 ㅇ)

: 장고 ORM을 통해 만들어진 자료형

: 단, DB가 단일한 객체를 반환할 때는 모델(Class)의 인스턴스로 반환됨

## CRUD

소프트웨어가 가지는 기본적인 데이터 처리 기능 (5개)

**Create**(저장) / Read(조회)..**단일 게시글**, **전체 게시글**  / **Update** (갱신) / **Delete** (삭제)

# ORMSet API 실습

### 사전준비

1. 외부 라이브러리 설치 및 설정
    
    
>> `'django_extensions'` 는 앱등록을 해줘야하는 라이브러리!

>> 새로운 라이브러리 설치했으므로  requirements.txt 다시 갱신

2. 장고 shell 실행

```python
python manage.py shell_plus
```

: 장고 환경 안에서 실행되는 파이썬 쉘

: `'django-extensions'` 을 설치하고, `'django_extensions'` 를 앱 등록해야 사용 가능

(입력하는 QuerySet API 구문이 장고 프로젝트에 영향을 미침)

: `exit` : shell 빠져나오기
    
    ---
    

## Create

### 데이터 객체 만들기 (3)

>> 게시글 작성 방법이 3가지

---

1. 클래스로 인스턴스 만들기

```python
# 1. 클래스로 인스턴스 만들기
article = Article()

# 2. 인스턴스 변수 할당
article.title = “frist”
article.content = “django”

# 3. save()메서드로 저장
article.save()
```

1.  처음에 인스턴스 생성할 때, 초기값을 할당

: 테이블 한 행(레코드)이 쓰여지는 것

```python
## 예 )) 
article = Article(title='second',content='django!')
```

<aside>
💡

`save()`

객체를 DB에 저장하는 인스턴스 메서드

1. `save()`를 호출해야 DB에 데이터가 저장됨
</aside>

1. QuerySet API 중 `create()` 메서드 활용

```python
 Article.objects.create(title='four', content='django!')
```

: `save()` 없어도 됨

---

## Read (3)

### Return new QuerySets (2)

<aside>
💡

조회할 데이터가 없어도 조회 ㅇ / queryset으로 반환!

</aside>

---

`all()` : 전체 데이터 조회

```python
Article.objects.all()
```

`filter()` : 매개변수와 일치하는 객체를 포함하는 QuerySet 반환

```python
Article.objects.filter()
```

---

### Do not retrun QuerySets (1)

<aside>
💡

- 조건에 없는 데이터를 조회하면 에러가 남
- 조회 결과가 n개이면 에러

---

**>> 즉, 없는 것과 여러개 조회가 안됨 (단일조회!!)**

</aside>

---

`get()` : 주어진 매개변수와 일치하는 객체를 반환

기본키가 1인 게시글을 줘~

기본키가 없으면 에러

같은 값인 게시글이 여러개면 에러

---

- get()의 특징

: 객체를 찾을 수 없으면 DoesNotExist 예외를 발생시키고, 둘 이상의 객체를 찾으면 MultipleObjectReturned 예외를 발생 ㅇ

: **기본키(pk)와 같이 고유성(uniqueness)이 보장되는 조회에서 사용!**

---

### 기타 명령어

- 인덱스 접근도 가능

데이터 조회 → 인덱스 접근

```python
1. 쿼리문을 변수에 저장

articles = Article.objects.filter(title='first')

articles[0]
>> <Article:Article object (1)>

---
articles[0].content
'django!'
```

- 기본키 접근

[`articles.id`](http://articles.id) 보단 [`articles.pk`](http://articles.pk) 를 권장

```python
[articles.pk](http://articles.pk)
```

## Update

인스턴스 변수 변경 → `save()` 메서드 호출

## Delete

1. 삭제하려는 데이터 조회 → 2. `delete()` 메서드 호출

>> 지워진 데이터의 pk는 다시 생성되지 않음

(즉, 1번 객체가 삭제되면 1번은 다시는 할당 안됨)

# ORM with view

장고 shell에서 연습했던 QuerySet API를 직접 view 함수에서 사용하기

---

예)) 전체 게시글 조회

## Field lookups

: 추가 조건을 `__` 를 통해 진행 (던더 스코어=더블 스코어)

```python
Article.objects.filter(content__contains='dja')
```
