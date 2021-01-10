from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect

from user.models import *


# Create your views here.


def index(request):
    return render(request, 'admin1/dashboard.html')


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
    return render(request, 'admin1/adduser.html')


def order(request):
    return render(request, 'admin1/order.html')


def payment(request):
    return render(request, 'admin1/Payment.html')


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


def size_delete(id):
    size_delete = Size.objects.filter(size_id=id)
    size_delete.delete()
    return redirect('/admin1/productSize')


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


def templateImage_delete(id):
    templateImage_delete = ImageTemplate.objects.filter(temp_id=id)
    templateImage_delete.delete()
    return redirect('/admin1/templateImage')


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


def color_delete(id):
    color_delete = Color.objects.filter(color_id=id)
    color_delete.delete()
    return redirect('/admin1/productColor')


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


def paperChoice_delete(id):
    paperChoice_delete = ShrinkWrapping.objects.filter(paper_id=id)
    paperChoice_delete.delete()
    return redirect('/admin1/paperChoice')


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


def shrinkWrapping_delete(id):
    shrinkWrapping_delete = ShrinkWrapping.objects.filter(shrink_wrapping_id=id)
    shrinkWrapping_delete.delete()
    return redirect('/admin1/shrinkWrapping')


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


def aqutousCoating_delete(id):
    aqutousCoating_delete = AqutousCoating.objects.filter(aqutous_coating_id=id)
    aqutousCoating_delete.delete()
    return redirect('/admin1/aqutousCoating')


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


def feedback_delete(id):
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
        gallary_store = Product(img_id=id, img_path=img_path)
        gallary_store.save()
        return redirect('/admin1/gallary/')

    else:
        gallary_edit = Gallary.objects.filter(img_id=id)
        return render(request, 'admin1/gallary.html',
                      {'gallary_edit': gallary_edit})


def gallary_delete(id):
    gallary_delete = Gallary.objects.filter(img_id=id)
    gallary_delete.delete()
    return redirect('/admin1/gallary')
