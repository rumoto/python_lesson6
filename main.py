def average_grade_students(students_list, course):
    grades_list = []
    for student in students_list:
        if (course in student.courses_in_progress) & (course in student.grades.keys()):
            for key, value in student.grades.items():
                if key == course:
                    for grades in value:
                        grades_list += [grades]
    res_average = round(sum(grades_list) / len((grades_list)), 1)
    return res_average

def average_grade_lecturers(lecturers_list, course):
    grades_list = []
    for lecturer in lecturers_list:
        if (course in lecturer.courses_attached) & (course in lecturer.grades.keys()):
            for key, value in lecturer.grades.items():
                if key == course:
                    for grades in value:
                        grades_list += [grades]
    res_average = round(sum(grades_list) / len((grades_list)), 1)
    return res_average

def average_grade(self):
    grades_list = []
    for value in self.grades.values():
        for grades in value:
            grades_list += [grades]
    res_average = round(sum(grades_list) / len((grades_list)), 1)
    return res_average

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Студент\n' \
              f'Имя: {self.name}\nФамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задания: {average_grade(self)}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return average_grade(self) < average_grade(other)

    def __eq__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return average_grade(self) == average_grade(other)

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
        res = f'Лектор\n' \
              f'Имя: {self.name}\nФамилия: {self.surname}\n' \
              f'Средняя оценка за лекции: {average_grade(self)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return average_grade(self) < average_grade(other)

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return average_grade(self) == average_grade(other)

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
        res = f'Проверяющий\n' \
              f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

student1 = Student('Ruoy', 'Eman', 'male')
student2 = Student('Sergey', 'Remnev', 'male')
reviewer1 = Reviewer('Ivan', 'Ivanov')
reviewer2 = Reviewer('Petya', 'Petrov')
lecturer1 = Lecturer('Fedor', 'Fedorov')
lecturer2 = Lecturer('Vasya', 'Vasiliev')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['JavaScript']
student2.courses_in_progress += ['Python']
student2.courses_in_progress += ['Java']
reviewer1.courses_attached += ['Python']
reviewer1.courses_attached += ['Java']
reviewer2.courses_attached += ['JavaScript']
lecturer1.courses_attached += ['Python']
lecturer1.courses_attached += ['Java']
lecturer2.courses_attached += ['JavaScript']
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 8)
reviewer2.rate_hw(student1, 'JavaScript', 2)
reviewer1.rate_hw(student2, 'Python', 10)
reviewer1.rate_hw(student2, 'Python', 9)
reviewer1.rate_hw(student2, 'Python', 9)
reviewer1.rate_hw(student2, 'Java', 6)
student1.rate_hw(lecturer1, 'Python', 7)
student1.rate_hw(lecturer2, 'JavaScript', 1)

print(reviewer1)
print(lecturer1)
print(student1)
print(student2)
print(student1 < student2)
print(student1 == student2)

students_list = [student1, student2]
lecturers_list = [lecturer1, lecturer2]

print(f'{average_grade_students(students_list, "Python")} - средняя оценка за домашние задания по всем студентам в рамках курса Python')
print(f'{average_grade_students(students_list, "Java")} - средняя оценка за домашние задания по всем студентам в рамках курса Java')
print(f'{average_grade_students(students_list, "JavaScript")} - средняя оценка за домашние задания по всем студентам в рамках курса JavaScript')
print(f'{average_grade_lecturers(lecturers_list, "JavaScript")} - средняя оценка за лекции всех лекторов в рамках курса JavaScript')