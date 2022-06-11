
import os
from coupon_generator.settings import BASE_DIR

ALLOWED_HOSTS = ["*"]
STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
DEBUG = False