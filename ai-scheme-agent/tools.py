import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCHEME_PATH = os.path.join(BASE_DIR, "schemes.json")

with open(SCHEME_PATH, "r", encoding="utf-8-sig") as f:
    SCHEMES = json.load(f)


def eligibility_tool(memory):
    eligible = []

    age = memory.get("age")
    income = memory.get("income")
    category = memory.get("category")

    if age is None or income is None or category is None:
        return eligible

    for s in SCHEMES:
        if not (s["min_age"] <= age <= s["max_age"]):
            continue
        if income > s["max_income"]:
            continue
        if category not in s["eligible_categories"]:
            continue

        eligible.append(s)

    return eligible


def scheme_info_tool(scheme):
    return (
        f"आप {scheme['name']} के लिए पात्र हैं। "
        f"आवेदन लिंक है {scheme['link']}"
    )
