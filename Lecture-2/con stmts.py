light = input("Enter light status: ").lower()

if light == "green":
    print("You can go forward..")
elif light == "yellow":
    print("You are ready to go forward.")
elif light == "red":
    print("Stop..")
else:
    print("Invalid light color")