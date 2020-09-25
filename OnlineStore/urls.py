"""OnlineStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path, re_path
from users import views
from Product import views as tru
from users.views import ProfilePage, RegisterView, LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login', LoginView.as_view(), name="login"),
    path('accounts/profile', ProfilePage.as_view(), name="profile"),
    path('accounts/register', RegisterView.as_view(), name="register"),
    path('logout',LogoutView.as_view(next_page='/'), name='logout'),
    path('', views.index),
    path('Product/', tru.Goods, name="Product"),
    re_path(r'^Product/create', tru.create, name="create_Product"),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    path('Product/edit/<int:id>/', tru.edit),
    path('Product/delete/<int:id>/', tru.delete),
    url(r'^(?P<id>\d+)/',
        tru.product_detail,
        name='product_detail'),

    ]
