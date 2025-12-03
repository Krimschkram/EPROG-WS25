class Student:
    __number_of_students = 0  # static attribute

    def __init__(self, name):
        self.name = name
        self.grade = None
        Student.__number_of_students += 1  # increment static attribute

    @staticmethod
    def get_number_of_students():
        return Student.__number_of_students

    def compute_grade(self, points):
        if points >= 90:
            self.grade = 'A'
        elif points >= 80:
            self.grade = 'B'
        elif points >= 70:
            self.grade = 'C'
        elif points >= 60:
            self.grade = 'D'
        else:
            self.grade = 'F'

s1 = Student("Alice")
s2 = Student("Bob")
print(f"Anzahl der Studierenden: {Student.get_number_of_students()}")