from django.urls import path
from . import views

urlpatterns = [
    path('data',views.data_page),
    path('test',views.test_page)
]