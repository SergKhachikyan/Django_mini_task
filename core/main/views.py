from django.shortcuts import render
from .models import Category,Product

def index(request):
    category_list = Category.objects.all()
    return render(request,'index.html',context={
        'category_list':category_list
    })
    
def product(request,id):
    product_list = Product.objects.filter(category_id = id)
    return render(request,'products.html',context={
        'product_list':product_list
    })