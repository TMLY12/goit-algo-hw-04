import re
def normalize_phone(phone: str) -> str:
    normalized = re.sub(r"[^\d+]", "", phone)
    if normalized.startswith("+380"):
        return normalized
    elif normalized.startswith("380"):
        return "+" + normalized
    elif normalized.startswith("0"):
        return "+38" + normalized
    else:
        return "+38" + normalized
raw_numbers = ["067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",]
fixed_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", fixed_numbers)