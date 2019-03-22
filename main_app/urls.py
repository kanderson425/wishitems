from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('items/add/', views.WishCreate.as_view(), name='add_wish'),
    path('items/<int:pk>/delete/', views.WishDelete.as_view(), name='delete_wish'),
    
]