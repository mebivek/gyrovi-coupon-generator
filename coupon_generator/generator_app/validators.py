
import re
from enum import Enum
from typing import List, Optional
from datetime import datetime

class CouponType(str, Enum):
    """
        This is a coupon type enum.
    """
    PERCENTAGE = "percentage"
    VALUE = "value"


import pydantic
from pydantic import constr

class CouponBodyValidator(pydantic.BaseModel, extra=pydantic.Extra.forbid):
    name: constr(min_length=3, max_length=200)
    expiry_date: Optional[str]
    discount_type: CouponType
    discount_value: int

    @pydantic.validator("expiry_date")
    @classmethod
    def validate_datetime(cls, val):
        try:
            datetime.fromisoformat(val.replace('Z', '+00:00'))
        except:
            return False
        return True

class CouponEditBodyValidator(pydantic.BaseModel, extra=pydantic.Extra.forbid):
    name: Optional[constr(min_length=3, max_length=200)]
    expiry_date: Optional[str]
    discount_type: Optional[CouponType]
    discount_value: Optional[int]
    is_redeemed: Optional[bool]
    
    @pydantic.validator("expiry_date")
    @classmethod
    def validate_datetime(cls, val):
        try:
            datetime.fromisoformat(val.replace('Z', '+00:00'))
        except:
            return False
        return True
