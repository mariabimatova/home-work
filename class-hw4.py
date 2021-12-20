'''
Задание № 4. Полевые испытания
Создайте по 2 экземпляра каждого класса, 
вызовите все созданные методы, а также реализуйте две функции:

для подсчета средней оценки за домашние задания
 по всем студентам в рамках конкретного курса 
 (в качестве аргументов принимаем список студентов и название курса);
для подсчета средней оценки за лекции всех лекторов в рамках курса
 (в качестве аргумента принимаем список лекторов и название курса).
'''


def calcAvgGrade(grades):
    grades_list = []
    for k, v in grades.items():
        for i in v:
            grades_list.append(i)

    sum = 0
    for i in grades_list:
        sum = sum + i

    if len(grades_list) > 0:
        average_grade = sum / len(grades_list)
    else:
        average_grade = 0
    return average_grade


def calcAverageGradeForCourse(people, course):
    count = 0
    grade_sum = 0
    for p in people:
        if course in p.grades:
            grades_list = p.grades[course]
            if len(grades_list) > 0:
                avg = sum(grades_list) / len(grades_list)
                grade_sum = grade_sum + avg
                count = count + 1

    if count > 0:
        average_grade = grade_sum / count
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

jay = Student('Jay', 'Zmeev', 'M')
jay.courses_in_progress += ['Python']

r = Reviewer('Pasha', 'Proveryalkin')
r.courses_attached += ['Python', 'Java']
r.rate_hw(me, 'Python', 10)
r.rate_hw(me, 'Python', 9)
r.rate_hw(jay, 'Python', 5)

r2 = Reviewer('Mary', 'Checker')
r2.courses_attached += ['Python']
r2.rate_hw(jay, 'Python', 10)
r2.rate_hw(jay, 'Python', 9)

p1 = Lecturer('Vasya', 'Professorov')
p1.courses_attached += ['Python']

p2 = Lecturer('Lena', 'Docentova')
p2.courses_attached += ['Python']

me.rateLecturer(p1, "Python", 7)
jay.rateLecturer(p1, "Python", 8)
jay.rateLecturer(p1, "Python", 7)
jay.rateLecturer(p2, "Python", 9)
jay.rateLecturer(p2, "Python", 7)

print("\n*** Printing reviewer r: ")
print(r)

print("\n*** Printing reviewer r2: ")
print(r2)

print(f"\n*** Printing professor: {p1.name}")
print(p1)

print(f"\n*** Printing professor: {p2.name}")
print(p2)

print("\n*** Printing me: ")
print(me)

print("\n*** Printing jay:")
print(jay)

print("Jay < me: ", end="")
print(jay < me)

print("Me > me: ", end="")
print(me > jay)

print(f"Professor {p1.name} < professor {p2.name}: ", end="")
print(p1 < p2)

print("Average grade for students studying Python:")
g1 = calcAverageGradeForCourse([me, jay], "Python")
print(g1)

print("Average grade for professors teaching Python:")
g2 = calcAverageGradeForCourse([p1, p2], "Python")
print(g2)
