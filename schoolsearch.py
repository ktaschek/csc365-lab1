class Student:
  def __init__(self, st_last_name, st_first_name, grade, classroom, bus, gpa, t_last_name, t_first_name):
    self.st_last_name = st_last_name
    self.st_first_name = st_first_name
    self.grade = grade
    self.classroom = classroom
    self.bus = bus
    self.gpa = gpa
    self.t_last_name = t_last_name
    self.t_first_name = t_first_name

def query_student(students: list, last_name: str, bus: bool = False):
  if bus:
    for student in students:
      if student.st_last_name == last_name:
        print(student.st_last_name + " " + student.st_first_name + " " + student.bus)
  else:
    for student in students:
      if student.st_last_name == last_name:
        print(student.st_last_name + " " + student.st_first_name + " " + student.grade + " " + student.classroom + " " + student.t_last_name + " " + student.t_first_name)

def query_teacher(students: list, last_name: str):
  for student in students:
    if student.t_last_name == last_name:
      print(student.st_last_name + " " + student.st_first_name)


def main():
  print("Opening students.txt...")
  try:
    file = open("students.txt", "r")
    students = []
    for line in file:
      line = line.split(",")
      students.append(Student(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7]))
    print("Loaded students.txt.")
    while True:
      query = input("Enter a query: ")
      tokens = query.split(" ")
      if len(tokens) == 1 and tokens[0] in ["Q", "Quit"]:
        print("Exiting...")
        return
      elif len(tokens) >= 2 and tokens[0] in ["S", "Student"]:
        if len(tokens) >= 3 and tokens[2] in ["B", "Bus"]:
          query_student(students, tokens[1], True)
        else:
          query_student(students, tokens[1])
      else:
        print("Invalid query.")
    
  except IOError:
    print("Unable to find students.txt")
    return

if __name__ == '__main__':
  main()