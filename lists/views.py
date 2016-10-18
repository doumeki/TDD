from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# home_page = None
def home_page(req):
    return render(req,'home.html') #自动搜索Templates下的html文件
