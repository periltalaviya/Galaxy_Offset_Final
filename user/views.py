from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect

from .forms import CreateUserForm
from .models import *


# Create your views here.

def index(request):
    return render(request, 'user/index.html')


def product(request):
    product_list = Product.objects.all()
    context = {
        'product_list': product_list,
    }
    return render(request, 'user/product.html', context)


def product_show1(request, id):
    ImageTemplateProductsList = []
    product_detail = Product.objects.filter(prod_ID=id)
    try:
        ImageTemplateProductsMap = ImageTemplateProductMapping.objects.filter(prod_id=id)
        ImageTemplateProductsList = [data.temp_id.temp_img for data in
                                     ImageTemplateProductsMap]
    except AttributeError:
        pass

    return render(request, 'user/product.html',
                  {'product_detail': product_detail, 'ImageTemplateProductsList': ImageTemplateProductsList})


def packages(request):
    return render(request, 'user/packages.html')


def order(request, id):
    products = Product.objects.all()
    sizesList = []
    AqutousCoatingProductList = []
    ColorsList = []
    PaperChoiceProductsList = []
    ShrinkWrappingProductsList = []
    FoldingOptionsProductsList = []
    NoOfMonthsProductsList = []
    HoleDrillingProductsList = []
    BindingMethodProductsList = []
    ImageTemplateProductsList = []

    try:
        sizesMap = SizeProductMapping.objects.filter(prod_id=id)
        sizesList = [data.size_id.prod_size for data in sizesMap]
    except AttributeError:
        pass

    try:
        colorMap = ColorProductMapping.objects.filter(prod_id=id)
        ColorsList = [data.color_id.prod_color for data in colorMap]
    except AttributeError:
        pass

    try:
        PaperChoiceProductMap = PaperChoiceProductMapping.objects.filter(prod_id=id)
        PaperChoiceProductsList = [data.paper_id.paper_choices_name for data in PaperChoiceProductMap]
    except AttributeError:
        pass

    try:
        AqutousCoatingProductMap = AqutousCoatingProductMapping.objects.filter(prod_id=id)
        AqutousCoatingProductList = [data.aqutous_coating_id.aqutous_coating_type for data in AqutousCoatingProductMap]
    except AttributeError:
        pass

    try:
        ShrinkWrappingProductsMap = SizeProductMapping.objects.filter(prod_id=id)
        ShrinkWrappingProductsList = [data.shrink_wrapping_id.shrink_options for data in ShrinkWrappingProductsMap]
    except AttributeError:
        pass

    try:
        FoldingOptionsProductsMap = FoldingOptionsProductMapping.objects.filter(prod_id=id)
        FoldingOptionsProductsList = [data.folding_options_id.folding_options_type for data in
                                      FoldingOptionsProductsMap]
    except AttributeError:
        pass

    try:
        NoOfMonthsProductsMap = NoOfMonthsProductMapping.objects.filter(prod_id=id)
        NoOfMonthsProductsList = [data.no_of_months_id.months for data in
                                  NoOfMonthsProductsMap]
    except AttributeError:
        pass

    try:
        HoleDrillingProductsMap = HoleDrillingProductMapping.objects.filter(prod_id=id)
        HoleDrillingProductsList = [data.hole_drilling_id.hole for data in
                                    HoleDrillingProductsMap]
    except AttributeError:
        pass

    try:
        BindingMethodProductsMap = BindingMethodProductMapping.objects.filter(prod_id=id)
        BindingMethodProductsList = [data.binding_method_id.binding_methods for data in
                                     BindingMethodProductsMap]
    except AttributeError:
        pass

    try:
        ImageTemplateProductsMap = ImageTemplateProductMapping.objects.filter(prod_id=id)
        ImageTemplateProductsList = [data.temp_id.temp_img for data in
                                     ImageTemplateProductsMap]
    except AttributeError:
        pass

    context = {'products': products,
               'sizesList': sizesList,
               "AqutousCoatingProductList": AqutousCoatingProductList,
               "ColorsList": ColorsList,
               "PaperChoiceProductsList": PaperChoiceProductsList,
               "ShrinkWrappingProductsList": ShrinkWrappingProductsList,
               "FoldingOptionsProductsList": FoldingOptionsProductsList,
               "NoOfMonthsProductsList": NoOfMonthsProductsList,
               "HoleDrillingProductsList": HoleDrillingProductsList,
               "BindingMethodProductsList": BindingMethodProductsList,
               "ImageTemplateProductsList": ImageTemplateProductsList
               }

    return render(request, 'user/order.html', context)


def aboutUs(request):
    return render(request, 'user/aboutUs.html')


def gallary(request):
    return render(request, 'user/Gallary.html')


def feedback(request):
    return render(request, 'user/feedback.html')


# def loginPage(request):
#     return render(request, 'user/login.html')
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('admin-home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('user-home')
            else:
                messages.error(request, 'Username or Password is incorrect')
                return redirect('user-login')

        context = {}
        return render(request, 'user/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('user-home')


# def registerPage(request):
#     return render(request, 'user/register.html')
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('admin-home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('admin-login')

        context = {'form': form}
        return render(request, 'User/register.html', context)
