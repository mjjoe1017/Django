# Django
Django for Mac OS

#Django 在Mac環境建設網站


桌面建立Django資料夾

開啟DOS

輸入 

>cd desktop cd Django

>python -m venv venv

>cd venv


>source bin/activate

>pip install django(安裝最新版本）


#安裝Django後, 在Dos輸入以下指令, 可以查看當前的Django版本

>python

>import django

>django.VERSION



#將DOS指令路徑切換到VENV路徑, 輸入以下指令建立mysite資料夾

>django-admin.py start project mysite

>cd mystie

>python manage.py runserver -h (在DOS輸入此行指令, 可查看執行web server的指令）

>python manage.py runserver

#開啟chrome

>網址輸入 http://127.0.0.1:8000/   或    輸入http://localhost:8000/

#以上步驟為Django建置Web server步驟

#
#
#修改Django Web Server網頁內容

#修改views.py檔案(路徑：desktop/django/VENV/mysite/foods/views.py）

>from django.shortcuts import render

> #Create your views here. //此行為檔案註解
>from django.http import HttpResponse

>def hello_world(request):
> 	return HttpResponse("Hello World!")



#修改urls.py檔案（路徑：desktop/django/VENV/mysite/mysite/urls.py）

>from foods.views import hello_world
>from django.conf.urls import url

>urlpatterns = [
>    url(r'^hello/$', hello_world),
>]

開啟chrome輸入網址：
http://localhost:8000/hello/

