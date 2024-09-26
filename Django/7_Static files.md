### - Django static files 공식 문서

[How to manage static files (e.g. images, JavaScript, CSS) | Django documentation](https://docs.djangoproject.com/en/5.1/howto/static-files/)

---
# Static files (정적 파일)

서버 측에서 변경되지 않고 고정적으로 제공되는 파일 (이미지, JS, CSS 파일..)

## 웹 서버와 정적 파일

- 웹 서버는 **특정위치(URL)에 있는 자원(=데이터)**을 요청(HTTP request)받아서 응답(HTTP response)을 처리, 제공함
- 웹 서버는 요청받은 URL로 서버에 있는 정적 자원 제공

>> **정적 파일을 제공하기 위한 경로(URL)**이 있어야 ㅇ >> ..요청에 응답하기 위해서

## Static files 기본 경로

### `app폴더/static`

: static 폴더도 직접 만들어줘야 ㅇ

---

### 1. 폴더 만들기

- `articles/static/articles/` 에 이미지 파일 배치

### 2. 이미지를 넣을 HTML에 IMG태그 작성

```html
{% load static %}

<img src="{% static 'articles/sample-1.png' %}" alt="sample-image">
```

- bulit-in tag가 아님 >>  **load tag를 사용해 import 후 사용 가능** (`load` 입력 → `tab`)
- static files 경로는 DTL의 static tag를 사용해야 ㅇ
- 약속된 경로 이후의 정적 파일의 경로를 `{% static ‘’ %}`에 작성!
- `{% load static %}` 은 상속 x → `base.html`에 `{% load static %}`해도 자식 html에 적용 x

---

### 3. 서버키면 URL에 이미지 ㅇ

- 로컬의 이미지 주소 ≠ 웹 상의 이미지 주소

>> 웹 상의 주소가 있어야 클라이언트가 이미지를 볼 수 ㅇ

# Media files

사용자가 웹에서 업로드하는 정적 파일 (user-uploaded)

## 이미지 업로드

### `ImageField()`

: 이미지 업로드에 이용하는 모델 필드

- 이미지 업로드할려면 테이블에 자리가 있어야하므로 모델 필드에 이미지 저장할 자리 만들어줘야 ㅇ
- 이미지 필드는 문자열 필드

>> so, **이미지 파일의 경로 문자열**이 저장됨 ..이미지 객체가 db에 저장 x

---

### 사전 준비

### 1. settings.py에 `MEDIA_ROOT`,`MEDIA_URL` 설정

### `MEDIA_ROOT`

미디어 파일들이 위치하는 디렉토리 절대 경로

```python
# settings.py

# 이 폴더에 사용자가 업로드한 이미지를 저장하겠다
# 이미지가 업로드되면 'media' 폴더가 생성
MEDIA_ROOT = BASE_DIR /'media'
```

### `MEDIA_URL`

MEDIA_ROOT에서 제공되는 미디어 파일의 주소 생성 

(STATIC_URL과 역할 같음)

```python
# settings.py

MEDIA_URL = 'media/'
```

### 2. `MEDIA_ROOT`,`MEDIA_URL` 의 URL 지정

: [urls.py](http://urls.py) 에 지정해주기

- 업로드된 파일 url ⇒ settings.MEDIA_URL
- MEDIA_URL로 참조하는 파일의 실제 위치 ⇒ settings.MEDIA_ROOT

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

```python
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# static(URL 주소, 미디어 파일의 실제 위치)
```

: 리스트 안에 써도 되지만, path와 구분하기 위해 리스트 뒤에 +로 추가해줌

---

### 과정

### 1. black=True 속성으로 빈 문자열이 저장될 수 있게 제약조건 설정

>> 이미지 없어도 게시글 작성 될 수 있게 하는 것

```python
## models.py

from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    
    # field는 기본적으로 공백을 허용안하므로 blank=True로 설정해줘야 ㅇ
    image = models.ImageField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

### 2. migrate

### 3. form 요소의 enctype 속성 추가

```html
  ## html
  
  <h1>Create</h1>
  
  # enctype="multipart/form-data"이 있어야 이미지 파일 주소전송 가능
  <form action="{% url "articles:create" %}" method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
```

: 이미지 주소를 보내려면 form태그에 속성을 추가해야 ㅇ

### 4. ModelForm 2번째 인자로 요청 받은 파일 데이터 작성

```python
## views.py

def create(request):
    if request.method == 'POST':
	    # 이미지 파일은 request.FILES에 의해 데이터가 넘어감
        form = ArticleForm(request.POST, request.FILES)
```

>> DB에는 파일 경로가 저장됨

## 업로드 이미지 제공

### 1. url 속성으로 업로드 파일의 경로 값 얻을 수 ㅇ

`article.image.url` : 업로드 파일 경로

`article.image` : 업로드 파일의 파일 이름

```html
# midia 폴더에 있는 이미지의 url주소
<img src="{{ article.image.url }}" alt="img">
```

### 2. 업로드 이미지 출력 확인 및 MEDIA_URL 확인

### 3. 이미지 데이터가 있는 경우에만 이미지 출력할 수 있게 하기

>> 이미지 없는 게시물은 detail 템플릿을 렌더링 할 수 x

: 이 설정 안하면 디테일 템플릿(페이지)가 안 뜨므로..


## 업로드 이미지 수정

- 수정 페이지 form요소에 enctype 속성 추가
    
  
    - update.html
    
    ```html
    
    enctype="multipart/form-data"
    ```
    
- update view 함수에 업로드 파일 추가 코드 작성
    
  
    - update.view.py
    
    ```html
    request.FILES
    ```

## 미디어 파일 추가 경로

- setting.py에서 설정한 media/ 이후의 경로들을 설정하는 다양한 방법

```python
## models.py

# 1. 기본 경로 설정
image = models.ImageField(blank=True, upload_to='images/')
# -> migrate 하면 media/images/ 폴더가 생김 (항상 media 폴더 밑에 생김)

# 2. 업로드 날짜로 경로 설정
image = models.ImageField(blank=True, upload_to='%Y/%m/%d/')
# -> media/2024/09/25/image.jpg

# 3. 함수 형식으로 경로 설정

## views.py
def articles_image_path(instance, filename):
	return f'image/{inatance.user.usernmae}/{filename}'

## models.py
image = models.ImageField(blank=True, upload_to=articles_image_path')
```

## BaseModelForm

`request.FILES` 는 두번째 인자

: FILES 또한 키워드 인자 생략 가능 (첫번째 인자인 request는 필수적으로 작성되서 두번째 인자도 자연스럽게 생략 가능..)
