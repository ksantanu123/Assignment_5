student={'Ram':80,'Shyam':90,'Sita':70,'Gita':60}
name=input("Enter the name of the student:")
if name in student:
    print(f"{name}'s marks is {student[name]}")
else:
    print(f"{name} not found in list")