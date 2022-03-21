"""company2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

# from sales.views import listorders


# there is 总的路由表
urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('sales/', include('sales.url')),
                  path('api/mgr/', include('mgr.url'))
              ] + static("/", document_root="./z_dist1.5")  # 加一个路由声明和静态文件 测试
