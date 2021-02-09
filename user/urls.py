from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="user-home"),
    path('product', views.product, name="user-product"),
    path('packages', views.packages, name="user-packages"),
    path('aboutUs', views.aboutUs, name="user-about-us"),
    path('gallary', views.gallary, name="user-gallary"),
    path('feedback', views.feedback, name="user-feedback"),
    path('login', views.loginPage, name="user-login"),
    path('register', views.registerPage, name="user-register"),
]