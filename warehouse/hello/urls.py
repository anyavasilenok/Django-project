from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('add_storage', views.add_storage, name="add_storage"),
    path('show_storage', views.show_storage, name="show_storage"),
    path('edit', views.edit, name="edit"),
    path('edit_storage', views.edit_storage, name="edit_storage"),
    path('delete_storage', views.delete_storage, name="delete_storage"),
    path('find_storage', views.find_storage, name="find_storage"),
    path('find_2_storage', views.find_2_storage, name="find_2_storage"),
    path('edit_inventory', views.edit_inventory, name="edit_inventory"),
    path('delete_inventory', views.delete_inventory, name="delete_inventory"),
    path('find_inventory', views.find_inventory, name="find_inventory"),
    path('find_2_inventory', views.find_2_inventory, name="find_2_inventory"),
    path('add_inventory', views.add_inventory, name="add_inventory"),
    path('search', views.search, name="search"),
    path('search_list', views.search_list, name="search_list"),
    path('search_2_list', views.search_2_list, name="search_2_list"),
    path('search_inventory', views.search_inventory, name="search_inventory"),
    path('search_2_inventory', views.search_2_inventory, name="search_2_inventory"),
    path('edit_2', views.edit_2, name="edit_2"),
    path('edit_salesinvoice', views.edit_salesinvoice, name="edit_salesinvoice"),
    path('edit_packinglist', views.edit_packinglist, name="edit_packinglist"),
    path('add_packinglist', views.add_packinglist, name="add_packinglist"),
    path('delete_packinglist', views.delete_packinglist, name="delete_packinglist"),
    path('find_packinglist', views.find_packinglist, name="find_packinglist"),
    path('find_2_packinglist', views.find_2_packinglist, name="find_2_packinglist"),
    path('add_salesinvoice', views.add_salesinvoice, name="add_salesinvoice"),
    path('delete_salesinvoice', views.delete_salesinvoice, name="delete_salesinvoice"),
    path('find_salesinvoice', views.find_salesinvoice, name="find_salesinvoice"),
    path('find_2_salesinvoice', views.find_2_salesinvoice, name="find_2_salesinvoice")
]
