class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "D"

s1 = Student("Rishabh", 92)
s2 = Student("Aman", 78)

print(s1.name, "Grade:", s1.calculate_grade())
print(s2.name, "Grade:", s2.calculate_grade())
