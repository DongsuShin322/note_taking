Django Study



1. 가상환경 생성

```
conda create -n django python=3.6
source activate django
```

2. 장고설치

```
pip install django~=1.11.0
```

3. 프로젝트 생성

```
mkdir django
cd django
django-admin startproject PROJECT_NAME .
```

4. 앱 생성(의미있는 하나의 기능 ex. blog, bulletin board)

```
./manage.py startapp APP_NAME

-- 앱 생성 후 setting.py 의 INSTALLED_APPS 에 추가(등록) 필요 --
<PROJECT_NAME/settings.py>
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'community',
]
```

5. 모델 생성 - 현재 DB가 없으므로 우선 생성

```
./manage.py migrate
```

6. 슈퍼유저 생성

```
./manage.py createsuperuser
```

7. 모델 생성

```
기본적으로 Class로 생성
<APP_NAME/models.py>
class Article(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    contents = models.TextField()
    url = models.URLField()
    email = models.EmailField()
    cdate = models.DateTimeField(auto_now_add=True)

./manage.py makemigrations APP_NAME -- 해당 앱의 변화가 있는 지를 확인
./manage.py migrate -- 실제 DB 에 적용(테이블 생성)
```

8. URL 설정

```
사용자들이 url에 접근할 수 있는 주소
<PROJECT_NAME/urls.py>
from APP_NAME.views import *
url(r'^write/', write, name='write') : write라는 함수로 url이 전달

<APP_NAME/views.py>
def write(request):
	return render(request, 'write.html') : request를 template에 전달
	
**rendering : 현재와 다른 어떤 상태로 만듦 - HTML로 쓰인 것을 모니터로 출력

APP_NAME/templates/write.html 디렉토리 및 파일 생성
<write.html>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>write</title>
</head>
<body>
  hello django!
</body>
</html>
```

9. HTML에서 FORM 사용하기

```
APP_NAME/forms.py 파일 생성
<forms.py>
from django.forms import ModelForm
from community.models import *

class Form(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'title', 'contents', 'url', 'email']
        
<views.py>
from django.shortcuts import render
from community.forms import *

def write(request):
    form = Form()
	return render(request, 'write.html', {'form':form})
	
<write.html>	
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>write</title>
</head>
<body>
  <form action="" method="post">
    {{ form.as_p }}
    <button type="submit" class="btn btn.primary">저장</button>
  </form>
</body>
</html>	
```

**************************************************************

- 정리

  1. DB 와 데이터 주고 받을 모델 생성 (models.py)

  2. 특정 작성 form 필요 시 APP_NAME/forms.py 생성

  3. 새로운 URL 페이지를 생성할 때마다 urls.py 의 urlpatterns 에 추가

  4. 특정 url 이 특정 함수 호출 --> views.py 에서 새로운 함수 정의

     render('새로운 html', {함께 넘겨줄 인자})

  5. 호출될 html 파일 작성 (APP_NAME/templates/*.html)

