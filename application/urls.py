from django.contrib import admin
from django.urls import path, include
from rest_framework.urls import app_name

from application import views

app_name='cart'

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.store,name='store'),
    path('basket',views.basket,name='basket'),
    path('cart/',views.view_cart,name='view_cart'),
    path('add/<int:shop_id>',views.add_cart,name='add_cart'),
    path('delete/<int:shop_id>/',views.delete_cart,name='delete_cart'),

]
