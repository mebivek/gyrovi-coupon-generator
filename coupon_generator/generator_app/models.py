from django.db import models
from django.db import models
from django.utils import timezone
from datetime import timedelta

coupon_types = (
    ("percentage", "%"),
    ("value", "$")
)

class Coupon(models.Model):
    name = models.CharField(max_length=200, unique=True)
    expiry_date = models.DateTimeField()
    is_redeemed = models.BooleanField(default=False)
    discount_type = models.CharField(choices=coupon_types, max_length=50)
    discount_value = models.FloatField()
    created_at = models.DateTimeField(default=timezone.now)


    def save(self, *args, **kwargs) -> None:
        if not self.expiry_date:
            self.expiry_date = timezone.now() + timedelta(days=30)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}-{self.discount_value}-{self.discount_type}" 