import json

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError

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
    loop_times = range(500, 10000, 500)
    value = {}
    State = ''
    City = ''
    Postal_Code = 0
    Job_title = ''
    Order_Detail = ''
    User_Address = ''
    quantity = 0
    TemplateValue = ''

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
        ShrinkWrappingProductsMap = ShrinkWrappingProductMapping.objects.filter(prod_id=id)
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

    if request.method == 'POST':
        customer_id = request.user
        product = Product.objects.get(prod_ID=id)
        product_id = product
        try:
            quantity = request.POST['quantity']
            print(quantity)
        except MultiValueDictKeyError:
            pass

        try:
            size = request.POST['size']
            value.update(size=size)
        except MultiValueDictKeyError:
            pass

        try:
            Colour = request.POST['Color']
            value.update(Colour=Colour)
        except MultiValueDictKeyError:
            pass

        try:
            Paper_Choice = request.POST['PaperChoice']
            value.update(Paper_Choice=Paper_Choice)
        except MultiValueDictKeyError:
            pass

        try:
            Aqutous_Coating = request.POST['AqutousCoating']
            value.update(Aqutous_Coating=Aqutous_Coating)
        except MultiValueDictKeyError:
            pass

        try:
            Shrink_Wrapping = request.POST['ShrinkWrapping']
            value.update(Shrink_Wrapping=Shrink_Wrapping)
        except MultiValueDictKeyError:
            pass

        try:
            Folding_Options = request.POST['FoldingOptions']
            value.update(Folding_Options=Folding_Options)
        except MultiValueDictKeyError:
            pass

        try:
            No_Of_Months = request.POST['NoOfMonths']
            value.update(No_Of_Months=No_Of_Months)
        except MultiValueDictKeyError:
            pass

        try:
            Binding_Method = request.POST['BindingMethod']
            value.update(Binding_Method=Binding_Method)
        except MultiValueDictKeyError:
            pass

        try:
            Hole_Drilling = request.POST['HoleDrilling']
            value.update(Hole_Drilling=Hole_Drilling)
        except MultiValueDictKeyError:
            pass

        try:
            Job_title = request.POST['jobTitle']
        except MultiValueDictKeyError:
            pass

        try:
            Order_Detail = request.POST['orderDetail']
        except MultiValueDictKeyError:
            pass

        try:
            User_Address = request.POST['address']
        except MultiValueDictKeyError:
            pass

        try:
            State = request.POST['state']
        except MultiValueDictKeyError:
            pass

        try:
            City = request.POST['city']
        except MultiValueDictKeyError:
            pass

        try:
            Postal_Code = request.POST['postalCode']
            Postal_Code = int(Postal_Code)
        except MultiValueDictKeyError:
            pass

        try:
            if request.POST['templateValue'] == 'Upload':
                if 'image' in request.FILES:
                    Template_Value1 = request.FILES['image']

                    fs = FileSystemStorage()
                    fs.save(Template_Value1.name, Template_Value1)
                    TemplateValue = Template_Value1.name
            elif request.POST['templateValue'] == 'Select':
                TemplateValue = request.POST['image2']
            else:
                pass
        except MultiValueDictKeyError:
            pass

        attribute_value = json.dumps(value)

        order_store = Order(user_id=customer_id, prod_id=product_id, quantity=quantity, attribute_value=attribute_value,
                            order_job_title=Job_title, order_desc=Order_Detail, address=User_Address, state=State,
                            city=City, postal_code=Postal_Code, product_img=TemplateValue)
        order_store.save()

    context = {'products': products,
               "loop_times": loop_times,
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


def contactUs(request):
    if request.method == 'POST':
        user_id = request.user
        feedback = request.POST['feedback']

        feedback_store = FeedBack(user_id=user_id, feedback_desc=feedback)
        feedback_store.save()
        return redirect('user-contact-us')

    return render(request, 'user/contactUS.html')


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('user-home')
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

                return redirect('user-login')

        context = {'form': form}
        return render(request, 'User/register.html', context)


@login_required(login_url="user-login")
def viewProfile(request):
    return render(request, "user/viewProfile.html")
