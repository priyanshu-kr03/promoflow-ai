def apply_coupon(rule, payload):
    order_amount = payload["order"]["amount"]

    if order_amount < rule["min_order"]:
        return False, "Order amount too low", 0

    discount = 0

    if rule["discount_type"] == "percentage":
        discount = (rule["value"] / 100) * order_amount
        discount = min(discount, rule["max_discount"])

    return True, "Coupon applied", int(discount)
