"""nano URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from app01 import views
from wordapp import views1
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^home/$",views.homepage),
    url(r"^add/",views.add_img,name='add'),
    url(r"^home/delete/",views.delete_img,name='delete'),
    url(r"^home1/$",views.home1),
    url(r"^word/$",views.word),
    url(r"^downloadfind/$",views.download_find),
    url(r"^downloadfind/find",views.download_find1,name='find'),
    url(r"^downloadfind/download/(?P<src>.*)",views.download_resume_appendix,name='download'),

    url(r'^wordlist/',views1.wordlist),
    url(r'^detailword/(?P<id>.*)/',views1.detailword),
    url(r'^redetailword/(?P<id>.*)/',views1.redetailword),
    url(r'^change/',views1.change)
]
