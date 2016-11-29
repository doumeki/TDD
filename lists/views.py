from django.shortcuts import render,redirect
from django.http import HttpResponse
from lists.models import Item

# Create your views here.

# home_page = None
def home_page(req):
    '''if req.method == 'POST':
        return HttpResponse(req.POST['item_text'])
    return render(req,'home.html') #自动搜索Templates下的html文件'''
    # return render(req,'home.html',{'new_item_text':req.POST.get('item_text','')})
    # item = Item()
    # item.text = req.POST.get('item_text','')
    # item.save()
    #
    # return render(req, 'home.html', {'new_item_text': item.text})
    if req.method == 'POST':
        new_item_text = req.POST['item_text']
        Item.objects.create(text = new_item_text) #不用实例化再save
        print ('second')
        return redirect('/') #先redirect 到/ ,再回到这个方法上来。但并不是POST
    items = Item.objects.all()
    print ('first in here')
    return render(req, 'home.html',{"items":items})

#自行添加的方法，第六章并没有提到自定义URL
#只是为了验证URL direct后的方式，正如注释所写的，先direct, 再回到home_page方法上去。
def other_page(req):
    print ('only here')
    items = Item.objects.all()
    return render(req,'home.html',{"items":items})