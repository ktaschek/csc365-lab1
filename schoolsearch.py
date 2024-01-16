STUDENTS_FILE = "students.txt"
GRADES = 7


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


def query_bus(students: list, bus: str):
    for student in students:
        if student.bus == bus:
            print(
                f"{student.st_last_name},{student.st_first_name},{student.grade},{student.classroom}")


def query_average(students: list, grade: str):
    students_in_grade = [
        student for student in students if student.grade == grade]
    average = sum(student.gpa for student in students_in_grade) / \
        len(students_in_grade)
    print(f"{grade},{average}")


def query_info(students: list):
    students_by_grade = [
        [student for student in students if student.grade == grade] for grade in range(GRADES)]
    for grade in range(GRADES):
        print(f"Grade {grade}: {len(students_by_grade[grade])}")


def query_quit():
    print("Exiting...")
    quit()


def parse_query(students: list, query: str):
    tokens = query.strip().split()
    if len(tokens) == 2 and tokens[0] in ["S", "Student"]:
        query_student(students, tokens[1])
    elif len(tokens) == 3 and tokens[0] in ["S", "Student"] and tokens[2] in ["B", "Bus"]:
        query_student(students, tokens[1], True)
    elif len(tokens) == 2 and tokens[0] in ["T", "Teacher"]:
        query_teacher(students, tokens[1])
    elif len(tokens) == 2 and tokens[0] in ["G", "Grade"]:
        query_grade(students, tokens[1])
    elif len(tokens) == 3 and tokens[0] in ["G", "Grade"] and tokens[2] in ["H", "High"]:
        query_grade(students, tokens[1], high=True)
    elif len(tokens) == 3 and tokens[0] in ["G", "Grade"] and tokens[2] in ["L", "Low"]:
        query_grade(students, tokens[1], low=True)
    elif len(tokens) == 2 and tokens[0] in ["B", "Bus"]:
        query_bus(students, tokens[1])
    elif len(tokens) == 2 and tokens[0] in ["A", "Average"]:
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
    except ValueError:
        return False
    return True


def main():
    print(f"Opening {STUDENTS_FILE}...")
    try:
        with open(STUDENTS_FILE, "r") as file:
            students = []
            for [i, line] in enumerate(file):
                line = line.strip().split(',')
                if not check_line(line):
                    print(f"Invalid format on line {i + 1}")
                    return
                students.append(
                    Student(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7]))
        print("Loaded students.txt")
        while True:
            query = input("\nEnter a query: ")
            parse_query(students, query)
    except IOError:
        print("Unable to find students.txt")
        return


if __name__ == '__main__':
    main()
