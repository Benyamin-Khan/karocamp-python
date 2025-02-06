def get_people_info() -> None:
    with open("people_data.txt", "a") as file:
        while True:
            first_name: str = input(
                "Enter the person's first name (type 'exit' to stop): "
            )
            if first_name.lower() == "exit":
                break
            last_name: str = input("Enter the person's last name: ")

            while True:
                try:
                    age: int = int(input("Enter the person's age: "))
                    if age < 0:
                        print("Age cannot be negative. Please enter a valid age.")
                    else:
                        break
                except ValueError:
                    print("Invalid input! Please enter a valid number for age.")

            file.write(f"{first_name} {last_name} {age}\n")
            print(f"Saved {first_name} {last_name}, Age: {age}.")


def display_adults() -> None:
    try:
        with open("people_data.txt", "r") as file:
            lines: list[str] = file.readlines()

            print("People older than 18:")
            for line in lines:
                first_name, last_name, age_str = line.split()
                age: int = int(age_str)

                if age > 18:
                    print(f"{first_name} {last_name}, Age: {age}")
    except FileNotFoundError:
        print("The file 'people_data.txt' does not exist.")


get_people_info()
display_adults()
