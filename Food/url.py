from . import views
from django.urls import path

urlpatterns = [
   #/food/
   path('', views.index, name='index'),
   path("item/",views.item, name='item'),

   #/food/1
   path("<int:item_id>/", views.details, name='details'),
]