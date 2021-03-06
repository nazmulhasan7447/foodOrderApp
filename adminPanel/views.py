from django.shortcuts import render, redirect
from django.contrib import messages
from user.models import Account, VerificationCode
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
# from django.core.mail import EmailMessage
# from django.template.loader import render_to_string
# from verification.random_code_gen import rand_num_gen
# from verification.email_threadings import EmailThreading
# from django.utils import timezone
from .models import *
from django.db.models import Q
from django.http import JsonResponse
import uuid
from django.core.files.storage import FileSystemStorage


def ap_RegisterSuperUser(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        username = request.POST['username']
        phone = request.POST['phone']
        password = request.POST['password']
        confirmpass = request.POST['con_pass']


        if name and email and username and phone and password and confirmpass:
            if  len(Account.objects.filter(email=email)) <= 0 and len(Account.objects.filter(username=username)) <= 0 and len(Account.objects.filter(phone_no=phone)) <= 0:
                if password == confirmpass:
                    try:
                        user_account = Account.objects.create_superuser(email=email, username=username, phone_no=phone, password=password)
                        user_account.fname = name
                        user_account.status = '0'
                        user_account.is_active = False
                        user_account.save()

                        # subject = f"Verification code"
                        # verification_url = f"http://127.0.0.1:8000/user/account/veirfication/{username}/{phone}/"
                        # html_content = render_to_string('backEnd_superAdmin/verification_template.html',
                        #                                 context={'verification_code': verification_url})
                        # email = EmailMessage(subject, html_content, to=[email])
                        # email.content_subtype = 'html'
                        # EmailThreading(email).start()
                        messages.success(request, "Verification code has been sent! Verify to activate your account!")
                        return redirect('apSuperAdminRegister')
                    except:
                        messages.success(request, "Can't create account! Try again!")
                        return redirect('adminPanelLoginRegister')
                    # ends sending verification email with code*************************

                else:
                    messages.success(request, "Password didn't match! Try again!")
                    return redirect('adminPanelLoginRegister')

    return render(request, 'backEnd_superAdmin/register.html')

def ap_loginSuperUser(request):

    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        if email and username and password:
            try:
                user = Account.objects.get(email=email)
                try:
                    if user.status == '1' and user.is_active == True:
                        authenticate_user = authenticate(request, email=email, password=password)
                        if authenticate_user is not None:
                            login(request, authenticate_user)
                            return redirect('apHome')
                        else:
                            messages.warning(request, "You are not authenticated yet!")
                            return redirect('adminPanelLoginRegister')
                    else:
                        messages.warning(request, "Please verify your account to acccess!")
                        return redirect('adminPanelLoginRegister')
                except:
                    messages.warning(request, "User not found!")
                    return redirect('adminPanelLoginRegister')
            except:
                messages.warning(request, 'Wrong username or email')
                return redirect('adminPanelLoginRegister')

    return render(request, 'backEnd_superAdmin/log_in.html')


def logoutSuperUser(request):
    try:
        logout(request)
        return redirect('adminPanelLoginRegister')
    except:
        pass
    redirect('adminPanelLoginRegister')


# @login_required(login_url='/ap/login/register')
def index(request):

    return render(request, 'backEnd_superAdmin/index.html')

# @login_required(login_url='/ap/login/register')
def home(request):

    user_list = Account.objects.all()

    context = {
        'user_list' : user_list,
    }

    return render(request, 'backEnd_superAdmin/home.html', context)

# @login_required(login_url='/ap/login/register')
def deactivateUser(request, pk):

    try:
        current_user = Account.objects.get(pk=pk)
        current_user.is_active = False
        current_user.save()
        messages.success(request, "User account has been deactivated!")
        return redirect('apHome')
    except:
        messages.warning(request, "Sorry! User not found!")
        return redirect('apHome')
    return redirect('apHome')

# @login_required(login_url='/ap/login/register')
def activateUser(request, pk):
    try:
        current_user = Account.objects.get(pk=pk)
        current_user.is_active = True
        current_user.save()
        messages.success(request, "User account has been activated!")
        return redirect('apHome')
    except:
        messages.warning(request, "Sorry! User not found!")
        return redirect('apHome')
    return redirect('apHome')

# @login_required(login_url='/ap/login/register')
def removeUser(request, pk):

    try:
        current_user = Account.objects.get(pk=pk)
        current_user.delete()
        messages.success(request, "User account has been removed!")
        return redirect('apHome')
    except:
        messages.warning(request, "Sorry! User not found!")
        return redirect('apHome')
    return redirect('apHome')


# accounts section *********************************************************
# @login_required(login_url='/ap/login/register')
def ap_seller_accounts_list(request):

    seller_list = Account.objects.filter(Q(is_seller=True) & Q(status='1'))

    context = {
        'seller_list' : seller_list,
    }

    return render(request, 'backEnd_superAdmin/accounts/seller_accounts_list.html', context)


# @login_required(login_url='/ap/login/register')
def ap_buyer_accounts_list(request):
    buyer_list = Account.objects.filter(Q(is_buyer=True) & Q(status='1'))

    context = {
        'buyer_list': buyer_list,
    }

    return render(request, 'backEnd_superAdmin/accounts/buyer_accounts_list.html', context)


# @login_required(login_url='/ap/login/register')
def ap_staff_accounts_list(request):
    staff_list = Account.objects.filter(Q(is_a_staff=True) & Q(status='1'))

    context = {
        'staff_list': staff_list,
    }

    return render(request, 'backEnd_superAdmin/accounts/staff_accounts_list.html', context)



# @login_required(login_url='/ap/login/register')
def ap_add_hotel(request):

    if request.method == 'POST':
        name = request.POST['name']
        city = request.POST['city']
        state = request.POST['state']
        description = request.POST['description']
        check_in = request.POST['check_in']
        check_out = request.POST['check_out']
        attraction_name_one = request.POST['attraction_name_one']
        attraction_one_distance = request.POST['attraction_one_distance']
        attraction_name_two = request.POST['attraction_name_two']
        attraction_name_two_distance = request.POST['attraction_name_two_distance']
        map_link = request.POST['map_link']
        wifi = request.POST.get('wifi')
        tv = request.POST.get('tv')
        parking = request.POST.get('parking')
        ac = request.POST.get('ac')

        images = request.FILES.getlist('hotel__images')

        hotel_id = uuid.uuid4()

        try:
            wif_i = False
            t_v = False
            parkin_g = False
            a_c = False

            if wifi == 'on':
                wif_i = True
            if tv == 'on':
                t_v = True
            if parking == 'on':
                parkin_g = True
            if ac == 'on':
                a_c = True

            hotel_model = Hotels(
                hotel_id=hotel_id,
                name=name,
                city=city,
                state=state,
                description=description,
                check_in=check_in,
                check_out=check_out,
                attraction_one_name=attraction_name_one,
                attraction_one_distance=attraction_one_distance,
                attraction_two_name=attraction_name_two,
                attraction_two_distance=attraction_name_two_distance,
                map_link=map_link,
                ac=a_c,
                parking=parkin_g,
                tv=t_v,
                wifi=wif_i,
                )
            hotel_model.save()

            if images:
                length_of_images = len(images)
                hotel = Hotels.objects.get(hotel_id=hotel_id)
                if length_of_images == 1:
                    hotel_img_model = HotelImages(hotel=hotel, img1=images[0])
                    hotel_img_model.save()
                if length_of_images == 2:
                    hotel_img_model = HotelImages(hotel=hotel, img1=images[0], img2=images[1])
                    hotel_img_model.save()
                if length_of_images == 3:
                    hotel_img_model = HotelImages(hotel=hotel, img1=images[0], img2=images[1], img3=images[2])
                    hotel_img_model.save()
                if length_of_images == 4:
                    hotel_img_model = HotelImages(hotel=hotel, img1=images[0], img2=images[1], img3=images[2], img4=images[3])
                    hotel_img_model.save()
                if length_of_images == 5:
                    hotel_img_model = HotelImages(hotel=hotel, img1=images[0], img2=images[1], img3=images[2], img4=images[3], img5=images[4])
                    hotel_img_model.save()
                if length_of_images == 6:
                    hotel_img_model = HotelImages(hotel=hotel, img1=images[0], img2=images[1], img3=images[2], img4=images[3], img5=images[4], img6=images[5])
                    hotel_img_model.save()
                if length_of_images == 7:
                    hotel_img_model = HotelImages(hotel=hotel, img1=images[0], img2=images[1], img3=images[2], img4=images[3], img5=images[4], img6=images[5], img7=images[6])
                    hotel_img_model.save()
                if length_of_images == 8:
                    hotel_img_model = HotelImages(hotel=hotel, img1=images[0], img2=images[1], img3=images[2], img4=images[3], img5=images[4], img6=images[5], img7=images[6], img8=images[7])
                    hotel_img_model.save()
                if length_of_images == 9:
                    hotel_img_model = HotelImages(hotel=hotel, img1=images[0], img2=images[1], img3=images[2], img4=images[3], img5=images[4], img6=images[5], img7=images[6], img8=images[7], img9=images[8])
                    hotel_img_model.save()
                if length_of_images == 10:
                    hotel_img_model = HotelImages(hotel=hotel, img1=images[0], img2=images[1], img3=images[2], img4=images[3], img5=images[4], img6=images[5], img7=images[6], img8=images[7], img9=images[8], img10=images[9])
                    hotel_img_model.save()

            messages.success(request, "Successfully added!")
            return redirect('apHotelList')
        except:
            messages.warning(request, "Something wrong! Try again!")
            return redirect('apHotelList')

    return render(request, 'backEnd_superAdmin/add_hotel.html')


# @login_required(login_url='/ap/login/register')
def ap_hotel_list(request):

    hotel_list = Hotels.objects.all()

    context = {
        'hotel_list' : hotel_list,
    }

    return render(request, 'backEnd_superAdmin/hotel_list.html', context)

# @login_required(login_url='/ap/login/register')
def ap_del_hotel(request, pk):

    try:
        current_obj = Hotels.objects.get(pk=pk)
        current_obj.delete()
        messages.success(request, 'Successfully deleted!')
        return redirect('apHotelList')
    except:
        messages.warning(request, "Can't be deleted!")
        return redirect('apHotelList')

    return redirect('apHotelList')


# @login_required(login_url='/ap/login/register')
def ap_update_hotel_info(request, pk):

    current_obj = Hotels.objects.get(pk=pk)
    current_hotel_img_obj = HotelImages.objects.filter(hotel=current_obj)

    if request.method == 'POST':
        name = request.POST['name']
        city = request.POST['city']
        state = request.POST['state']
        description = request.POST['description']
        check_in = request.POST['check_in']
        check_out = request.POST['check_out']
        attraction_name_one = request.POST['attraction_name_one']
        attraction_one_distance = request.POST['attraction_one_distance']
        attraction_name_two = request.POST['attraction_name_two']
        attraction_name_two_distance = request.POST['attraction_name_two_distance']
        map_link = request.POST['map_link']
        wifi = request.POST.get('wifi')
        tv = request.POST.get('tv')
        parking = request.POST.get('parking')
        ac = request.POST.get('ac')

        fs = FileSystemStorage()

        wif_i = False
        t_v = False
        parkin_g = False
        a_c = False

        if wifi == 'on':
            wif_i = True
        if tv == 'on':
            t_v = True
        if parking == 'on':
            parkin_g = True
        if ac == 'on':
            a_c = True

        current_obj.name = name
        current_obj.city = city
        current_obj.state = state
        current_obj.description = description
        current_obj.check_in = check_in
        current_obj.check_out = check_out
        current_obj.attraction_one_name = attraction_name_one
        current_obj.attraction_one_distance = attraction_one_distance
        current_obj.attraction_two_name = attraction_name_two
        current_obj.attraction_two_distance = attraction_name_two_distance
        current_obj.map_link = map_link
        current_obj.ac = a_c
        current_obj.parking = parkin_g
        current_obj.tv = t_v
        current_obj.wifi = wif_i
        current_obj.save()

        try:
            images = request.FILES.getlist('hotel__images')
            length_of_images = len(images)
            hotel_image_model = HotelImages.objects.get(hotel=current_obj)

            if images:
                if current_hotel_img_obj[0].img1:
                    fs.delete(current_hotel_img_obj[0].img1.name)
                if current_hotel_img_obj[0].img2:
                    fs.delete(current_hotel_img_obj[0].img2.name)
                if current_hotel_img_obj[0].img3:
                    fs.delete(current_hotel_img_obj[0].img3.name)
                if current_hotel_img_obj[0].img4:
                    fs.delete(current_hotel_img_obj[0].img4.name)
                if current_hotel_img_obj[0].img5:
                    fs.delete(current_hotel_img_obj[0].img5.name)
                if current_hotel_img_obj[0].img6:
                    fs.delete(current_hotel_img_obj[0].img6.name)
                if current_hotel_img_obj[0].img7:
                    fs.delete(current_hotel_img_obj[0].img7.name)
                if current_hotel_img_obj[0].img8:
                    fs.delete(current_hotel_img_obj[0].img8.name)
                if current_hotel_img_obj[0].img9:
                    fs.delete(current_hotel_img_obj[0].img9.name)
                if current_hotel_img_obj[0].img10:
                    fs.delete(current_hotel_img_obj[0].img10.name)

                if length_of_images > 0:
                    if length_of_images == 1:
                        hotel_image_model.img1 = images[0]
                        print(images[0])
                        hotel_image_model.save()
                        print(images[0])
                    elif length_of_images == 2:
                        hotel_image_model.img1 = images[0]
                        hotel_image_model.img2 = images[1]
                        hotel_image_model.save()
                    elif length_of_images == 3:
                        hotel_image_model.img1 = images[0]
                        hotel_image_model.img2 = images[1]
                        hotel_image_model.img3 = images[2]
                        hotel_image_model.save()
                    elif length_of_images == 4:
                        hotel_image_model.img1 = images[0]
                        hotel_image_model.img2 = images[1]
                        hotel_image_model.img3 = images[2]
                        hotel_image_model.img4 = images[3]
                        hotel_image_model.save()
                    elif length_of_images == 5:
                        hotel_image_model.img1 = images[0]
                        hotel_image_model.img2 = images[1]
                        hotel_image_model.img3 = images[2]
                        hotel_image_model.img4 = images[3]
                        hotel_image_model.img5 = images[4]
                        hotel_image_model.save()
                    elif length_of_images == 6:
                        hotel_image_model.img1 = images[0]
                        hotel_image_model.img2 = images[1]
                        hotel_image_model.img3 = images[2]
                        hotel_image_model.img4 = images[3]
                        hotel_image_model.img5 = images[4]
                        hotel_image_model.img6 = images[5]
                        hotel_image_model.save()
                    elif length_of_images == 7:
                        hotel_image_model.img1 = images[0]
                        hotel_image_model.img2 = images[1]
                        hotel_image_model.img3 = images[2]
                        hotel_image_model.img4 = images[3]
                        hotel_image_model.img5 = images[4]
                        hotel_image_model.img6 = images[5]
                        hotel_image_model.img7 = images[6]
                        hotel_image_model.save()
                    elif length_of_images == 8:
                        hotel_image_model.img1 = images[0]
                        hotel_image_model.img2 = images[1]
                        hotel_image_model.img3 = images[2]
                        hotel_image_model.img4 = images[3]
                        hotel_image_model.img5 = images[4]
                        hotel_image_model.img6 = images[5]
                        hotel_image_model.img7 = images[6]
                        hotel_image_model.img8 = images[7]
                        hotel_image_model.save()
                    elif length_of_images == 9:
                        hotel_image_model.img1 = images[0]
                        hotel_image_model.img2 = images[1]
                        hotel_image_model.img3 = images[2]
                        hotel_image_model.img4 = images[3]
                        hotel_image_model.img5 = images[4]
                        hotel_image_model.img6 = images[5]
                        hotel_image_model.img7 = images[6]
                        hotel_image_model.img8 = images[7]
                        hotel_image_model.img9 = images[8]
                        hotel_image_model.save()
                    elif length_of_images == 10:
                        hotel_image_model.img1 = images[0]
                        hotel_image_model.img2 = images[1]
                        hotel_image_model.img3 = images[2]
                        hotel_image_model.img4 = images[3]
                        hotel_image_model.img5 = images[4]
                        hotel_image_model.img6 = images[5]
                        hotel_image_model.img7 = images[6]
                        hotel_image_model.img8 = images[7]
                        hotel_image_model.img9 = images[8]
                        hotel_image_model.img10 = images[9]
                        hotel_image_model.save()
                messages.success(request, "Successfully updated!")
                return redirect('apHotelList')
        except:
            messages.warning(request, "Something wrong! Try again!")
            return redirect('apHotelList')

    context = {
        'current_pk' : pk,
        'current_obj': current_obj,
    }
    return render(request, 'backEnd_superAdmin/update_hotel_info.html', context)



# deals section starts*****************************************
# @login_required(login_url='/ap/login/register')
def ap_add_deals(request):

    if request.method == 'POST':
        title = request.POST.get("title")
        promocode = request.POST.get("promocode")
        brand_name = request.POST.get("brand_name")
        terms_coditions = request.POST.get("terms_coditions")
        brand_logo = request.FILES['brand_logo']

        if title and promocode and brand_logo and brand_name and terms_coditions:
            deals_model = Deals(title=title, promocode=promocode, brand_name=brand_name, terms_condition=terms_coditions, logo=brand_logo)
            deals_model.save()
            messages.success(request, "Successfully added!")
            return redirect('apAddDeal')

    return render(request, 'backEnd_superAdmin/add_deal.html')

# @login_required(login_url='/ap/login/register')
def ap_deal_list(request):

    # deals list
    deals_list = Deals.objects.all()

    context = {
        'deals_list' : deals_list,
    }
    return render(request, 'backEnd_superAdmin/deals_list.html', context)

# @login_required(login_url='/ap/login/register')
def ap_del_deal(request, pk):

    try:
        fs = FileSystemStorage()
        current_deal = Deals.objects.get(pk=pk)
        fs.delete(current_deal.logo.name)
        current_deal.delete()
        messages.success(request, "Successfully deleted!")
        return redirect('apDealList')
    except:
        messages.warning(request, "Can't be deleted! Try again!")
        return redirect('apDealList')
    return redirect('apDealList')


# @login_required(login_url='/ap/login/register')
def ap_update_deal(request, pk):

    current_obj = Deals.objects.get(pk=pk)

    if request.method == 'POST':
        title = request.POST.get("title")
        promocode = request.POST.get("promocode")
        brand_name = request.POST.get("brand_name")
        terms_coditions = request.POST.get("terms_coditions")


        if title and promocode and brand_name and terms_coditions:
            try:
                fs = FileSystemStorage()
                brand_logo = request.FILES['brand_logo']
                if brand_logo:
                    # deleting current logo
                    fs.delete(current_obj.logo.name)

                    current_obj.title = title
                    current_obj.promocode = promocode
                    current_obj.brand_name = brand_name
                    current_obj.terms_condition = terms_coditions
                    current_obj.logo = brand_logo
                    current_obj.save()
                    messages.success(request, "Successfully added!")
                    return redirect('apDealList')
            except:
                current_obj.title = title
                current_obj.promocode = promocode
                current_obj.brand_name = brand_name
                current_obj.terms_condition = terms_coditions
                current_obj.save()
                messages.success(request, "Successfully added!")
                return redirect('apDealList')


    context = {
        'current_pk' : pk,
        'current_obj' : current_obj,
    }

    return render(request, 'backEnd_superAdmin/update_deal.html', context)











