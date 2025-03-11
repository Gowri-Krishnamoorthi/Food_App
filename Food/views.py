from django.shortcuts import get_object_or_404, render , redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
# Create your views here.
from .models import Item
from django.template import loader
from .form import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# def index(request):
#     item_list = Item.objects.all()
#     #return HttpResponse("Hello World")
#     #template = loader.get_template('food/index.html')
#     context = {
#         'item_list' : item_list,
#     }
#     #return HttpResponse(item_list)
#     #return HttpResponse (template.render(context,request))
#     return render(request,'food/index.html',context)

class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'

def item(request):
    return HttpResponse("<h1>This is an item view<h2>")

# def details(request,item_id):
#     item = Item.objects.get(pk=item_id)
#     context = {
#         'item' : item,
#     }
#     #return HttpResponse("This is item id no/id: %s" % item_id)
#     return render(request , 'food/details.html' , context)

class FoodDetail(DetailView):
    model = Item
    template_name = 'food/details.html'
    #context_object_name = 'item'

def add_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request, 'food/add_item.html', {'form' : form})

class Add_Item(CreateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    template_name = 'food/add_item.html'
    success_url = reverse_lazy('food:index')  # Redirect to a valid page after submission

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)


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
    