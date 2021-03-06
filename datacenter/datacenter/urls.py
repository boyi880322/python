"""datacenter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mysite import views
from mysite.views import homepage,lotto,CHexport,index,showpost,chart,mychart,mychart1,mychart2,test,money
urlpatterns = [
    path('post/<str:slug>/',showpost),
	path('',homepage),
    path('admin/', admin.site.urls),
    path('lotto/',lotto),
    path('index/',index),
    path('mychart/',mychart),
    path('mychart/<int:bid>/',mychart),
    path('mychart1/<int:bid>/',mychart),
    path('mychart2/<int:bid>/',mychart),
    path('mychartdate/<int:year>/<int:month>/',chart),
    path('mychartdate/<int:year>/',chart),
    path( 'test/',test),
    path( 'money/',money),
    path('CHexport/',CHexport),

]
