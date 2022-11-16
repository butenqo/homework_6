
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grades = []

    def rate_lecturer(self, lecturer, course, grade):
        if grade > 0 and grade < 11:
            if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                return 'Ошибка'
   
    def average_grade(self):
        for grade in self.grades.values():
            self.average_grades += grade 
        return sum(self.average_grades)/len(self.average_grades)

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредня оценка за домашние задания: {self.average_grade()}\nКурсы в процессе обучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}')

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() < other.average_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        

class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_grades = []

    def average_grade(self):
        for grade in self.grades.values():
            self.average_grades += grade 
        return sum(self.average_grades)/len(self.average_grades)


    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредня оценка за лекции: {self.average_grade()}')

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() < other.average_grade()
           

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
        return (f'Имя: {self.name}\nФамилия: {self.surname}')
                

bad_student = Student('Jack', 'Bowie', 'men')
best_student = Student('Ruoy', 'Eman', 'your_gender')

bad_reviewer = Reviewer('Bred', 'Django')
cool_reviewer = Reviewer('Some', 'Buddy')

cool_lecturer = Lecturer('John', 'Blade')
bad_lecturer = Lecturer('Tom', 'Rot')

bad_lecturer.courses_attached += ['Java']
bad_lecturer.courses_attached += ['Ruby']
cool_lecturer.courses_attached += ['Java']
cool_lecturer.courses_attached += ['Ruby']
bad_student.courses_in_progress += ['Java']
bad_student.courses_in_progress += ['Python']
bad_student.courses_in_progress += ['Ruby']

best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Ruby']
best_student.courses_in_progress += ['Java']
best_student.finished_courses += ['PHP']
best_student.rate_lecturer(cool_lecturer, 'Java', 10)
best_student.rate_lecturer(cool_lecturer, 'Java', 6)
best_student.rate_lecturer(bad_lecturer, 'Ruby', 5)
best_student.rate_lecturer(bad_lecturer, 'Java', 5)

bad_student.courses_in_progress += ['Java']
bad_student.courses_in_progress += ['Python']
bad_student.courses_in_progress += ['Ruby']

cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Ruby']
cool_reviewer.courses_attached += ['Java']
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Java', 9)
cool_reviewer.rate_hw(best_student, 'Ruby', 8)
cool_reviewer.rate_hw(bad_student, 'Python', 7)
cool_reviewer.rate_hw(bad_student, 'Java', 6)
cool_reviewer.rate_hw(bad_student, 'Ruby', 5)

# print(bad_lecturer > cool_lecturer)
# print(bad_student > best_student)
# print(best_student)
# print(bad_lecturer)
# print(bad_reviewer)
print(bad_lecturer.grades)
print(cool_lecturer.grades)


def average_grade_student(list_students, course):
    course_grades = []
    for student in list_students:
        if course in student.grades:
            course_grades += student.grades[course]

    print(f'Средняя оценка обучающихся по курсу {course}: {sum(course_grades)/len(course_grades)}')

def average_grade_lector(list_lector, course):
    course_grades = []
    for lector in list_lector:
        if course in lector.grades:
            course_grades += lector.grades[course]

    print(f'Средняя оценка лекторов по курсу {course}: {sum(course_grades)/len(course_grades)}')


average_grade_student([bad_student, best_student], "Ruby")
average_grade_lector([bad_lecturer, cool_lecturer], "Java")