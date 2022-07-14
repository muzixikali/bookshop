from django.shortcuts import render
from django.views import View  # 导入视图根类


# Create your views here.
class RegisterView(View):
    """用户注册视图"""

    def get(self, request):
        """get请求-->提供注册页面"""
        return render(request, 'register.html')

    def post(self, request):
        """post请求-->实现注册逻辑"""
        pass
