from django.urls import path, re_path
from . import views

urlpatterns = [
    # 用户注册路由
    path('register/', views.RegisterView.as_view())
]
