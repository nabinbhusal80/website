"""website URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from kanchanpur import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home_view,name="homepage"),
    url(r'^news$',views.news_view,name="news"),
    url(r'^team$',views.team_view,name="team"),
    url(r'^developer$',views.developer_view,name='developer'),
    url(r'^ticket$',views.ticket_view,name='ticket'),
    url(r'^gallary$',views.gallary_view,name='gallary'),
    url(r'^about$',views.about_view,name='about'),
    url(r'^sponsor$',views.sponsor_view,name='sponsor'),


]
