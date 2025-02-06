
# تابع برای تبدیل عدد رومی به عدد نرمال
def roman_to_int(roman: str) -> int:
    # دیکشنری برای معادل عددی هر حرف رومی
    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 
        'C': 100, 'D': 500, 'M': 1000
    }

    # متغیر برای ذخیره کردن نتیجه نهایی
    total = 0

    # پیمایش در حروف عدد رومی
    for i in range(len(roman)):
        # اگر حرف بعدی بزرگتر از حرف فعلی باشد، باید از آن کم کنیم
        if i + 1 < len(roman) and roman_dict[roman[i]] < roman_dict[roman[i + 1]]:
            total -= roman_dict[roman[i]]
        else:
            total += roman_dict[roman[i]]

    return total

# تست تابع با یک عدد رومی
roman_number = "MCMXCIV"  # معادل 1994 در سیستم ده‌دهی
normal_number = roman_to_int(roman_number)
print(f"عدد رومی: {roman_number} معادل: {normal_number}")
