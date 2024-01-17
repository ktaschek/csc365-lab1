import sys

STUDENTS_FILE = "students.txt"
GRADES = 7
MAX_GPA = 4.0
MIN_GPA = 0.0


class Student:
    st_last_name: str
    st_first_name: str
    grade: str
    classroom: str
    bus: str
    gpa: str
    t_last_name: str
    t_first_name: str

    def __init__(self, st_last_name: str, st_first_name: str, grade: str, classroom: str, bus: str, gpa: str, t_last_name: str, t_first_name: str):
        self.st_last_name = st_last_name
        self.st_first_name = st_first_name
        self.grade = grade
        self.classroom = classroom
        self.bus = bus
        self.gpa = gpa
        self.t_last_name = t_last_name
        self.t_first_name = t_first_name


def query_student(students: list, last_name: str, bus: bool = False):
    for student in students:
        if student.st_last_name == last_name:
            if bus:
                print(
                    f"{student.st_last_name},{student.st_first_name},{student.bus}")
            else:
                print(f"{student.st_last_name},{student.st_first_name},{student.grade},{student.classroom},{student.t_last_name},{student.t_first_name}")


def query_teacher(students: list, last_name: str):
    for student in students:
        if student.t_last_name == last_name:
            print(f"{student.st_last_name},{student.st_first_name}")


def query_grade(students: list, grade: str, high: bool = False, low: bool = False):
    try:
        int(grade)
        if int(grade) not in range(GRADES):
            raise ValueError
        if high:
            student = max((student for student in students if student.grade ==
                          grade), key=lambda student: student.gpa)
            print(f"{student.st_last_name},{student.st_first_name},{student.gpa},{student.t_last_name},{student.t_first_name},{student.bus}")
        elif low:
            student = min((student for student in students if student.grade ==
                          grade), key=lambda student: student.gpa)
            print(f"{student.st_last_name},{student.st_first_name},{student.gpa},{student.t_last_name},{student.t_first_name},{student.bus}")
        else:
            for student in students:
                if student.grade == grade:
                    print(f"{student.st_last_name},{student.st_first_name}")
    except ValueError:
        print("Invalid Grade")


def query_bus(students: list, bus: str):
    try:
        int(bus)
        for student in students:
            if student.bus == bus:
                print(
                    f"{student.st_last_name},{student.st_first_name},{student.grade},{student.classroom}")
    except ValueError:
        print("Invalid Bus Route")


def query_average(students: list, grade: str):
    try:
        int(grade)
        if int(grade) not in range(GRADES):
            raise ValueError
        if students_in_grade := [
            student for student in students if student.grade == grade
        ]:
            average = round(sum(float(student.gpa) for student in students_in_grade) /
                            len(students_in_grade), 2)
            print(f"{grade},{average}")
        else:
            print("No students in grade")

    except ValueError as e:
        print("Invalid Grade")


def query_info(students: list):
    # count the number of students in each grade and print it
    for grade in range(GRADES):
        print(
            f"{grade}: {len([student for student in students if student.grade == str(grade)])}")


def query_quit():
    print("Exiting...")
    quit()


def parse_query(students: list, query: str):
    tokens = query.strip().split()
    if len(tokens) == 2 and tokens[0] in ["S:", "Student:"]:
        query_student(students, tokens[1])
    elif len(tokens) == 3 and tokens[0] in ["S:", "Student:"] and tokens[2] in ["B", "Bus"]:
        query_student(students, tokens[1], True)
    elif len(tokens) == 2 and tokens[0] in ["T:", "Teacher:"]:
        query_teacher(students, tokens[1])
    elif len(tokens) == 2 and tokens[0] in ["G:", "Grade:"]:
        query_grade(students, tokens[1])
    elif len(tokens) == 3 and tokens[0] in ["G:", "Grade:"] and tokens[2] in ["H", "High"]:
        query_grade(students, tokens[1], high=True)
    elif len(tokens) == 3 and tokens[0] in ["G:", "Grade:"] and tokens[2] in ["L", "Low"]:
        query_grade(students, tokens[1], low=True)
    elif len(tokens) == 2 and tokens[0] in ["B:", "Bus:"]:
        query_bus(students, tokens[1])
    elif len(tokens) == 2 and tokens[0] in ["A:", "Average:"]:
        query_average(students, tokens[1])
    elif len(tokens) == 1 and tokens[0] in ["I", "Info"]:
        query_info(students)
    elif len(tokens) == 1 and tokens[0] in ["Q", "Quit"]:
        query_quit()
    else:
        print("Invalid query")


def check_line(tokens: list) -> bool:
    if len(tokens) != 8:
        return
    if tokens[2] not in [str(i) for i in range(GRADES)]:
        # Invalid grade
        return False
    try:
        # Check if classroom is an integer
        int(tokens[3])
        # Check if bus is an integer
        int(tokens[4])
        # Check if gpa is a float
        float(tokens[5])
        if float(tokens[5]) < MIN_GPA or float(tokens[5]) > MAX_GPA:
            # Invalid gpa
            return False
    except ValueError:
        return False
    return True


def main(test_file: str = None):
    print(f"Opening {STUDENTS_FILE}...")
    try:
        with open(STUDENTS_FILE, "r") as file:
            students = []
            for [i, line] in enumerate(file):
                tokens = line.strip().split(',')
                if not check_line(tokens):
                    print(f"Invalid format on line {i + 1}")
                    return
                students.append(
                    Student(tokens[0], tokens[1], tokens[2], tokens[3], tokens[4], tokens[5], tokens[6], tokens[7]))
        print("Loaded students.txt")
        if test_file:
            print(f"Using test suite: {test_file}")
            try:
                with open(test_file, "r") as file:
                    for [i, line] in enumerate(file):
                        if line.strip() == "" or line.strip().startswith("//"):
                            continue
                        print(f"\nEnter a query: {line.strip()}")
                        parse_query(students, line.strip())
            except IOError:
                print(f"Unable to find {test_file}")
                return
            return
        while True:
            query = input("\nEnter a query: ").strip()
            parse_query(students, query)
    except IOError:
        print("Unable to find students.txt")
        return


if __name__ == '__main__':
    if len(sys.argv) == 1:
        main()
    elif len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print("Invalid number of arguments")
