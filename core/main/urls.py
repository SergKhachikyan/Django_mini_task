from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('products/<int:id>/',views.product, name='products')
]