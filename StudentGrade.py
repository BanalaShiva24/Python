'''
StudentId = int(input("Enter Student ID: "))
StudentName = input("Enter Student Name: ")
StudentPercentage = float(input("Enter Student Percentage: "))
if StudentPercentage<75 :
     print("LOW ATTENDANCE")
else:
     print("Everything is Fine")
NumberOfSubjects = int(input("Enter the number of subjects : "))
Total = 0
count = 0
while NumberOfSubjects > 0 :
    marks = int(input(f"Enter the marks scored in the subject {count+1} : "))
    prompt= input("Do you want to enter score for more subjects ? [Yes/No]\n")
    if prompt.lower()!="yes":
          break
    NumberOfSubjects -=1
    count+=1
    Total += marks
Average = int(Total)/count
if Average >= 90:
    print("Excellent")
elif Average >=70 :
    print("Good , but not super")
elif Average >=50:
    print("Try to work hard and improve u r performance")
else :
    print("Better dont study ")
print(Average)
'''
# ===========================================Student ID=========================================
Student_Id_Valid = False
while not Student_Id_Valid:
    Student_Id = input("Enter the ID of the student :")
    if Student_Id.isdigit():
        Student_Id = int(Student_Id)
        if Student_Id > 0:
            Student_Id_Valid = True
        else:
            print("Please enter positive number")
    else :
        print("Only numbers are allowed to be entered")
Complete_Id = "STU"+str(Student_Id).zfill(5)
print(f"Student ID is {Complete_Id}")

#=========================================Student Name=============================================
Student_Name_Valid = False
while not Student_Name_Valid:
    Student_Name = input("Enter the name of the Student :")
    Student_Name = Student_Name.strip().title()
    name_check = Student_Name.replace(" ","")
   # print(Student_Name)
    if  name_check.isalpha() and len(Student_Name):
        Student_Name_Valid = True
    else :
        if not name_check.isalpha():
            print("Please enter only alphabets ")
        elif len(Student_Name<=3):
            print("Enter the characters more than 3 ")

print(f"Your name is {Student_Name}")
#============================================Student E-mail============================================
Email = Student_Name.split(" ")
Student_Email = Email[0].lower()
print(Student_Email+'.'+str(Student_Id)+'@university.edu')
#===========================================Attendance Percentage======================================
Percentage_Valid = False
while not Percentage_Valid:
    Percentage = float(input("Please enter the attendance percentage: "))
    if Percentage in range(0,101) :
        Percentage_Valid = True
    else:
        print("Please enter the values between 0 and 100")
print(f"Attendance percentage of {Student_Name} is "+str(Percentage)+"%")
#==================================Subjects=============================
Subjects_Valid = False
while not  Subjects_Valid:
    No_of_Subjects = input("Enter number of subjects you need to calculate :")
    if No_of_Subjects.isdigit():
        No_of_Subjects = int(No_of_Subjects)
        if No_of_Subjects > 0:
            Subjects_Valid = True
        else:
            print("Enter positive values")
    else :
        print("Enter only numeric numbers")
print(No_of_Subjects)
#=========================Average======================================
Marks_Validity =False
count = 0
Average = 0
Total = 0
while(No_of_Subjects>count):
    Marks = input(f"Enter the marks of the subject {count+1}:")
    if Marks.isdigit():
        Marks = float(Marks)
        if Marks in range (0,101):
            Marks_Validity = True
            Total += Marks
        else :
            print("Please enter marks in range 0 to 100")
    count+=1
Average = (Total)/ count
print(f"Total marks obtained by {Student_Name} is {Total}")
print(f"Average of the marks of Student {Student_Name} is {Average}" )