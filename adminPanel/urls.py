from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [

    # login-register
    re_path(r'^ap/register/updated/$', views.ap_RegisterSuperUser, name="apSuperAdminRegister"),
    re_path(r'^ap/login/updated/$', views.ap_loginSuperUser, name="apSuperAdminLogin"),
    re_path(r'^ap/logout/super/user/$', views.logoutSuperUser, name="apLogoutSuperUser"),

    re_path(r'^index/$', views.index, name="apIndex"),
    re_path(r'^ap/home/$', views.home, name="apHome"),
    re_path(r'^ap/deactivate/user/(?P<pk>\d+)/$', views.deactivateUser, name="apDeactivateuser"),
    re_path(r'^ap/activate/user/(?P<pk>\d+)/$', views.activateUser, name="apActivateUser"),
    re_path(r'^ap/remove/user/(?P<pk>\d+)/$', views.removeUser, name="apRemoveUser"),

    # acccounts list section ***********************************
    re_path(r'^ap/seller/accounts/list/$', views.ap_seller_accounts_list, name='apsellerAccountsList'),
    re_path(r'^ap/buyer/acccounts/list/$', views.ap_buyer_accounts_list, name='apBuyerAccountsList'),
    re_path(r'^ap/staff/accounts/list/$', views.ap_staff_accounts_list, name= 'apStaffAccountsList'),

    re_path(r'^ap/add/hotel/$', views.ap_add_hotel, name="apAddHotel"),
    re_path(r'^ap/hotel/list/$', views.ap_hotel_list, name="apHotelList"),
    re_path(r'^ap/del/hotel/(?P<pk>\d+)/$', views.ap_del_hotel, name='apDeleteHotel'),
    re_path(r'^ap/update/hotel/(?P<pk>\d+)/$', views.ap_update_hotel_info, name='apUpdateHotelInfo'),

    # deal section &****************************************
    re_path(r'^ap/add/deal/$', views.ap_add_deals, name='apAddDeal'),
    re_path(r'^ap/deal/list/$', views.ap_deal_list, name='apDealList'),
    re_path(r'^ap/del/deal/(?P<pk>\d+)/$', views.ap_del_deal, name='apDelDeal'),
    re_path(r'^ap/update/deal/(?P<pk>\d+)/$', views.ap_update_deal, name='apUpdateDeal'),

]
