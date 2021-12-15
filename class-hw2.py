'''
Задание № 2. 
Атрибуты и взаимодействие классов.
В квизе к предыдущей лекции мы реализовали возможность выставлять студентам оценки за домашние задания.
Теперь это могут делать только Reviewer (реализуйте такой метод)!

А что могут делать лекторы? Получать оценки за лекции от студентов :)

Реализуйте метод выставления оценок лекторам у класса Student 
(оценки по 10-балльной шкале, хранятся в атрибуте-словаре у Lecturer, 
в котором ключи – названия курсов, а значения – списки оценок).

Лектор при этом должен быть закреплен за тем курсом, на который записан студент.
'''


class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

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
    grades = {}

    pass


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


me = Student('Masha', 'Bimatova', 'F')
me.courses_in_progress += ['Python']

jay = Student('Jay', 'Javovich', 'M')
jay.courses_in_progress += ['Java']

r = Reviewer('Pasha', 'Proveryalkin')
r.courses_attached += ['Python', 'Java']
r.rate_hw(me, 'Python', 10)
r.rate_hw(me, 'Python', 9)
r.rate_hw(jay, 'Python', 5) # error

print("Grades of Masha: ")
print(me.grades)

print("Grades of Jay:")
print(jay.grades)

p = Lecturer('Vasya', 'Professorov')
p.courses_attached += ['Java']

me.rateLecturer(p, "Python", 7)
jay.rateLecturer(p, "Java", 8)

print("Grades of professor: ")
print(p.grades)
