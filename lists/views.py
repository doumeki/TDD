from django.shortcuts import render,redirect
from django.http import HttpResponse
from lists.models import Item,List

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
        return redirect('/lists/the-only-list-in-the-world') #先redirect 到/ ,再回到这个方法上来。但并不是POST
    return render(req,'home.html')

#自行添加的方法，第六章并没有提到自定义URL
#只是为了验证URL direct后的方式，正如注释所写的，先direct, 再回到home_page方法上去。
def other_page(req):
    print ('only here')
    items = Item.objects.all()
    return render(req,'home.html',{"items":items})

def view_list(req,list_id):
    list_ = List.objects.get(id = list_id) # 要加上id = list_id才行，要不然不能GET到数据
    items = Item.objects.filter(list = list_) #查找
    return render(req,'list.html',{'list':list_})

def new_list(req):
    list_ = List.objects.create()
    Item.objects.create(text = req.POST['item_text'],list = list_)
    return redirect('/lists/%d/'%(list_.id,))

def add_item(req,list_id):
    list_ = List.objects.get(id = list_id)
    Item.objects.create(text = req.POST['item_text'],list = list_)
    return redirect('/lists/%d/'%(list_.id))
