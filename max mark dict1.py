n=int(input("how many students?"))
students = {}
marks = {}
for i in range(n):
    name=input(f" enter the name of students{i+1}:")	
    mark=int(input(f"enter mark of {name}:"))
    students[name]=mark
    print("\nDictionary",students)
    highest=max(students.values())
    print("the highest mark is:",highest)
    topper=max(name)
    print("topper student name :",topper)
    
    