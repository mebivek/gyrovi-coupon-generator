from .models import Coupon
from django.test import TestCase, Client
import json
def create_client():
    client = Client()
    return client

# Create your tests here.
class CouponCreateTest(TestCase):

    def setUp(self):
        self.client = create_client()

    def test_create_coupon(self):
        body_coupon_list = [
            {
                "name": "Coupon 1",
                "expiry_date": "2022-06-25T06:48:36.192Z",
                "discount_type": "percentage",
                "discount_value": 2
            },
            {
                "name": "Coupon 2",
                "discount_type": "value",
                "discount_value": 50
            },
        ]

        response = self.client.post("/coupon/create/", json.dumps(body_coupon_list), content_type='application/json')
        response_data = response.json()

        with self.subTest():
            self.assertEqual(response.status_code, 200)
        
        with self.subTest():
            self.assertEqual(len(response_data["data"]), len(body_coupon_list))

        
class CouponRedeemTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.all_coupons = []
        demo_coupons = [
            {
                "name": "Coupon 1",
                "expiry_date": "2022-06-25T06:48:36.192Z",
                "discount_type": "percentage",
                "discount_value": 2
            },
            {
                "name": "Coupon 2",
                "discount_type": "value",
                "discount_value": 50
            },
        ]
        for coupon in demo_coupons:
            coupon = Coupon.objects.create(
                name=coupon["name"],
                expiry_date = coupon.get("expiry_date"),
                discount_type = coupon["discount_type"],
                discount_value = coupon["discount_value"]
            )
            cls.all_coupons.append(coupon)
    
    def setUp(self):
        self.client = create_client()
    
    def test_redeem_coupon(self):
        response1 = self.client.get("/coupon/redeem/")
        response2 = self.client.get("/coupon/redeem/")
        response3 = self.client.get("/coupon/redeem/")
        with self.subTest():
            self.assertEqual(response1.status_code, 200)
        with self.subTest():
            self.assertEqual(response2.status_code, 200)
        with self.subTest():
            self.assertEqual(response3.status_code, 400)

    

