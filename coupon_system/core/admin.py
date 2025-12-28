from django.contrib import admin
from .models import Organization, Coupon

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name", "api_key", "created_at")
    readonly_fields = ("api_key", "created_at")


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ("code", "organization", "status", "created_at")
    list_filter = ("status", "organization")
    readonly_fields = ("rule_config", "verification_note", "created_at")
