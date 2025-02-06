from typing import List, Dict, Union
from persiantools.jdatetime import JalaliDate


def get_students() -> List[Dict[str, Union[str, int, float]]]:
    """
    Get students list from user input.

    Returns:
        List: List of students
    """
    students: List[Dict[str, Union[str, int, float]]] = []
    choice: str = ""
    while choice != "q":
        first_name: str = input("Enter the first name: ").capitalize()
        last_name: str = input("Enter the last name: ").capitalize()
        birth_year: int = int(input("Enter your Jalali birth year: "))
        gpa: float = float(input("Enter your GPA: "))

        students.append(
            {
                "first_name": first_name,
                "last_name": last_name,
                "birth_year": birth_year,
                "gpa": gpa,
            }
        )
        choice: str = input("Press q or Q to exit: ").lower()
    return students


def print_fullnames_upper(student_list: List[Dict[str, Union[str, int, float]]]):
    for student in student_list:
        print((student["first_name"] + " " + student["last_name"]).upper())
        print_age(student=student)


def print_age(student: Dict[str, Union[str, int, float]]):
    current_year: int = JalaliDate.today().year
    print(current_year - student["birth_year"])


def get_gpa_average(student_list: List[Dict[str, Union[str, int, float]]]) -> float:
    gpas: List[float] = []
    for student in student_list:
        gpas.append(student["gpa"])
    gpa_average: float = sum(gpas) / len(gpas)
    return gpa_average


students: List[Dict[str, Union[str, int, float]]] = get_students()

print_fullnames_upper(student_list=students)
average: float = get_gpa_average(student_list=students)
print(f"Total average is: {average}")
