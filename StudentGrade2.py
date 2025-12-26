print("="*30)
print("  LMS Grade Tracking System")
print("="*30)
# ID Verification
Student_Id_Valid = False
while not Student_Id_Valid :
    Student_Id = input("Enter your ID : ")
    if Student_Id.isdigit():
        Student_Id = int(Student_Id)
        if Student_Id > 0 :
            Student_Id_Valid = True
        else :
            print("Please Enter a Positive or Above Zero")
    else:
        print("Please enter the numeric values other characters are not allowed")

print(f"Your ID {Student_Id}")
Formatted_Id = "STU"+str(Student_Id).zfill(5)
print(Formatted_Id)

# Name Verification
Student_Name_Valid = False
while not Student_Name_Valid:
    Student_Name = input("Enter the name of the student :")
    Student_Name= Student_Name.strip().title()
    name_check = Student_Name.replace(" ","")
    if name_check.isalpha() and len(Student_Name)>=3:
        Student_Name_Valid = True
        print(f"Welcome {Student_Name}")
    else :
        if not name_check.isalpha():
            print("Name should contain only letters")
        elif len(Student_Name)<3:
            print("Name should be greater than 3 alphabets")

# E-mail Generation
name = Student_Name.split()
first_name = name[0].lower()
email = first_name+'.'+str(Student_Id)+".@gmail.com"
print(f"Your email is {email}")

# Base Course Fee

base_course_valid = False
while not base_course_valid:
    base_fee = input("Enter the value of the fee :")
    if base_fee.isdigit():
        base_fee = int(base_fee)
        if base_fee <=0:
            print("Please enter the positive number")
        else:
            base_course_valid = True
    else:
        print("Only numbers are allowed to be entered...")

# Descripiton
discount = 0
Description = input("Enter the descripition of the student").lower().strip()
if "reference" in Description :
    discount+= 5000
elif "scholarship" in Description :
    discount+=7000
elif "promo" in Description:
    discount+=3000
else:
    discount+=0
actual_fee = (base_fee- discount)
print(actual_fee)