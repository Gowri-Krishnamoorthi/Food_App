from django.shortcuts import get_object_or_404, render , redirect
from django.http import HttpResponse
# Create your views here.
from .models import Item
from django.template import loader
from .form import ItemForm

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

def add_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request, 'food/add_item.html', {'form' : form})

def update_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)  # This prevents DoesNotExist error
    form = ItemForm(request.POST or None, instance=item)  # Pre-fill the form

    if form.is_valid():
        form.save()
        return redirect('food:index')  # Redirect to index after updating

    return render(request, 'food/add_item.html', {'form': form, 'item': item})  # Use a proper template

def delete_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    
    return render(request,'food/delete_item.html', {'item':item})
    