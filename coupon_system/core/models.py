from django.db import models
import uuid

class Organization(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    api_key = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Coupon(models.Model):
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    code = models.CharField(max_length=50)
    description = models.TextField()

    rule_config = models.JSONField()
    status = models.CharField(
        max_length=20,
        choices=[
            ("ACTIVE", "Active"),
            ("NEED_INFO", "Need Info"),
            ("BLOCKED", "Blocked"),
        ],
        default="NEED_INFO"
    )

    verification_note = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("organization", "code")

    def __str__(self):
        if self.organization:
            return f"{self.organization.name} - {self.code}"
        return f"Unassigned - {self.code}"

