from django.conf.urls import url
from . import views

app_name = 'shop'

urlpatterns = [
    #url(r'^$', views.ShopItemsList.as_view(), name='itemlist'),
    url(r'^$', views.shop_items_list, name='itemlist'),
]