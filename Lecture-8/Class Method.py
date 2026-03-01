class Student:
    school = "AITS"

    @classmethod
    def change_school(cls, new_name):
        cls.school = new_name

Student.change_school("IIT")
print(Student.school)