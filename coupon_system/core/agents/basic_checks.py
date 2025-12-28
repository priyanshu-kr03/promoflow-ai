def basic_checks(rule):
    if rule["discount_type"] == "percentage":
        if rule["value"] > 60:
            return "BLOCKED", "Discount above 60% is not allowed"

        if "max_discount" not in rule:
            return "NEED_INFO", "Max discount missing"

    if "min_order" not in rule:
        return "NEED_INFO", "Minimum order missing"

    return None, None
