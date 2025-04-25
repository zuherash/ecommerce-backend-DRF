from django.urls import path
from .views import RigesterView
urlpatterns = [
    path("register/", RigesterView.as_view(), name="Register")
]
