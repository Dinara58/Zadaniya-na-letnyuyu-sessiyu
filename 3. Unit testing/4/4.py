import re
import sys

def is_correct_mobile_phone_number_ru(number):
    pattern = r'^(\+?7|8)\s?(\(\d{3}\)|\d{3})[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}$'
    return bool(re.match(pattern, number))

def check_mobile_phone_number():
    phone_number = input("Введите номер мобильного телефона: ")
    
    if is_correct_mobile_phone_number_ru(phone_number):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    check_mobile_phone_number()
