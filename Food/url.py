from . import views
from django.urls import path

app_name = 'food'

urlpatterns = [
   #/food/
   path('', views.index, name='index'),
   path("item/",views.item, name='item'),

   #/food/1
   path("<int:item_id>/", views.details, name='details'),

   path("add" , views.add_item , name='add_item'),

   path("update/<int:item_id>/", views.update_item , name='update')
]