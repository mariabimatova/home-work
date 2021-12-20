'''Задание № 3. Полиморфизм и магические методы
Перегрузите магический метод __str__ у всех классов.
У проверяющих он должен выводить информацию в следующем виде:

print(some_reviewer)
Имя: Some
Фамилия: Buddy

У лекторов:
print(some_lecturer)
Имя: Some
Фамилия: Buddy
Средняя оценка за лекции: 9.9

А у студентов так:
print(some_student)
Имя: Ruoy
Фамилия: Eman
Средняя оценка за домашние задания: 9.9
Курсы в процессе изучения: Python, Git
Завершенные курсы: Введение в программирование

Реализуйте возможность сравнивать (через операторы сравнения)
 между собой лекторов по средней оценке за лекции и 
студентов по средней оценке за домашние задания.'''


def calcAvgGrade(grades):
    grades_list = []
    for k, v in grades.items():
        for i in v:
            grades_list.append(i)

    sum = 0
    for i in grades_list:
        sum = sum+i

    if len(grades_list) > 0:
        average_grade = sum / len(grades_list)
    else:
        average_grade = 0
    return average_grade


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        average_grade = calcAvgGrade(self.grades)

        line1 = f"Name: {self.name}"
        line2 = f"Surname: {self.surname}"
        line3 = f"Average grade: {average_grade}"
        line4 = f"Courses in progress: {self.courses_in_progress}"
        line5 = f"Finished courses: {self.finished_courses}"
        return line1 + "\n" + line2 + "\n" + line3 + "\n" + line4 + "\n" + line5

    def __lt__(self, other):
        a = calcAvgGrade(self.grades)
        b = calcAvgGrade(other.grades)
        return a < b

    def rateLecturer(self, professor, course, grade):
        if course in self.courses_in_progress:
            professor.grades.setdefault(course, [])
            professor.grades[course].append(grade)
        else:
            return "Ошибка"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        average_grade = calcAvgGrade(self.grades)

        line1 = f"Name: {self.name}"
        line2 = f"Surname: {self.surname}"
        line3 = f"Average grade: {average_grade}"
        return line1 + "\n" + line2 + "\n" + line3

    def __lt__(self, other):
        a = calcAvgGrade(self.grades)
        b = calcAvgGrade(other.grades)
        return a < b


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        line1 = f"Name: {self.name}"
        line2 = f"Surname: {self.surname}"
        return line1 + "\n" + line2


me = Student('Masha', 'Bimatova', 'F')
me.courses_in_progress += ['Python']

jay = Student('Jay', 'Javovich', 'M')
jay.courses_in_progress += ['Java']

r = Reviewer('Pasha', 'Proveryalkin')
r.courses_attached += ['Python', 'Java']
r.rate_hw(me, 'Python', 10)
r.rate_hw(me, 'Python', 9)
r.rate_hw(jay, 'Python', 5)  # error

print("Grades of Masha: ")
print(me.grades)

print("Grades of Jay:")
print(jay.grades)

p1 = Lecturer('Vasya', 'Professorov')
p1.courses_attached += ['Java']

p2 = Lecturer('Lena', 'Docentova')
p2.courses_attached += ['Java']

me.rateLecturer(p1, "Python", 7)
jay.rateLecturer(p1, "Java", 8)
jay.rateLecturer(p1, "Java", 7)
jay.rateLecturer(p2, "Java", 9)
jay.rateLecturer(p2, "Java", 7)

print("*** Printing reviewer: ")
print(r)

print(f"*** Printing professor: {p1.name}")
print(p1)

print(f"*** Printing professor: {p2.name}")
print(p2)

print("*** Printing me: ")
print(me)

print("*** Printing jay:")
print(jay)

print("Jay < me: ", end="")
print(jay < me)

print("Me > me: ", end="")
print(me > jay)

print(f"Professor {p1.name} < professor {p2.name}: ", end="")
print(p1 < p2)
