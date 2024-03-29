"""pybursa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from .views import *



urlpatterns = [
    #url(r'^$', index, name='index'),
    #url(r'^contact/$', contact, name='contact'),
    #url(r'^polls/', include('polls.urls')),
	#url(r'^student_list/$', views.student_list, name='student_list'),
	#url(r'^student_detail/$', views.student_detail, name='student_detail'),
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^courses/', include('courses.urls')),
    url(r'^students/', include('students.urls', namespace="students")),
    url(r'^contact/$', contact, name='contact'),
	url(r'^quadratic/', include('quadratic.urls')),
   	url(r'^coaches/', include('coaches.urls')),
	url(r'^feedback/', include('feedbacks.urls')),
	
	
]

