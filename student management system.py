#-------STUDENT MANAGEMENT SYSTEM-------
student = []
def register_student():
    name = input("Enter student name:")
    math = int(input("Enter math score:"))
    science = int(input("Enter science score:"))
    english = int(input("Enter english score:"))
    student_data ={
        "name": name,
        "math": math,
        "science": science,
        "english": english,
        "average": 0,
        "grade": ""
    }
    student.append(student_data)
    print("Student data recorded succesfully!")

#--------AVERAGE SCORE--------
def average_score(student_data):
    name = input("Enter student name:")
    for student_data in student:
        if student_data["name"] == name:
            average = (student_data["math"] + student_data["science"] + student_data["english"]) / 3
            print(f"{name}'s average score is: {average}")
            return
    print("Student not found")

#--------ASSIGN GRADES--------
def grades(student_data):
    name= input("Enter student name")
    for student_data in student:
        if student_data["name"]== name:
            student_grade = student_data["grade"]
        elif 80 <= student_data["average"] <=100:
            student_data["grade"] = "A"
            print(f"{name}, Your grade is {student_grade}")
        elif 60<=student_data["average"] <=79:
            student_data["grade"]="B"
            print(f"{name}, Your grade is {student_grade}")
        elif 59<= student_data["average"] <= 59:
            student_data["grade"]= "C"
            print(f"{name}, Your grade is {student_grade}")
        else:
              print("You have failed!") 
            
    student.append(student_data)    


#---------STUDENTS RESULTS---------
def results(student_data):
    result_data = f"""
---------RESULTS REPORT----------
NAME : {student["name"]}
SUBJECT MARKS : Math : {student["math"]}
                Science : {student["science"]}
                English: {student["science"]}
AVERAGE SCORE: {student["average"]}
GRADE: {student["grade"]}
---------END OF REPORT----------- """
    print(result_data)

#--------MULTIPLE STUDENT SCORES-------
students=[]
def students_records(students_data):
    for student in students_data:
        student = students_data[student]
        name = input("Enter student name:")
        average = int(input("Enter  average score:"))
        grade = input("Enter student grade:")
        students_data ={
          { "name": name,"average score": average,"grade": grade}, 
        }
    students.append(students_data)
    print("Student records stored successfully!")

#---------BEST STUDENT--------
def best_student(students_data):
    best_student = max(students["average"])
    print(f"The {best_student} is {students["name"]} with an average score of {students["average"]}")
    
#--------THE SYSTEM------------
def system():
    while True:
        print("Welcome to the Student Management System")
        print("1.Register Student")
        print("2.Average Score")
        print("3.Grades")
        print("4.Results")
        print("5.Students Records")
        print("6.Best Student")
        print("7.Exit")

        choice = input("Enter your choice:")

        if choice == "1":
            register_student()
        elif choice == "2":
            average_score()     
        elif choice == "3":
            grades()
        elif choice == "4":
            results()
        elif choice == "5":
            students_records()
        elif choice == "6":
            best_student()
        elif choice == "7":
            print("You have exited from the system!")
            break
        else:
            print("Invalid choice, try again")
        
if __name__=="__system__":
    system()







