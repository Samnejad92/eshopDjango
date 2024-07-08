from django.urls import path
from . import views

urlpatterns=[
    path('',views.products_list_view),
    path('details',views.products_detail_view),
]