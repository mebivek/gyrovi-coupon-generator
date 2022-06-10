from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('index/', views.reedeem_coupon, name='index'),
    path('redeem/', csrf_exempt(views.send_a_coupon), name='redeem'),
    path('create/', csrf_exempt(views.create_coupons), name='create'),
    path('delete/<int:coupon_id>/', csrf_exempt(views.delete_coupon), name='delete'),
    path('edit/<int:coupon_id>/', csrf_exempt(views.edit_coupon), name='delete')
]