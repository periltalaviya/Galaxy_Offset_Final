from django.contrib.auth import views as auth_views
from django.urls import path

from admin1 import views

urlpatterns = [
    path('', views.index, name="admin-home"),

    path('login/', views.loginPage, name="admin-login"),
    path('logout/', views.logoutUser, name="admin-logout"),

    path("password-reset/", auth_views.PasswordResetView.as_view(template_name='admin1/password_reset.html'),
         name="password_reset"),
    path("password-reset/done/",
         auth_views.PasswordResetDoneView.as_view(template_name='admin1/password_reset_done.html'),
         name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/",
         auth_views.PasswordResetConfirmView.as_view(template_name='admin1/password_reset_confirm.html'),
         name="password_reset_confirm"),
    path("password-reset-complete/",
         auth_views.PasswordResetCompleteView.as_view(template_name='admin1/password_reset_complete.html'),
         name="password_reset_complete"),

    path('gallary/', views.gallary, name="admin-gallary"),
    path('gallary_show1/<int:id>', views.gallary_show1, name="admin-gallary-show1"),
    path('gallary_delete/<int:id>', views.gallary_delete, name="admin-gallary-delete"),
    path('gallary_edit/<int:id>', views.gallary_edit, name="admin-gallary-edit"),

    path('addUser/', views.addUser, name="admin-add-user"),
    path('addUser_delete/<int:id>', views.addUser_delete, name="admin-add-user-delete"),
    path('addUser_edit/<int:id>', views.addUser_edit, name="admin-add-user-edit"),
    path('addUser_show1/<int:id>', views.addUser_show1, name="admin-add-user-show1"),

    path('order/', views.order, name="admin-order"),
    path('order_delete/<int:id>', views.order_delete, name="admin-order-delete"),
    path('order_edit/<int:id>', views.order_edit, name="admin-order-edit"),
    path('order_show1/<int:id>', views.order_show1, name="admin-order-show1"),

    path('payment/', views.payment, name="admin-payment"),

    path('packages/', views.packages, name="admin-packages"),
    path('packages_delete/<int:id>', views.packages_delete, name="admin-packages-delete"),
    path('packages_edit/<int:id>', views.packages_edit, name="admin-packages-edit"),
    path('packages_show1/<int:id>', views.packages_show1, name="admin-packages-show1"),

    path('feedback/', views.feedback, name="admin-feedback"),
    path('feedback_delete/<int:id>', views.feedback, name="admin-feedback-delete"),
    path('feedback_show/<int:id>', views.feedback_show1, name="admin-feedback-show1"),

    path('viewProfile/', views.viewProfile, name="admin-view-profile"),
    path('editProfile/', views.editProfile, name="admin-edit-profile"),
    path('changePassword/', views.changePassword, name='admin-change-password'),

    path('product/', views.product, name="admin-product"),
    path('product_edit/<int:id>', views.product_edit, name="admin-product-edit"),
    path('product_show1/<int:id>', views.product_show1, name="admin-product-show1"),
    path('product_delete/<int:id>', views.product_delete, name="admin-product-delete"),

    path('productSize/', views.size, name="admin-product-size"),
    path('size_delete/<int:id>', views.size_delete, name="admin-product-size-delete"),
    path('size_edit/<int:id>', views.size_edit, name="admin-product-size-edit"),
    path('size_data_update/<int:id>', views.size_edit_update, name="admin-product-size-edit-update"),

    path('sizeProductMap/', views.sizeProductMap, name="admin-size-product-map"),
    path('sizeProductMap_delete/<int:id>', views.sizeProductMap_delete, name="admin-size-product-map-delete"),
    path('sizeProductMap_edit/<int:id>', views.sizeProductMap_edit, name="admin-size-product-map-edit"),

    path('productColor/', views.color, name="admin-color-options"),
    path('color_delete/<int:id>', views.color_delete, name="admin-product-color-delete"),
    path('color_edit/<int:id>', views.color_edit, name="admin-product-color-edit"),
    path('color_data_update/<int:id>', views.color_edit_update, name="admin-product-color-edit-update"),

    path('colorProductMap/', views.colorProductMap, name="admin-color-product-map"),
    path('colorProductMap_delete/<int:id>', views.colorProductMap_delete, name="admin-color-product-map-delete"),
    path('colorProductMap_edit/<int:id>', views.colorProductMap_edit, name="admin-color-product-map-edit"),

    path('templateImage/', views.templateImage, name="admin-template-image"),
    path('templateImage_show1/<int:id>', views.templateImage_show1, name="admin-template-image-show1"),
    path('templateImage_delete/<int:id>', views.templateImage_delete, name="admin-template-image-delete"),
    path('templateImage_edit/<int:id>', views.templateImage_edit, name="admin-template-image-edit"),

    path('imageTempProductMap/', views.imageTempProductMap, name="admin-image-template-product-map"),
    path('imageTempProductMap_delete/<int:id>', views.imageTempProductMap_delete,
         name="admin-image-template-product-map-delete"),
    path('imageTempProductMap_edit/<int:id>', views.imageTempProductMap_edit,
         name="admin-image-template-product-map-edit"),

    path('paperChoice/', views.paperChoice, name="admin-paper-choice"),
    path('paperChoice_delete/<int:id>', views.paperChoice_delete, name="admin-paper-choice-delete"),
    path('paperChoice_edit/<int:id>', views.paperChoice_edit, name="admin-paper-choice-edit"),
    path('paperChoice_data_update/<int:id>', views.paperChoice_edit_update, name="admin-paper-choice-edit-update"),

    path('paperProductMap/', views.paperProductMap, name="admin-paper-product-map"),
    path('paperProductMap_delete/<int:id>', views.paperProductMap_delete, name="admin-paper-product-map-delete"),
    path('paperProductMap_edit/<int:id>', views.paperProductMap_edit, name="admin-paper-product-map-edit"),

    path('shrinkWrapping/', views.shrinkWrapping, name="admin-shrink-wrapping"),
    path('shrinkWrapping_delete/<int:id>', views.shrinkWrapping_delete, name="admin-shrink-wrapping-delete"),
    path('shrinkWrapping_edit/<int:id>', views.shrinkWrapping_edit, name="admin-shrink-wrapping-edit"),
    path('shrinkWrapping_data_update/<int:id>', views.shrinkWrapping_edit_update,
         name="admin-shrink-wrapping-edit-update"),

    path('shrinkWrappingProductMap/', views.shrinkWrappingProductMap, name="admin-shrink-wrapping-product-map"),
    path('shrinkWrappingProductMap_delete/<int:id>', views.shrinkWrappingProductMap_delete,
         name="admin-shrink-wrapping-product-map-delete"),
    path('shrinkWrappingProductMap_edit/<int:id>', views.shrinkWrappingProductMap_edit,
         name="admin-shrink-wrapping-product-map-edit"),

    path('foldingOption/', views.foldingOption, name="admin-folding-option"),
    path('foldingOption_delete/<int:id>', views.foldingOption_delete, name="admin-folding-option-delete"),
    path('foldingOption_edit/<int:id>', views.foldingOption_edit, name="admin-folding-option-edit"),
    path('foldingOption_data_update/<int:id>', views.foldingOption_edit_update,
         name="admin-folding-option-edit-update"),

    path('foldingOptionProductMap/', views.foldingOptionProductMap, name="admin-folding-option-product-map"),
    path('foldingOptionProductMap_delete/<int:id>', views.foldingOptionProductMap_delete,
         name="admin-folding-option-product-map-delete"),
    path('foldingOptionProductMap_edit/<int:id>', views.foldingOptionProductMap_edit,
         name="admin-folding-option-product-map-edit"),

    path('aqutousCoating/', views.aqutousCoating, name="admin-aqutous-coating"),
    path('aqutousCoating_delete/<int:id>', views.aqutousCoating_delete, name="admin-aqutous-coating-delete"),
    path('aqutousCoating_edit/<int:id>', views.aqutousCoating_edit, name="admin-aqutous-coating-edit"),
    path('aqutousCoating_data_update/<int:id>', views.aqutousCoating_edit_update,
         name="admin-aqutous-coating-edit-update"),

    path('aqutousCoatingProductMap/', views.aqutousCoatingProductMap, name="admin-aqutous-coating-product-map"),
    path('aqutousCoatingProductMap_delete/<int:id>', views.aqutousCoatingProductMap_delete,
         name="admin-aqutous-coating-product-map-delete"),
    path('aqutousCoatingProductMap_edit/<int:id>', views.aqutousCoatingProductMap_edit,
         name="admin-aqutous-coating-product-map-edit"),

    path('noOfMonths/', views.noOfMonths, name="admin-no-of-months"),
    path('noOfMonths_delete/<int:id>', views.noOfMonths_delete, name="admin-no-of-months-delete"),
    path('noOfMonths_edit/<int:id>', views.noOfMonths_edit, name="admin-no-of-months-edit"),
    path('noOfMonths_data_update/<int:id>', views.noOfMonths_edit_update,
         name="admin-no-of-months-edit-update"),

    path('noOfMonthsProductMap/', views.noOfMonthsProductMap, name="admin-no-of-months-product-map"),
    path('noOfMonthsProductMap_delete/<int:id>', views.noOfMonthsProductMap_delete,
         name="admin-no-of-months-product-map-delete"),
    path('noOfMonthsProductMap_edit/<int:id>', views.noOfMonthsProductMap_edit,
         name="admin-no-of-months-product-map-edit"),

    path('holeDrilling/', views.holeDrilling, name="admin-hole-drilling"),
    path('holeDrilling_delete/<int:id>', views.holeDrilling_delete, name="admin-hole-drilling-delete"),
    path('holeDrilling_edit/<int:id>', views.holeDrilling_edit, name="admin-hole-drilling-edit"),

    path('holeDrillingProductMap/', views.holeDrillingProductMap, name="admin-hole-drilling-product-map"),
    path('holeDrillingProductMap_delete/<int:id>', views.holeDrillingProductMap_delete,
         name="admin-hole-drilling-product-map-delete"),
    path('holeDrillingProductMap_edit/<int:id>', views.holeDrillingProductMap_edit,
         name="admin-hole-drilling-product-map-edit"),

    path('bindingMethod/', views.bindingMethod, name="admin-binding-method"),
    path('bindingMethod_delete/<int:id>', views.bindingMethod_delete, name="admin-binding-method-delete"),
    path('bindingMethod_edit/<int:id>', views.bindingMethod_edit, name="admin-binding-method-edit"),
    path('bindingMethod_data_update/<int:id>', views.bindingMethod_edit_update,
         name="admin-binding-method-edit-update"),

    path('bindingMethodProductMap/', views.bindingMethodProductMap, name="admin-binding-method-product-map"),
    path('bindingMethodProductMap_delete/<int:id>', views.bindingMethodProductMap_delete,
         name="admin-binding-method-product-map-delete"),
    path('bindingMethodProductMap_edit/<int:id>', views.bindingMethodProductMap_edit,
         name="admin-binding-method-product-map-edit"),

]
