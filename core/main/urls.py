from django.urls import path
from .views import index, reservation

urlpatterns = [
    path('', index, name='index'),
    path('reservation/', reservation, name='reservation')
]