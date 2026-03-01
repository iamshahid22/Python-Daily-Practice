class Student:
    school = "AITS"   # class variable

    def __init__(self, name):
        self.name = name   # instance variable

s1 = Student("Shahid")
s2 = Student("Rahul")

print(s1.school)
print(s2.school)