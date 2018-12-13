from django.urls import path, include
from rest_framework import routers
from .user.views import UserView
from .login.views import LoginView

router = routers.DefaultRouter()
router.register(r'user',UserView, base_name='user')
router.register(r'login', LoginView, base_name='login')

urlpatterns = [
    path('',include(router.urls))
]