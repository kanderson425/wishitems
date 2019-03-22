from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DeleteView
from .models import Item

# Create your views here.
def index(request):
    items = Item.objects.all()
    count = items.count()
    # id = Item.objects.get(id=item_id)
    return render(request, 'index.html', {'item_list': items, 'count': count})

class WishCreate(CreateView):
    model = Item
    fields = '__all__'
    success_url = ''

class WishDelete(DeleteView):
    model = Item
    success_url = '/'

