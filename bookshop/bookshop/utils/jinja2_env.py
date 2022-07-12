from jinja2 import Environment
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse


def jinja2_environment(**options):
    """jinja2的环境"""

    # 创建环境对象
    env = Environment(**options)

    # 自定义模板语法:{{ static("静态文件路径") }} {{ url("路由的命名空间") }}
    env.globals.update({
        "static": staticfiles_storage.url,  # 获取静态文件前缀
        "url": reverse  # 反向解析路由名
    })
    # 返回环境对象
    return env
