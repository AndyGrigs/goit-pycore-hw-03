import re

def normalize_phone(phone):
    digits = re.sub(r'\D', '', phone)
    if digits.startswith('0'):
        normalized = '+380' + digits[1:]
    elif digits.startswith('380'):
        normalized = '+' + digits
    else:
        normalized = '+380' + digits

    return normalized

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери:", sanitized_numbers)