import os
import json
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
Convert coupon description into structured JSON.

JSON format:
{
  "discount_type": "percentage|flat",
  "value": number,
  "min_order": number,
  "max_discount": number,
  "audience": "all|first_time"
}

Return ONLY valid JSON.
"""

def generate_rule(description: str) -> dict:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": description}
        ]
    )

    return json.loads(response.choices[0].message.content)
