from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="user-home"),
    path('product', views.product, name="user-product"),
    path('order/<int:id>', views.order, name="product"),
    path('packages', views.packages, name="user-packages"),
    path('aboutUs', views.aboutUs, name="user-about-us"),
    path('gallary', views.gallary, name="user-gallary"),
    path('feedback', views.feedback, name="user-feedback"),
    path('login', views.loginPage, name="user-login"),
    path('logout/', views.logoutUser, name="user-logout"),
    path('register', views.registerPage, name="user-register"),
    path('product_show1/<int:id>', views.product_show1, name="user-product-show1"),
]