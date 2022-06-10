

from pydantic import ValidationError as PydanticError
from coupon_generator.response import error_json_response
from coupon_generator.constants import ERROR_INVALID_BODY_INPUT, ERROR_UNKNOWN, ERROR_COUPON_NOT_FOUND
from .models import Coupon


class CustomException(Exception):
    def __init__(self, message, status_code=400):
        self.message = message
        self.status_code = status_code
        super().__init__()

def error_handler(func):
    def validate(*args, **kwargs):
        try:
            to_return = func(*args, **kwargs)
        except PydanticError as err:
            return error_json_response(
                ERROR_INVALID_BODY_INPUT, status_code=400
            )
        except CustomException as e:
            return error_json_response(e.message, status_code=e.status_code)
        except Coupon.DoesNotExist:
            return error_json_response(ERROR_COUPON_NOT_FOUND, status_code=404)
        except Exception as e:
            print("exc", str(e))
            return error_json_response(
                ERROR_UNKNOWN
            )
        else:
            return to_return
    return validate