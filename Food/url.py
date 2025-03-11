from . import views
from django.urls import path

app_name = 'food'

urlpatterns = [
   #/food/
   #path('', views.index, name='index'), #method

   path('', views.IndexClassView.as_view(), name='index'), #class based view


   path("item/",views.item, name='item'),

   #/food/1
   #path("<int:item_id>/", views.details, name='details'),

   path("<int:pk>/", views.FoodDetail.as_view(), name='details'),

   #path("add" , views.add_item , name='add_item'),

   path("add/" , views.Add_Item.as_view() , name='add_item'),


   path("update/<int:item_id>/", views.update_item , name='update'),

   path("delete/<int:item_id>/", views.delete_item , name='delete'),

]