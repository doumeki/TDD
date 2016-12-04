"""superlists URL Configuration

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
import lists.views

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    # url(r'^aio$',lists.views.other_page),
    url(r'^$',lists.views.home_page), #新方法不用引号了，写上的参考过时了
    # url(r'^lists/(.+)/$',lists.views.view_list,name='view_lists'), #可通过group传递参数
    url(r'^lists/(\d+)/$',lists.views.view_list,name='view_lists'), #可通过group传递参数
    url(r'^lists/(\d+)/add_item$',lists.views.add_item,name='add_item'), #可通过group传递参数
    url(r'^lists/new$',lists.views.new_list,name='new_list'),


]
