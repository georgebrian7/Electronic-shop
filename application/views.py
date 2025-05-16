from django.shortcuts import render, redirect
from .models import Shop,ShopItem
# Create your views here.

def store(request):
    shops = Shop.objects.all()
    return render(request, 'store.html', {'shops': shops})
def basket(request):
    shop_items = ShopItem.objects.all()
    return render(request, 'basket.html', {'shop_items': shop_items})
def view_cart(request):
    if not request.session.session_key:
        request.session.create()
    shop_items = ShopItem.objects.filter(session_key=request.session.session_key)
    total_price = sum(item.shop.price * item.quantity for item in shop_items)

    return render(request, 'basket.html', {'shop_items': shop_items, 'total_price': total_price})

def add_cart(request, shop_id):
    shop = Shop.objects.get(id=shop_id)
    if not request.session.session_key:
        request.session.create()
    shop_item, created = ShopItem.objects.get_or_create(shop=shop, session_key=request.session.session_key)
    shop_item.quantity += 1
    shop_item.save()
    return redirect('cart:view_cart')

def delete_cart(request, shop_id):
    shop = Shop.objects.get(id=shop_id)
    Shop.objects.filter(shop=shop, session_key=request.session.session_key).delete()
    return redirect('cart:view_cart')
