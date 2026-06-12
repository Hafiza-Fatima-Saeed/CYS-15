Students = int(input("Enter total number of students:"))
for i in range(Students):
    Student_name =input("Emter student name:")
    Roll_Number = int(input("Enter roll no:"))
    Obtained_marks = int(input("enter your marks:"))
    Total_Marks = int(input("enter total marks:"))
    print("Student name:", Student_name)
    print("Roll number:", Roll_Number)
    


    if Total_Marks <= 0 or Total_Marks > 300:
        print("enter valid numbers:")
    elif Obtained_marks > Total_Marks > 300:
        print("Enter valid numbers:")
    else:
        result = (Obtained_marks/Total_Marks) * 100
        print(result)
    if result >= 90:
        print("A+")
    elif result >= 85:
        print("A-")
    elif result >= 80:
        print("B+")
    elif result >= 75:
        print("B-")
    elif result >= 70:
        print("C+")
    elif result >= 65:
        print("C-")
    elif result >= 60:
        print("F")


