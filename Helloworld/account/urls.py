from django.conf.urls import url
from . import views

from django.conf import settings

from django.contrib.auth import views as auth_views  # 为了使用内置的登陆方法，导入了Django内置视图文件

# from blog.views import blog_title, blog_article

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    # url(r'^login/$', views.user_login, name='user_login'),  # 自定义的登录
    url(r'^login/$', auth_views.login, name='user_login'),  # django内置登录
    # 以一个字典类型，向默认的auth_views.login传template_name的值
    url(r'new-login/$', auth_views.login, {'template_name': 'account/login.html'}),  # django内置登陆方法2
]
