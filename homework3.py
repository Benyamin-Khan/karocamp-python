from typing import List


# تابع برای ذخیره اطلاعات افراد در فایل
def save_to_file() -> None:
    with open("people_data.txt", "a") as file:
        while True:
            first_name: str = input(
                "Enter the person's first name (type 'exit' to stop): "
            )
            if first_name.lower() == "exit":
                break  # اگر 'exit' وارد شود، حلقه متوقف می‌شود
            last_name: str = input("Enter the person's last name: ")

            # دریافت سن با چک کردن ورودی معتبر
            while True:
                try:
                    age: int = int(input("Enter the person's age: "))
                    if age < 0:
                        print("Age cannot be negative. Please enter a valid age.")
                    else:
                        break  # اگر سن درست وارد شد، حلقه را ترک می‌کنیم
                except ValueError:
                    print("Invalid input! Please enter a valid number for age.")

            # ذخیره اطلاعات در فایل
            file.write(f"{first_name} {last_name} {age}\n")
            print(f"Saved {first_name} {last_name}, Age: {age}.")


# تابع برای خواندن فایل و نمایش افراد بالای 18 سال
def display_adults() -> None:
    try:
        with open("people_data.txt", "r") as file:
            lines: List[str] = file.readlines()  # لیست خطوط فایل

            print("People older than 18:")
            for line in lines:
                # تجزیه داده‌ها به نام، نام خانوادگی و سن
                first_name, last_name, age_str = line.split()
                age: int = int(age_str)  # تبدیل سن به عدد صحیح

                # نمایش افراد بالای 18 سال
                if age > 18:
                    print(f"{first_name} {last_name}, Age: {age}")
    except FileNotFoundError:
        print("The file 'people_data.txt' does not exist.")


# فراخوانی تابع برای ذخیره اطلاعات
save_to_file()

# فراخوانی تابع برای نمایش افراد بالای 18 سال
display_adults()
