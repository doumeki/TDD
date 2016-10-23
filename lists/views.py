from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# home_page = None
def home_page(req):
    '''if req.method == 'POST':
        return HttpResponse(req.POST['item_text'])
    return render(req,'home.html') #自动搜索Templates下的html文件'''
    return render(req,'home.html',{'new_item_text':req.POST.get('item_text','')})