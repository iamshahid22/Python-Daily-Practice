tel = int(input("Enter your tel marks: "))
hin = int(input("Enter your hin marks: "))
eng = int(input("Enter your eng marks: "))
mat = int(input("Enter your mat marks: "))
sci = int(input("Enter your sci marks: "))
soc = int(input("Enter your soc marks: "))

avg = (tel + hin + eng + mat + sci + soc) / 6

print("Average:", avg)

if 90 <= avg <= 100:
    print("Your grade is A+")
elif 80 <= avg < 90:
    print("Your grade is A")
elif 70 <= avg < 80:
    print("Your grade is B")
elif 60 <= avg < 70:
    print("Your grade is C")
elif 50 <= avg < 60:
    print("Your grade is D")
elif 40 <= avg < 50:
    print("Your grade is E")
elif 30 <= avg < 40:
    print("Your grade is F")
else:
    print("You are not fit to study")