student={
    "name":"shahid",
    "subjects":{
        "tel":98,
        "hin":90,
        "eng":94,
        "mat":95,
        "phy":92,
        "soc":91
    }
}
print(student)
print(student["subjects"])
print(student["subjects"]["eng"])

#methods
print(student.keys())
print(student.values())
print(student.items())
print(student.get("key"))

new_dict={"name":"Dhain","age":20}
student.update(new_dict)
print(student)
