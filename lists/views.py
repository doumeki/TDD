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
        return redirect('/')
    items = Item.objects.all()
    return render(req, 'home.html',{"items":items})