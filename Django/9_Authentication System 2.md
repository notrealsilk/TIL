# 회원 가입

User 객체를 Create 하는 과정

## UserCreationForm()

회원 가입할 때 사용자 입력 데이터 받는 빌트인 ModelForm

### 1. 회원 가입 페이지 작성

---

- 회원 가입 로직 에러

>> but, 회원가입 시도 후 에러 페이지 ㅇ

### 이유


>> 회원가입에 사용된 `UserCreationForm()` 는 장고의 기본 유저 모델로 작성된 클래스이기 때문


so, 커스텀 유저 모델을 작성하려면 다시 form 작성 필요

---

### `UserCreationForm()`, `UserChangeForm()`

: class Meta: model = User 가 작성된 Form이기 때문에 **재작성 필요**



### `get_user_model()`

: User 모델을 참조하는 간접적 방법 → 함수 사용
: 현재 프젝에서 활성화된 사용자 모델(active user model)을 반환하는 함수
: **Django는 User클래스를 직접 참조하는걸 권장 X**

- User 모델을 직접 참조하지 않는 이유

<aside>
💡

- `get_user_model()` 은 User 모델을 참조하면 커스텀 User 모델을 자동으로 반환하기 때문
- 유저 모델 이름이 바뀌면 유지 보수가 힘듦

---

: so, 장고는 필수적으로 User 클래스를 직접 참조하지 x

: `get_user_model()` 사용!

</aside>


### 2. 회원 가입 로직 작성

>> 회원가입이 됐을 뿐, 로그인은 안 됨 (따로 설정 안했기 떄문)

# 회원 탈퇴

User 객체를 Delete 하는 과정 → 회원 정보 삭제 

(like 로그아웃 → 세션삭제)

### 1. 회원 탈퇴 로직 작성

<aside>
💡

- urls.py

: request에 user정보가 담겨져 있기 때문

: 로그아웃 Delete와 달리, 회원 탈퇴 Delete 조회를 할 필요 없으므로 <int:pk>.. variable routing할 필요 X

</aside>


# 회원정보 수정

User 객체를 Update 하는 과정

## UserChangeForm()

회원정보 수정시 사용자 입력 데이터를 받는 빌트인 ModelForm

### 회원정보 수정 페이지 작성


---

<aside>
💡

### UserChangeForm 사용 시 문제점

User 모델의 모든 정보(fields)를 모두 출력

즉, 권한 설정이 안 됨

>> customUserChangeForm에서 출력 필드 재조정!

</aside>

- customUserChangeForm 출력 필드 재정의

## customUserChangeForm 출력 필드 재정의

: 비밀번호 변경은 회원정보 수정에서 안됨

>> 회원정보 form에는 비밀번호 filed가 없기 때문


---

# 회원정보 수정 : 비밀번호 변경

인증된 사용자의 Session데이터를 Update를 하는 과정

## PasswordChangeForm()

비밀번호 변경 시 사용자 입력 데이터를 받는 built-in Form

---

<aside>
💡

### form 인 이유

: 비밀번호 자체가 저장되는게 아닌, session을 변경하는 거여서 비밀번호는 저장될 필요 없음 → model form X

</aside>

### 비밀번호 변경 페이지 작성

- `프로젝트 / urls.py`

<aside>
💡

`user_pk/password/`가 주소이기 때문에 accounts 앱이 아닌 프로젝트 [urls.py](http://urls.py) 에서 설정해주기

</aside>


---

### 최종 비밀번호 변경 로직

## 세션 무효화 방지

암호를 변경하면 로그아웃

>> 기존 Session ≠ 회원 인증 정보 때문

: 비밀번호 변경은 Session 데이터를 바꾸는 것, 클라이언트가 보낸 세션 id가 서버의 Session 데이터와 달라서 로그인이 안됨 → 로그아웃

---

### `update_session_auth_hash(request, user)`

암호 변경시 세션 무효화를 막아주는 함수

>> 기존 session을 새로운 비밀번호의 Session Data로 변경해줌

: 비밀번호 변경 후, 적용해줘야 함

---

- 인증된(=로그인) 사용자에 대한 접근 제한

# 인증된 사용자에 대한 접근 제한

## 1. is_authenticated 속성

### `is_authenticated`

사용자의 인증 여부를 알 수 있는 User model 속성 (T,F)

>> 모든 User 인스턴스에 대해 **(로그인) 항상 True**인 읽기 전용 속성

>> 비인증 사용자**(비로그인)는 항상 Fales**

```python
request.user.is_authenticated
```

### 적용

- 로그인과 비로그인 상태에서 화면에 출력되는 링크를 다르게 설정
  - `앱 / index.html`
  
  
- 인증된 사용자면 로그인/회원가입 로직 수행할 수 없게 하기
  - `계정 앱 / views.py`
  
  

## 2. login_required 데코레이터

### `login_required`

**인증된 사용자에게만 view함수를 실행**시키는 데코레이터

<aside>
💡

>> 비인증 사용자면, **/accounts/login 으로 redirect**

즉, @가 붙은 view함수는 로그인이 되야 사용가능하고, 강제로 링크로 이동하면 로그인하라고 뜸

</aside>

- 인증된 사용자만 게시글 작성/수정/삭제 가능
  
  
- 인증된 사용자만 로그아웃/탈퇴/비밀번호 변경 가능

### accounts 앱 / forms.py
```
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# django는 User 모델을 직접 참조하는 것을 권장하지 않는다.
# from .models import User
# 그래서 Django는 User 모델을 간접적으로 참조할 수 있는 방법을 별도로 제공한다.
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()


class CustomUserChangeForm(UserChangeForm):
    # password = None

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email',)
```

### accounts 앱 / urls.py
```
from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
]
```

### accounts 앱 / views.py
```
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm


# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@login_required
def logout(request):
    auth_logout(request)
    return redirect('articles:index')


def signup(request):
		# 로그인 돼 있는 경우, 소개 페이지로
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # user = form.save()
            # auth_login(request, user)  # 회원가입 후 자동 로그인
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@login_required
def delete(request):
    # 누가 요청한건지 User모델에서 검색할 필요가 없다.
    # request 객체에 요청을 보내는 user 정보가 함께 들어있기 때문.
    request.user.delete()
    return redirect('articles:index')


@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


@login_required
def change_password(request, user_pk):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # 세션 무효화 방지 // 변경 비밀번호 저장후 진행
            update_session_auth_hash(request, request.user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)
```


## is_authenticated 코드

- 메서드 x / 속성 값임!


## 회원가입 후 자동 로그인

- 회원가입 성공한 User 객체를 활용해 login 진행

## 회원 탈퇴 개선

### 탈퇴와 함께 기존 사용자 Session Data 삭제

- 사용자 객체 삭제 이후 로그아웃 함수 호출
- (1) 탈퇴 후, (2) 로그아웃 순서

>> 로그아웃을 하면 해당 요청 객체 정보가 없어지므로, 유저정보도 없어지기 때문

## PasswordChangeForm 인자 순서

- `PasswordChangeForm`는 user 객체를 첫번째 인자로 받음

>> 부모 클래스 `SetPasswordform()` 의 생성자 함수 구성을 따르기 때문
