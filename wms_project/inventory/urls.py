from django.urls import path
from .views import inventory_view, sell_item, add_item

urlpatterns = [
    path('', inventory_view, name='inventory_view'),
    path('sell/<int:item_id>/', sell_item, name='sell_item'),
    path('add/', add_item, name='add_item'),
]