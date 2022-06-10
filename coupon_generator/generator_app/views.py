
import json
import random
from django.shortcuts import render
from .models import Coupon
from django.utils import timezone
from django.http import JsonResponse
from .validators import CouponBodyValidator, CouponEditBodyValidator
from coupon_generator.response import error_json_response, success_json_response
from coupon_generator.constants import *
from .exception_handler import error_handler, CustomException

def get_available_coupons():
    now = timezone.now()
    coupons = Coupon.objects.filter(is_redeemed=False, expiry_date__gt=now)
    return coupons

def reedeem_coupon(request):
    
    available_coupons = get_available_coupons()
    context = {}
    if available_coupons.count() == 0:
        context["error"] = ERROR_COUPONS_NOT_AVAILABLE
    return render(request, 'generator_app/index.html', context)

@error_handler
def send_a_coupon(request):
    """
        Lucky draw a coupon that is not redeemed and not expired.
    """
    now = timezone.now()
    coupons = Coupon.objects.filter(is_redeemed=False, expiry_date__gt=now)
    if coupons.count() == 0:
        raise CustomException(ERROR_COUPONS_NOT_AVAILABLE)
        # return error_json_response(message=ERROR_COUPONS_NOT_AVAILABLE) # send coupon not available
    else:
        random_coupon = random.choice(list(coupons))
        random_coupon.is_redeemed = True
        random_coupon.save()
        data = {
            "type": random_coupon.discount_type, 
            "value": random_coupon.discount_value
        }
        return success_json_response("Success", data=data)   #send a coupon

@error_handler
def create_coupons(request):
    """
        Create coupons with input given
    """
    body = json.loads(request.body.decode("UTF-8"))
    validate = list(map(lambda x: CouponBodyValidator(**x), body))
    coupons_body_name = map(lambda x: x["name"], body)
    existing_coupons = Coupon.objects.filter(name__in=coupons_body_name)
    if existing_coupons.count() > 0:
        existing_coupons_names = map(lambda x: x.name, existing_coupons)
        message = ', '.join(set(existing_coupons_names))
        message = f"Coupon with name(s) '{message}' already exist."
        raise CustomException(message)
    coupons_list = []
    for item in body:
        coupon = Coupon(**item)
        coupon.save()
        coupons_list.append(coupon)
    data = list(map(lambda x: {
        "id": x.id,
        "name": x.name, 
        "expiry_date": str(x.expiry_date), 
        "discount_type": x.discount_type,
        "discount_value": x.discount_value,
        "created_at": str(x.created_at)
        }, coupons_list
    ))
    return success_json_response(message=f"{len(data)} coupon(s) created.", data=data)

@error_handler
def delete_coupon(request, coupon_id):
    """
        Delete coupons with id
    """
    coupon = Coupon.objects.filter(id=coupon_id).delete()
    return success_json_response(message="Coupon deleted successfully.")

@error_handler
def edit_coupon(request, coupon_id):
    """
        Edit coupon with given id
    """
    coupon = Coupon.objects.get(id=coupon_id)
    body = json.loads(request.body)
    CouponEditBodyValidator(**body)
    existing_coupons = Coupon.objects.filter(name=body["name"]).exclude(id=coupon_id)
    print("existing_coupons", existing_coupons)
    if existing_coupons.count() > 0:
        body_name = body["name"]
        message = f"Coupon with name '{body_name}' already exist."
        raise CustomException(message)
    coupons = Coupon.objects.filter(id=coupon_id).update(**body)
    coupon = Coupon.objects.get(id=coupon_id)
    data = {
        "id": coupon.id,
        "name": coupon.name, 
        "expiry_date": str(coupon.expiry_date), 
        "is_redeemed": coupon.is_redeemed, 
        "discount_type": coupon.discount_type,
        "discount_value": coupon.discount_value,
        "created_at": str(coupon.created_at)
    }
    return success_json_response(message=f"Coupon updated successfully.", data=data)

