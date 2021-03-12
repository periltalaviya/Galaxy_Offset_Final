from django.urls import path

from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name="user-home"),
    path('product', views.product, name="user-product"),
    path('order/<int:id>', views.order, name="user-order"),
    path('packages/<int:id>', views.packages, name="user-packages"),
    path('aboutUs', views.aboutUs, name="user-about-us"),
    path('gallary', views.gallary, name="user-gallary"),
    path('contactUs', views.contactUs, name="user-contact-us"),
    path('login', views.loginPage, name="user-login"),
    path('logout/', views.logoutUser, name="user-logout"),
    path('register', views.registerPage, name="user-register"),
    path('product_show1/<int:id>', views.product_show1, name="user-product-show1"),
    path('viewProfile/', views.viewProfile, name="user-view-profile"),
    path('editProfile/', views.editProfile, name="user-edit-profile"),
    path('changePassword/', views.changePassword, name='user-change-password'),

    path("password-reset/", auth_views.PasswordResetView.as_view(template_name='Account/password_reset.html'),
         name="password_reset")
]
