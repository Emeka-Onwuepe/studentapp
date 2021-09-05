from rest_framework import routers
from django.urls import path
from knox import views as KnoxView
router = routers.DefaultRouter()
from .apis.users import LoginUser


urlpatterns = [
    path('login', LoginUser.as_view(), name="login"),
    path('logout', KnoxView.LogoutView.as_view(), name="knox_logout"),
]

urlpatterns += router.urls