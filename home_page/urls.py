from django.urls import path
from .views import predict_heart as index  

urlpatterns = [
    path("", index, name="predict"),
]