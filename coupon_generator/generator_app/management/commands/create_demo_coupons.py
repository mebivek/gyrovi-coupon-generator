from django.core.management.base import BaseCommand, CommandError
from generator_app.models import Coupon, coupon_types
import random

class Command(BaseCommand):
    help = "creates 20 coupons for demo purpose"

    def handle(self, *args, **options):
        coupon_types_value = [coupon_types[0][0], coupon_types[1][0]]
        for i in range(1, 21):
            coupon_name = f"Coupon demo {i}"
            try:
                coupon = Coupon.objects.create(
                    name = coupon_name,
                    discount_type = random.choice(coupon_types_value),
                    discount_value = i,
                    is_redeemed = False
                )
            except:
                Coupon.objects.filter(name=coupon_name).update(
                    discount_type = random.choice(coupon_types_value),
                    discount_value = i,
                    is_redeemed = False
                )
        self.stdout.write(self.style.SUCCESS('Successfully created "%s" coupons ' % 20))