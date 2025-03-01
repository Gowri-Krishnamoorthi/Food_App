from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Item
from django.template import loader

def index(request):
    item_list = Item.objects.all()
    #return HttpResponse("Hello World")
    #template = loader.get_template('food/index.html')
    context = {
        'item_list' : item_list,
    }
    #return HttpResponse(item_list)
    #return HttpResponse (template.render(context,request))
    return render(request,'food/index.html',context)

def item(request):
    return HttpResponse("<h1>This is an item view<h2>")

def details(request,item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item' : item,
    }
    #return HttpResponse("This is item id no/id: %s" % item_id)
    return render(request , 'food/details.html' , context)