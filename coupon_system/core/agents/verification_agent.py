import os
from openai import OpenAI
from core.agents.basic_checks import basic_checks

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def verify_coupon(rule):
    status, note = basic_checks(rule)
    if status:
        return status, note

    prompt = f"""
You are a coupon verification agent.

Rule:
{rule}

Respond ONLY with:
ACTIVE
NEED_INFO: reason
BLOCKED: reason
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    text = response.choices[0].message.content.strip()

    if text.startswith("ACTIVE"):
        return "ACTIVE", None
    if text.startswith("NEED_INFO"):
        return "NEED_INFO", text
    return "BLOCKED", text
