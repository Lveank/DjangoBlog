"""Helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from blog.views import blog_title, blog_article, index
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', index, name='index'),  # 这是为了测试用的index，视图写在blog里。注意没有name=some-url-name写模板时会匹配不到
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls', namespace='blog', app_name='blog')),
    url(r'^account/', include('account.urls', namespace='account', app_name='account')),
    url(r'^pwd_reset/', include('password_reset.urls', namespace='pwd_reset', app_name='pwd_reset')),
    url(r'^article/', include('article.urls', namespace='article', app_name='article')),
    # 使用通用视图制作homepage（不用自己写视图函数）
    url(r'^home/', TemplateView.as_view(template_name='home.html')),
]
