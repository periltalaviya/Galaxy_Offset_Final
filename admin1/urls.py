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

    path('holeDrilling/', views.holeDrilling, name="admin-hole-drilling"),
    path('holeDrilling_delete/<int:id>', views.holeDrilling_delete, name="admin-hole-drilling-delete"),
    path('holeDrilling_edit/<int:id>', views.holeDrilling_edit, name="admin-hole-drilling-edit"),
    path('holeDrilling_data_update/<int:id>', views.holeDrilling_edit_update,
         name="admin-hole-drilling-edit-update"),

    path('bindingMethod/', views.bindingMethod, name="admin-binding-method"),
    path('bindingMethod_delete/<int:id>', views.bindingMethod_delete, name="admin-binding-method-delete"),
    path('bindingMethod_edit/<int:id>', views.bindingMethod_edit, name="admin-binding-method-edit"),
    path('bindingMethod_data_update/<int:id>', views.bindingMethod_edit_update,
         name="admin-binding-method-edit-update"),

]
