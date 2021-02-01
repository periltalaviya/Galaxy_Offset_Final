from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from user.models import *
from .forms import SizeProductMapForm, ColorProductMapForm, PaperProductMapForm, ShrinkWrappingProductMapForm, \
    AqutousCoatingProductMapForm, FoldingOptionProductMapForm, NoOfMonthsProductMapForm, HoleDrillingProductMapForm, \
    ImageTempProductMapForm, CreateUserForm, EditUserProfile, OrderForm, BindingMethodProductMapForm


# Create your views here.


def index(request):
    return render(request, 'admin1/dashboard.html')


@login_required
def product(request):
    if request.method == 'POST':
        product_name = request.POST['p_name']
        product_price = request.POST['p_price']
        product_desc = request.POST['p_desc']
        product_image = request.FILES['p_image']
        product_store = Product(prod_Name=product_name, prod_Price=product_price,
                                prod_Desc=product_desc, prod_img=product_image)
        product_store.save()
        return redirect('/admin1/product/')
    else:
        product_show = Product.objects.all()
        # start paginator logic
        paginator = Paginator(product_show, 3)
        page = request.GET.get('page')
        try:
            product_show = paginator.page(page)
        except PageNotAnInteger:
            product_show = paginator.page(1)
        except EmptyPage:
            product_show = paginator.page(paginator.num_pages)
        # end paginator logic
        return render(request, 'admin1/product.html',
                      {'product_show': product_show})


def product_edit(request, id):
    if request.method == 'POST':
        product_name = request.POST['p_name']
        product_price = request.POST['p_price']
        product_desc = request.POST['p_desc']
        product_image = request.FILES['p_image']
        product_store = Product(prod_ID=id, prod_Name=product_name,
                                prod_Price=product_price, prod_Desc=product_desc, prod_img=product_image)
        product_store.save()
        return redirect('/admin1/product/')

    else:
        product_edit = Product.objects.filter(prod_ID=id)
        return render(request, 'admin1/product.html',
                      {'product_edit': product_edit})


def product_show1(request, id):
    product_show1 = Product.objects.filter(prod_ID=id)
    return render(request, 'admin1/product.html', {'product_show1': product_show1})


def product_delete(request, id):
    product_delete = Product.objects.filter(prod_ID=id)
    product_delete.delete()
    return redirect('/admin1/product/')


def addUser(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('/admin1/addUser')

    addUser_show = User.objects.all()
    # start paginator logic
    paginator = Paginator(addUser_show, 3)
    page = request.GET.get('page')
    try:
        addUser_show = paginator.page(page)
    except PageNotAnInteger:
        addUser_show = paginator.page(1)
    except EmptyPage:
        addUser_show = paginator.page(paginator.num_pages)
    # end paginator logic
    return render(request, 'admin1/addUser.html',
                  {'addUser_show': addUser_show, "form": form})


def addUser_show1(request, id):
    addUSer_show1 = User.objects.filter(user_id=id)
    return render(request, 'admin1/addUser.html', {'addUser_show1': addUSer_show1})


def addUser_delete(request, id):
    addUser_delete = User.objects.filter(user_id=id)
    addUser_delete.delete()
    return redirect('/admin1/addUser')


def addUser_edit(request, id):
    instance = User.objects.get(user_id=id)
    print(instance.username)
    form = EditUserProfile()
    if request.method == 'POST':
        form = EditUserProfile(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/admin1/addUser')
    else:
        form = EditUserProfile(instance=instance)

    return render(request, 'admin1/addUser.html', {'form': form, 'instance': instance})


# def order(request):
#     return render(request, 'admin1/order.html')
def order(request):
    form = OrderForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect("/admin1/order/")
    else:
        order_show = Order.objects.all()
        # start paginator logic
        paginator = Paginator(order_show, 3)
        page = request.GET.get('page')
        try:
            order_show = paginator.page(page)
        except PageNotAnInteger:
            order_show = paginator.page(1)
        except EmptyPage:
            order_show = paginator.page(paginator.num_pages)
        # end paginator logic
        return render(request, 'admin1/order.html', {'order_show': order_show, 'form': form})


def order_delete(request, id):
    order_delete = Order.objects.filter(order_id=id)
    order_delete.delete()
    return redirect('/admin1/order')


def order_edit(request, id):
    instance = Order.objects.get(order_id=id)
    form = OrderForm(instance=instance)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/admin1/order')
    else:
        form = Order(instance=instance)

    return render(request, 'admin1/order.html', {'form': form, 'instance': instance})


def payment(request):
    payment_show = Payment.objects.all()
    # start paginator logic
    paginator = Paginator(payment_show, 3)
    page = request.GET.get('page')
    try:
        payment_show = paginator.page(page)
    except PageNotAnInteger:
        payment_show = paginator.page(1)
    except EmptyPage:
        payment_show = paginator.page(paginator.num_pages)
    # end paginator logic
    return render(request, 'admin1/payment.html', {'payment_show': payment_show})


def viewProfile(request):
    return render(request, 'admin1/viewProfile.html')


def size(request):
    if request.method == 'POST':
        size_store = request.POST['prod_size']
        size_update = Size(prod_size=size_store)
        size_update.save()
        return redirect('/admin1/productSize')
    else:
        size_show = Size.objects.all()
        # start paginator logic
        paginator = Paginator(size_show, 3)
        page = request.GET.get('page')
        try:
            size_show = paginator.page(page)
        except PageNotAnInteger:
            size_show = paginator.page(1)
        except EmptyPage:
            size_show = paginator.page(paginator.num_pages)
        # end paginator logic
        return render(request, 'admin1/size.html', {'size_show': size_show})


def size_edit(request, id):
    size_edit = Size.objects.filter(size_id=id)
    return render(request, 'admin1/size.html', {'size_edit': size_edit})


def size_edit_update(request, id):
    if request.method == 'POST':
        size_store = request.POST['prod_size']
        size_update = Size(size_id=id, prod_size=size_store)
        size_update.save()
        return redirect('/admin1/productSize')


def size_delete(request, id):
    size_delete = Size.objects.filter(size_id=id)
    size_delete.delete()
    return redirect('/admin1/productSize')


def sizeProductMap(request):
    form = SizeProductMapForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect("/admin1/sizeProductMap/")
    else:
        sizeProductMap_show = SizeProductMapping.objects.all()
        # start paginator logic
        paginator = Paginator(sizeProductMap_show, 3)
        page = request.GET.get('page')
        try:
            sizeProductMap_show = paginator.page(page)
        except PageNotAnInteger:
            sizeProductMap_show = paginator.page(1)
        except EmptyPage:
            sizeProductMap_show = paginator.page(paginator.num_pages)
        # end paginator logic
        return render(request, 'admin1/sizeProductMap.html', {'sizeProductMap_show': sizeProductMap_show, 'form': form})


def sizeProductMap_delete(request, id):
    sizeProductMap_delete = SizeProductMapping.objects.filter(size_p_map_id=id)
    sizeProductMap_delete.delete()
    return redirect('/admin1/sizeProductMap')


def sizeProductMap_edit(request, id):
    instance = SizeProductMapping.objects.get(size_p_map_id=id)
    form = SizeProductMapForm(instance=instance)
    if request.method == 'POST':
        form = SizeProductMapForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/admin1/sizeProductMap')
    else:
        form = SizeProductMapForm(instance=instance)

    return render(request, 'admin1/sizeProductMap.html', {'form': form, 'instance': instance})


def templateImage(request):
    if request.method == 'POST':
        temp_img = request.FILES['temp_img']
        templateImage_update = ImageTemplate(temp_img=temp_img)
        templateImage_update.save()
        return redirect('/admin1/templateImage')
    else:
        templateImage_show = ImageTemplate.objects.all()
        # start paginator logic
        paginator = Paginator(templateImage_show, 3)
        page = request.GET.get('page')
        try:
            templateImage_show = paginator.page(page)
        except PageNotAnInteger:
            templateImage_show = paginator.page(1)
        except EmptyPage:
            templateImage_show = paginator.page(paginator.num_pages)
        # end paginator logic
        return render(request, 'admin1/templateImage.html', {'templateImage_show': templateImage_show})


def templateImage_show1(request, id):
    templateImage_show1 = ImageTemplate.objects.filter(temp_id=id)
    return render(request, 'admin1/templateImage.html', {'templateImage_show1': templateImage_show1})


def templateImage_edit(request, id):
    if request.method == 'POST':
        temp_img = request.FILES['temp_img']
        templateImage_store = ImageTemplate(temp_id=id, temp_img=temp_img)
        templateImage_store.save()
        return redirect('/admin1/templateImage/')

    else:
        templateImage_edit = ImageTemplate.objects.filter(temp_id=id)
        return render(request, 'admin1/templateImage.html',
                      {'templateImage_edit': templateImage_edit})


def templateImage_delete(request, id):
    templateImage_delete = ImageTemplate.objects.filter(temp_id=id)
    templateImage_delete.delete()
    return redirect('/admin1/templateImage')


def imageTempProductMap(request):
    form = ImageTempProductMapForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect("/admin1/imageTempProductMap/")
    else:
        imageTempProductMap_show = ImageTemplateProductMapping.objects.all()
        # start paginator logic
        paginator = Paginator(imageTempProductMap_show, 3)
        page = request.GET.get('page')
        try:
            imageTempProductMap_show = paginator.page(page)
        except PageNotAnInteger:
            imageTempProductMap_show = paginator.page(1)
        except EmptyPage:
            imageTempProductMap_show = paginator.page(paginator.num_pages)
        # end paginator logic
        return render(request, 'admin1/imageTempProductMap.html',
                      {'imageTempProductMap_show': imageTempProductMap_show, 'form': form})


def imageTempProductMap_delete(request, id):
    imageTempProductMap_delete = ImageTemplateProductMapping.objects.filter(imageTemp_p_map_id=id)
    imageTempProductMap_delete.delete()
    return redirect('/admin1/imageTempProductMap')


def imageTempProductMap_edit(request, id):
    instance = ImageTemplateProductMapping.objects.get(imageTemp_p_map_id=id)
    form = ImageTempProductMapForm(instance=instance)
    if request.method == 'POST':
        form = ImageTempProductMapForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/admin1/imageTempProductMap')
    else:
        form = ImageTempProductMapForm(instance=instance)

    return render(request, 'admin1/imageTempProductMap.html', {'form': form, 'instance': instance})


def color(request):
    if request.method == 'POST':
        color_store = request.POST['prod_color']
        color_update = Color(prod_color=color_store)
        color_update.save()
        return redirect('/admin1/productColor')
    else:
        color_show = Color.objects.all()
        # start paginator logic
        paginator = Paginator(color_show, 3)
        page = request.GET.get('page')
        try:
            color_show = paginator.page(page)
        except PageNotAnInteger:
            color_show = paginator.page(1)
        except EmptyPage:
            color_show = paginator.page(paginator.num_pages)
        # end paginator logic
        return render(request, 'admin1/Color.html', {'color_show': color_show})


def color_edit(request, id):
    color_edit = Color.objects.filter(color_id=id)
    return render(request, 'admin1/Color.html', {'color_edit': color_edit})


def color_edit_update(request, id):
    if request.method == 'POST':
        color_store = request.POST['prod_color']
        color_update = Color(color_id=id, prod_color=color_store)
        color_update.save()
        return redirect('/admin1/productColor')


def color_delete(request, id):
    color_delete = Color.objects.filter(color_id=id)
    color_delete.delete()
    return redirect('/admin1/productColor')


def colorProductMap(request):
    form = ColorProductMapForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect("/admin1/colorProductMap/")
    else:
        colorProductMap_show = ColorProductMapping.objects.all()
        # start paginator logic
        paginator = Paginator(colorProductMap_show, 3)
        page = request.GET.get('page')
        try:
            colorProductMap_show = paginator.page(page)
        except PageNotAnInteger:
            colorProductMap_show = paginator.page(1)
        except EmptyPage:
            colorProductMap_show = paginator.page(paginator.num_pages)
        # end paginator logic
        return render(request, 'admin1/colorProductMap.html',
                      {'colorProductMap_show': colorProductMap_show, 'form': form})


def colorProductMap_delete(request, id):
    colorProductMap_delete = ColorProductMapping.objects.filter(color_p_map_id=id)
    colorProductMap_delete.delete()
    return redirect('/admin1/colorProductMap')


def colorProductMap_edit(request, id):
    instance = ColorProductMapping.objects.get(color_p_map_id=id)
    form = ColorProductMapForm(instance=instance)
    if request.method == 'POST':
        form = ColorProductMapForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/admin1/colorProductMap')
    else:
        form = ColorProductMapForm(instance=instance)

    return render(request, 'admin1/colorProductMap.html', {'form': form, 'instance': instance})


def paperChoice(request):
    if request.method == 'POST':
        paperChoice_store = request.POST['paper_choices_name']
        paperChoice_update = PaperChoice(paper_choices_name=paperChoice_store)
        paperChoice_update.save()
        return redirect('/admin1/paperChoice')
    else:
        paperChoice_show = PaperChoice.objects.all()
        # start paginator logic
        paginator = Paginator(paperChoice_show, 3)
        page = request.GET.get('page')
        try:
            paperChoice_show = paginator.page(page)
        except PageNotAnInteger:
            paperChoice_show = paginator.page(1)
        except EmptyPage:
            paperChoice_show = paginator.page(paginator.num_pages)
        # end paginator logic
        return render(request, 'admin1/paperChoice.html', {'paperChoice_show': paperChoice_show})


def paperChoice_edit(request, id):
    paperChoice_edit = PaperChoice.objects.filter(paper_id=id)
    return render(request, 'admin1/paperChoice.html', {'paperChoice_edit': paperChoice_edit})


def paperChoice_edit_update(request, id):
    if request.method == 'POST':
        paperChoice_store = request.POST['paper_choice_name']
        paperChoice_update = PaperChoice(paper_id=id, paper_choice_name=paperChoice_store)
        paperChoice_update.save()
        return redirect('/admin1/paperChoice')


def paperChoice_delete(request, id):
    paperChoice_delete = PaperChoice.objects.filter(paper_id=id)
    paperChoice_delete.delete()
    return redirect('/admin1/paperChoice')


def paperProductMap(request):
    form = PaperProductMapForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect("/admin1/paperProductMap/")
    else:
        paperProductMap_show = PaperChoiceProductMapping.objects.all()
        # start paginator logic
        paginator = Paginator(paperProductMap_show, 3)
        page = request.GET.get('page')
        try:
            paperProductMap_show = paginator.page(page)
        except PageNotAnInteger:
            paperProductMap_show = paginator.page(1)
        except EmptyPage:
            paperProductMap_show = paginator.page(paginator.num_pages)
        # end paginator logic
        return render(request, 'admin1/paperChoiceProductMap.html',
                      {'paperProductMap_show': paperProductMap_show, 'form': form})


def paperProductMap_delete(request, id):
    paperProductMap_delete = PaperChoiceProductMapping.objects.filter(paper_p_map_id=id)
    paperProductMap_delete.delete()
    return redirect('/admin1/paperProductMap')


def paperProductMap_edit(request, id):
    instance = ColorProductMapping.objects.get(paper_p_map_id=id)
    form = PaperProductMapForm(instance=instance)
    if request.method == 'POST':
        form = PaperProductMapForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/admin1/paperProductMap')
    else:
        form = PaperProductMapForm(instance=instance)

    return render(request, 'admin1/paperChoiceProductMap.html', {'form': form, 'instance': instance})


def shrinkWrapping(request):
    if request.method == 'POST':
        shrinkWrapping_store = request.POST['shrink_options']
        shrinkWrapping_update = ShrinkWrapping(shrink_options=shrinkWrapping_store)
        shrinkWrapping_update.save()
        return redirect('/admin1/shrinkWrapping')
    else:
        shrinkWrapping_show = ShrinkWrapping.objects.all()
        # start paginator logic
        paginator = Paginator(shrinkWrapping_show, 3)
        page = request.GET.get('page')
        try:
            shrinkWrapping_show = paginator.page(page)
        except PageNotAnInteger:
            shrinkWrapping_show = paginator.page(1)
        except EmptyPage:
            shrinkWrapping_show = paginator.page(paginator.num_pages)
        # end paginator logic
        return render(request, 'admin1/shrinkWrapping.html', {'shrinkWrapping_show': shrinkWrapping_show})


def shrinkWrapping_edit(request, id):
    shrinkWrapping_edit = ShrinkWrapping.objects.filter(shrink_wrapping_id=id)
    return render(request, 'admin1/shrinkWrapping.html', {'shrinkWrapping_edit': shrinkWrapping_edit})


def shrinkWrapping_edit_update(request, id):
    if request.method == 'POST':
        shrinkWrapping_store = request.POST['shrink_options']
        shrinkWrapping_update = ShrinkWrapping(shrink_wrapping_id=id, shrink_options=shrinkWrapping_store)
        shrinkWrapping_update.save()
        return redirect('/admin1/shrinkWrapping')


def shrinkWrapping_delete(request, id):
    shrinkWrapping_delete = ShrinkWrapping.objects.filter(shrink_wrapping_id=id)
    shrinkWrapping_delete.delete()
    return redirect('/admin1/shrinkWrapping')


def shrinkWrappingProductMap(request):
    form = ShrinkWrappingProductMapForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect("/admin1/shrinkWrappingProductMap/")
    else:
        shrinkWrappingProductMap_show = ShrinkWrappingProductMapping.objects.all()
        # start paginator logic
        paginator = Paginator(shrinkWrappingProductMap_show, 3)
        page = request.GET.get('page')
        try:
            shrinkWrappingProductMap_show = paginator.page(page)
        except PageNotAnInteger:
            shrinkWrappingProductMap_show = paginator.page(1)
        except EmptyPage:
            shrinkWrappingProductMap_show = paginator.page(paginator.num_pages)
        # end paginator logic
        return render(request, 'admin1/shrinkWrappingProductMap.html',
                      {'shrinkWrappingProductMap_show': shrinkWrappingProductMap_show, 'form': form})


def shrinkWrappingProductMap_delete(request, id):
    shrinkWrappingProductMap_delete = ShrinkWrappingProductMapping.objects.filter(shrink_wrap_p_map_id=id)
    shrinkWrappingProductMap_delete.delete()
    return redirect('/admin1/shrinkWrappingProductMap')


def shrinkWrappingProductMap_edit(request, id):
    instance = ShrinkWrappingProductMapping.objects.get(shrink_wrap_p_map_id=id)
    form = ShrinkWrappingProductMapForm(instance=instance)
    if request.method == 'POST':
        form = ShrinkWrappingProductMapForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/admin1/shrinkWrappingProductMap')
    else:
        form = ShrinkWrappingProductMapForm(instance=instance)

    return render(request, 'admin1/shrinkWrappingProductMap.html', {'form': form, 'instance': instance})


def aqutousCoating(request):
    if request.method == 'POST':
        aqutousCoating_store = request.POST['aqutous_coating_type']
        aqutousCoating_update = AqutousCoating(aqutous_coating=aqutousCoating_store)
        aqutousCoating_update.save()
        return redirect('/admin1/aqutousCoating')
    else:
        aqutousCoating_show = AqutousCoating.objects.all()
        # start paginator logic
        paginator = Paginator(aqutousCoating_show, 3)
        page = request.GET.get('page')
        try:
            aqutousCoating_show = paginator.page(page)
        except PageNotAnInteger:
            aqutousCoating_show = paginator.page(1)
        except EmptyPage:
            aqutousCoating_show = paginator.page(paginator.num_pages)
        # end paginator logic
        return render(request, 'admin1/aqutousCoating.html', {'shrinkWrapping_show': aqutousCoating_show})


def aqutousCoating_edit(request, id):
    aqutousCoating_edit = AqutousCoating.objects.filter(aqutous_coating_id=id)
    return render(request, 'admin1/aqutousCoating.html', {'aqutousCoating_edit': aqutousCoating_edit})


def aqutousCoating_edit_update(request, id):
    if request.method == 'POST':
        aqutousCoating_store = request.POST['shrink_options']
        aqutousCoating_update = AqutousCoating(aqutous_coating_id=id, aqutous_coating_type=aqutousCoating_store)
        aqutousCoating_update.save()
        return redirect('/admin1/aqutousCoating')


def aqutousCoating_delete(request, id):
    aqutousCoating_delete = AqutousCoating.objects.filter(aqutous_coating_id=id)
    aqutousCoating_delete.delete()
    return redirect('/admin1/aqutousCoating')


def aqutousCoatingProductMap(request):
    form = AqutousCoatingProductMapForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect("/admin1/aqutousCoatingProductMap/")
    else:
        aqutousCoatingProductMap_show = AqutousCoatingProductMapping.objects.all()
        # start paginator logic
        paginator = Paginator(aqutousCoatingProductMap_show, 3)
        page = request.GET.get('page')
        try:
            aqutousCoatingProductMap_show = paginator.page(page)
        except PageNotAnInteger:
            aqutousCoatingProductMap_show = paginator.page(1)
        except EmptyPage:
            aqutousCoatingProductMap_show = paginator.page(paginator.num_pages)
        # end paginator logic
        return render(request, 'admin1/aqutousCoatingProductMap.html',
                      {'aqutousCoatingProductMap_show': aqutousCoatingProductMap_show, 'form': form})


def aqutousCoatingProductMap_delete(request, id):
    aqutousCoatingProductMap_delete = AqutousCoatingProductMapping.objects.filter(aCoat_p_map_id=id)
    aqutousCoatingProductMap_delete.delete()
    return redirect('/admin1/aqutousCoatingProductMap')


def aqutousCoatingProductMap_edit(request, id):
    instance = AqutousCoatingProductMapping.objects.get(aCoat_p_map_id=id)
    form = AqutousCoatingProductMapForm(instance=instance)
    if request.method == 'POST':
        form = AqutousCoatingProductMapForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/admin1/aqutousCoatingProductMap')
    else:
        form = AqutousCoatingProductMapForm(instance=instance)

    return render(request, 'admin1/aqutousCoatingProductMap.html', {'form': form, 'instance': instance})


def foldingOption(request):
    if request.method == 'POST':
        foldingOption_store = request.POST['folding_options_type']
        foldingOption_update = FoldingOptions(folding_options_type=foldingOption_store)
        foldingOption_update.save()
        return redirect('/admin1/foldingOption')
    else:
        foldingOption_show = FoldingOptions.objects.all()
        # start paginator logic
        paginator = Paginator(foldingOption_show, 3)
        page = request.GET.get('page')
        try:
            foldingOption_show = paginator.page(page)
        except PageNotAnInteger:
            foldingOption_show = paginator.page(1)
        except EmptyPage:
            foldingOption_show = paginator.page(paginator.num_pages)
        # end paginator logic
        return render(request, 'admin1/foldingOption.html', {'foldingOption_show': foldingOption_show})


def foldingOption_edit(request, id):
    foldingOption_edit = FoldingOptions.objects.filter(folding_options_id=id)
    return render(request, 'admin1/foldingOption.html', {'foldingOption_edit': foldingOption_edit})


def foldingOption_edit_update(request, id):
    if request.method == 'POST':
        foldingOption_store = request.POST['folding_options_type']
        foldingOption_update = FoldingOptions(folding_options_id=id, folding_option_type=foldingOption_store)
        foldingOption_update.save()
        return redirect('/admin1/foldingOption')


def foldingOption_delete(request, id):
    foldingOption_delete = FoldingOptions.objects.filter(folding_options_id=id)
    foldingOption_delete.delete()
    return redirect('/admin1/foldingOption')


def foldingOptionProductMap(request):
    form = FoldingOptionProductMapForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect("/admin1/foldingOptionProductMap/")
    else:
        foldingOptionProductMap_show = FoldingOptionsProductMapping.objects.all()
        # start paginator logic
        paginator = Paginator(foldingOptionProductMap_show, 3)
        page = request.GET.get('page')
        try:
            foldingOptionProductMap_show = paginator.page(page)
        except PageNotAnInteger:
            foldingOptionProductMap_show = paginator.page(1)
        except EmptyPage:
            foldingOptionProductMap_show = paginator.page(paginator.num_pages)
        # end paginator logic
        return render(request, 'admin1/foldingOptionProductMap.html',
                      {'foldingOptionProductMap_show': foldingOptionProductMap_show, 'form': form})


def foldingOptionProductMap_delete(request, id):
    foldingOptionProductMap_delete = FoldingOptionsProductMapping.objects.filter(folding_optiom_p_map_id=id)
    foldingOptionProductMap_delete.delete()
    return redirect('/admin1/foldingOptionProductMap')


def foldingOptionProductMap_edit(request, id):
    instance = FoldingOptionsProductMapping.objects.get(folding_optiom_p_map_id=id)
    form = FoldingOptionProductMapForm(instance=instance)
    if request.method == 'POST':
        form = FoldingOptionProductMapForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/admin1/foldingOptionProductMap')
    else:
        form = FoldingOptionProductMapForm(instance=instance)

    return render(request, 'admin1/foldingOptionProductMap.html', {'form': form, 'instance': instance})


def noOfMonths(request):
    if request.method == 'POST':
        noOfMonths_store = request.POST['months']
        noOfMonths_update = NoOfMonths(months=noOfMonths_store)
        noOfMonths_update.save()
        return redirect('/admin1/noOfMonths')
    else:
        noOfMonths_show = NoOfMonths.objects.all()
        # start paginator logic
        paginator = Paginator(noOfMonths_show, 3)
        page = request.GET.get('page')
        try:
            noOfMonths_show = paginator.page(page)
        except PageNotAnInteger:
            noOfMonths_show = paginator.page(1)
        except EmptyPage:
            noOfMonths_show = paginator.page(paginator.num_pages)
        # end paginator logic
        return render(request, 'admin1/NoOfMonths.html', {'noOfMonths_show': noOfMonths_show})


def noOfMonths_edit(request, id):
    noOfMonths_edit = NoOfMonths.objects.filter(no_of_months_id=id)
    return render(request, 'admin1/NoOfMonths.html', {'noOfMonths_edit': noOfMonths_edit})


def noOfMonths_edit_update(request, id):
    if request.method == 'POST':
        noOfMonths_store = request.POST['months']
        noOfMonths_update = NoOfMonths(no_of_months_id=id, months=noOfMonths_store)
        noOfMonths_update.save()
        return redirect('/admin1/noOfMonths')


def noOfMonths_delete(request, id):
    noOfMonths_delete = NoOfMonths.objects.filter(no_of_months_id=id)
    noOfMonths_delete.delete()
    return redirect('/admin1/noOfMonths')


def noOfMonthsProductMap(request):
    form = NoOfMonthsProductMapForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect("/admin1/noOfMonthsProductMap/")
    else:
        noOfMonthsProductMap_show = NoOfMonthsProductMapping.objects.all()
        # start paginator logic
        paginator = Paginator(noOfMonthsProductMap_show, 3)
        page = request.GET.get('page')
        try:
            noOfMonthsProductMap_show = paginator.page(page)
        except PageNotAnInteger:
            noOfMonthsProductMap_show = paginator.page(1)
        except EmptyPage:
            noOfMonthsProductMap_show = paginator.page(paginator.num_pages)
        # end paginator logic
        return render(request, 'admin1/noOfMonthsProductMap.html',
                      {'noOfMonthsProductMap_show': noOfMonthsProductMap_show, 'form': form})


def noOfMonthsProductMap_delete(request, id):
    noOfMonthsProductMap_delete = NoOfMonthsProductMapping.objects.filter(no_of_months_p_map_id=id)
    noOfMonthsProductMap_delete.delete()
    return redirect('/admin1/noOfMonthsProductMap')


def noOfMonthsProductMap_edit(request, id):
    instance = NoOfMonthsProductMapping.objects.get(no_of_months_p_map_id=id)
    form = NoOfMonthsProductMapForm(instance=instance)
    if request.method == 'POST':
        form = NoOfMonthsProductMapForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/admin1/noOfMonthsProductMap')
    else:
        form = NoOfMonthsProductMapForm(instance=instance)

    return render(request, 'admin1/noOfMonthsProductMap.html', {'form': form, 'instance': instance})


def holeDrilling(request):
    if request.method == 'POST':
        holeDrilling_store = request.POST['hole']
        holeDrilling_update = HoleDrilling(hole=holeDrilling_store)
        holeDrilling_update.save()
        return redirect('/admin1/holeDrilling')
    else:
        holeDrilling_show = HoleDrilling.objects.all()
        # start paginator logic
        paginator = Paginator(holeDrilling_show, 3)
        page = request.GET.get('page')
        try:
            holeDrilling_show = paginator.page(page)
        except PageNotAnInteger:
            holeDrilling_show = paginator.page(1)
        except EmptyPage:
            holeDrilling_show = paginator.page(paginator.num_pages)
        # end paginator logic
        return render(request, 'admin1/holeDrilling.html', {'holeDrilling_show': holeDrilling_show})


def holeDrilling_edit(request, id):
    holeDrilling_edit = HoleDrilling.objects.filter(hole_drilling_id=id)
    return render(request, 'admin1/holeDrilling.html', {'holeDrilling_edit': holeDrilling_edit})


def holeDrilling_edit_update(request, id):
    if request.method == 'POST':
        holeDrilling_store = request.POST['hole']
        holeDrilling_update = HoleDrilling(hole_drilling_id=id, hole=holeDrilling_store)
        holeDrilling_update.save()
        return redirect('/admin1/holeDrilling')


def holeDrilling_delete(request, id):
    holeDrilling_delete = HoleDrilling.objects.filter(hole_drilling_id=id)
    holeDrilling_delete.delete()
    return redirect('/admin1/holeDrilling')


def holeDrillingProductMap(request):
    form = HoleDrillingProductMapForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect("/admin1/holeDrillingProductMap/")
    else:
        holeDrillingProductMap_show = HoleDrillingProductMapping.objects.all()
        # start paginator logic
        paginator = Paginator(holeDrillingProductMap_show, 3)
        page = request.GET.get('page')
        try:
            holeDrillingProductMap_show = paginator.page(page)
        except PageNotAnInteger:
            holeDrillingProductMap_show = paginator.page(1)
        except EmptyPage:
            holeDrillingProductMap_show = paginator.page(paginator.num_pages)
        # end paginator logic
        return render(request, 'admin1/holeDrillingProductMap.html',
                      {'holeDrillingProductMap_show': holeDrillingProductMap_show, 'form': form})


def holeDrillingProductMap_delete(request, id):
    holeDrillingProductMap_delete = HoleDrillingProductMapping.objects.filter(hole_drill_p_map_id=id)
    holeDrillingProductMap_delete.delete()
    return redirect('/admin1/holeDrillingProductMap')


def holeDrillingProductMap_edit(request, id):
    instance = HoleDrillingProductMapping.objects.get(hole_drill_p_map_id=id)
    form = HoleDrillingProductMapForm(instance=instance)
    if request.method == 'POST':
        form = HoleDrillingProductMapForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/admin1/holeDrillingProductMap')
    else:
        form = HoleDrillingProductMapForm(instance=instance)

    return render(request, 'admin1/holeDrillingProductMap.html', {'form': form, 'instance': instance})


def bindingMethod(request):
    if request.method == 'POST':
        bindingMethod_store = request.POST['binding_methods']
        bindingMethod_update = BindingMethod(binding_methods=bindingMethod_store)
        bindingMethod_update.save()
        return redirect('/admin1/bindingMethod')
    else:
        bindingMethod_show = BindingMethod.objects.all()
        # start paginator logic
        paginator = Paginator(bindingMethod_show, 3)
        page = request.GET.get('page')
        try:
            bindingMethod_show = paginator.page(page)
        except PageNotAnInteger:
            bindingMethod_show = paginator.page(1)
        except EmptyPage:
            bindingMethod_show = paginator.page(paginator.num_pages)
        # end paginator logic
        return render(request, 'admin1/bindingMethod.html', {'bindingMethod_show': bindingMethod_show})


def bindingMethod_edit(request, id):
    bindingMethod_edit = BindingMethod.objects.filter(binding_method_id=id)
    return render(request, 'admin1/bindingMethod.html', {'bindingMethod_edit': bindingMethod_edit})


def bindingMethod_edit_update(request, id):
    if request.method == 'POST':
        bindingMethod_store = request.POST['binding_methods']
        bindingMethod_update = BindingMethod(binding_method_id=id, binding_methods=bindingMethod_store)
        bindingMethod_update.save()
        return redirect('/admin1/bindingMethod')


def bindingMethod_delete(request, id):
    bindingMethod_delete = BindingMethod.objects.filter(binding_method_id=id)
    bindingMethod_delete.delete()
    return redirect('/admin1/bindingMethod')


def bindingMethodProductMap(request):
    form = BindingMethodProductMapForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect("/admin1/bindingMethodProductMap/")
    else:
        bindingMethodProductMap_show = BindingMethodProductMapping.objects.all()
        # start paginator logic
        paginator = Paginator(bindingMethodProductMap_show, 3)
        page = request.GET.get('page')
        try:
            bindingMethodProductMap_show = paginator.page(page)
        except PageNotAnInteger:
            bindingMethodProductMap_show = paginator.page(1)
        except EmptyPage:
            bindingMethodProductMap_show = paginator.page(paginator.num_pages)
        # end paginator logic
        return render(request, 'admin1/bindingMethodProductMap.html',
                      {'bindingMethodProductMap_show': bindingMethodProductMap_show, 'form': form})


def bindingMethodProductMap_delete(request, id):
    bindingMethodProductMap_delete = BindingMethodProductMapping.objects.filter(binding_methods_p_map_id=id)
    bindingMethodProductMap_delete.delete()
    return redirect('/admin1/bindingMethodProductMap')


def bindingMethodProductMap_edit(request, id):
    instance = BindingMethodProductMapping.objects.get(binding_methods_p_map_id=id)
    form = BindingMethodProductMapForm(instance=instance)
    if request.method == 'POST':
        form = BindingMethodProductMapForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/admin1/bindingMethodProductMap')
    else:
        form = BindingMethodProductMapForm(instance=instance)

    return render(request, 'admin1/bindingMethodProductMap.html', {'form': form, 'instance': instance})


def feedback(request):
    feedback_show = FeedBack.objects.all()
    # start paginator logic
    paginator = Paginator(feedback_show, 3)
    page = request.GET.get('page')
    try:
        feedback_show = paginator.page(page)
    except PageNotAnInteger:
        feedback_show = paginator.page(1)
    except EmptyPage:
        feedback_show = paginator.page(paginator.num_pages)
    # end paginator logic
    return render(request, 'admin1/feedback.html', {'feedback_show': feedback_show})


def feedback_delete(request, id):
    feedback_delete = FeedBack.objects.filter(feedback_id=id)
    feedback_delete.delete()
    return redirect('/admin1/feedback')


def gallary(request):
    if request.method == 'POST':
        img_path = request.FILES['img_path']
        gallary_update = Gallary(img_path=img_path)
        gallary_update.save()
        return redirect('/admin1/gallary')
    else:
        gallary_show = Gallary.objects.all()
        # start paginator logic
        paginator = Paginator(gallary_show, 3)
        page = request.GET.get('page')
        try:
            gallary_show = paginator.page(page)
        except PageNotAnInteger:
            gallary_show = paginator.page(1)
        except EmptyPage:
            gallary_show = paginator.page(paginator.num_pages)
        # end paginator logic
        return render(request, 'admin1/gallary.html', {'gallary_show': gallary_show})


def gallary_show1(request, id):
    gallary_show1 = Gallary.objects.filter(img_id=id)
    return render(request, 'admin1/gallary.html', {'gallary_show1': gallary_show1})


def gallary_edit(request, id):
    if request.method == 'POST':
        img_path = request.FILES['img_path']
        gallary_store = Gallary(img_id=id, img_path=img_path)
        gallary_store.save()
        return redirect('/admin1/gallary/')

    else:
        gallary_edit = Gallary.objects.filter(img_id=id)
        return render(request, 'admin1/gallary.html',
                      {'gallary_edit': gallary_edit})


def gallary_delete(request, id):
    gallary_delete = Gallary.objects.filter(img_id=id)
    gallary_delete.delete()
    return redirect('/admin1/gallary')
