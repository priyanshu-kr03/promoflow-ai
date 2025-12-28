from django.urls import path
from .views import create_coupon, apply_coupon_api

urlpatterns = [
    path("coupons/create/", create_coupon),
    path("coupons/apply/", apply_coupon_api),
]
