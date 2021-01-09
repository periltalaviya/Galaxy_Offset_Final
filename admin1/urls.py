from django.urls import path

from admin1 import views

urlpatterns = [
    path('', views.index, name="admin-home"),

    path('gallary/', views.gallary, name="admin-gallary"),
    path('gallary_show1/<int:id>', views.gallary_show1, name="admin-gallary-show1"),
    path('gallary_delete/<int:id>', views.gallary_delete, name="admin-gallary-delete"),
    path('gallary_edit/<int:id>', views.gallary_edit, name="admin-gallary-edit"),

    path('adduser/', views.addUser, name="admin-add-user"),
    path('order/', views.order, name="admin-order"),
    path('payment/', views.payment, name="admin-payment"),

    path('feedback/', views.feedback, name="admin-feedback"),
    path('feedback_delete/<int:id>', views.feedback, name="admin-feedback-delete"),

    path('viewprofile/', views.viewProfile, name="admin-view-profile"),

    path('product/', views.product, name="admin-product"),
    path('product_edit/<int:id>', views.product_edit, name="admin-product-edit"),
    path('product_show1/<int:id>', views.product_show1, name="admin-product-show1"),
    path('product_delete/<int:id>', views.product_delete, name="admin-product-delete"),

    path('productSize/', views.size, name="admin-product-size"),
    path('size_delete/<int:id>', views.size_delete, name="admin-product-size-delete"),
    path('size_edit/<int:id>', views.size_edit, name="admin-product-size-edit"),
    path('size_data_update/<int:id>', views.size_edit_update, name="admin-product-size-edit-update"),

    path('productColor/', views.color, name="admin-color-options"),
    path('color_delete/<int:id>', views.color_delete, name="admin-product-color-delete"),
    path('color_edit/<int:id>', views.color_edit, name="admin-product-color-edit"),
    path('color_data_update/<int:id>', views.color_edit_update, name="admin-product-color-edit-update"),

    path('templateImage/', views.templateImage, name="admin-template-image"),
    path('templateImage_show1/<int:id>', views.templateImage_show1, name="admin-template-image-show1"),
    path('templateImage_delete/<int:id>', views.templateImage_delete, name="admin-template-image-delete"),
    path('templateImage_edit/<int:id>', views.templateImage_edit, name="admin-template-image-edit"),

    path('paperChoice/', views.paperChoice, name="admin-paper-choice"),
    path('paperChoice_delete/<int:id>', views.paperChoice_delete, name="admin-paper-choice-delete"),
    path('paperChoice_edit/<int:id>', views.paperChoice_edit, name="admin-paper-choice-edit"),
    path('paperChoice_data_update/<int:id>', views.paperChoice_edit_update, name="admin-paper-choice-edit-update"),
]
