from django.conf.urls import url
from . import views
urlpatterns = [
    url("Home",views.Home,name = "Home")
]
