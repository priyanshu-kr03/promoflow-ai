from rest_framework.decorators import api_view
from rest_framework.response import Response

from .auth import authenticate_org
from .models import Coupon
from .agents.rule_generator import generate_rule
from .agents.verification_agent import verify_coupon
from .rules.evaluator import apply_coupon


@api_view(["POST"])
def create_coupon(request):
    org = authenticate_org(request)

    code = request.data["code"]
    description = request.data["description"]

    rule = generate_rule(description)
    status, note = verify_coupon(rule)

    coupon = Coupon.objects.create(
        organization=org,
        code=code,
        description=description,
        rule_config=rule,
        status=status,
        verification_note=note
    )

    return Response({
        "organization": org.name,
        "coupon": coupon.code,
        "status": status,
        "note": note,
        "rule": rule
    })

@api_view(["POST"])
def apply_coupon_api(request):
    org = authenticate_org(request)

    code = request.data["coupon_code"]

    try:
        coupon = Coupon.objects.get(
            organization=org,
            code=code,
            status="ACTIVE"
        )
    except Coupon.DoesNotExist:
        return Response({"error": "Invalid coupon"}, status=400)

    valid, message, discount = apply_coupon(
        coupon.rule_config,
        request.data
    )

    if not valid:
        return Response({"error": message}, status=400)

    return Response({
        "message": message,
        "discount": discount,
        "final_amount": request.data["order"]["amount"] - discount
    })