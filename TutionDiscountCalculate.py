name= input("Enter your Student name: ")
gradeLevel= int(input("Enter your Grade Level(1-12): "))
if gradeLevel < 1 or gradeLevel > 12:
    print("Invalid Grade Level")
    exit()
tuitionFee= float(input("Enter your Tuition Fee: "))
academicTopper = input("Are you an Academic Topper? (yes/no): ").strip().lower()
if academicTopper not in ['yes', 'no']:
    print("Invalid input for Academic Topper")
    exit()

discount = 0.0
if gradeLevel >= 1 and gradeLevel <= 5:
    discount = 0.00
elif gradeLevel >= 6 and gradeLevel <= 8:    
    discount = 0.05 
elif gradeLevel >= 9 and gradeLevel <= 12:
    if academicTopper == 'yes':
        discount = 0.20
    else:
        discount = 0.10
match gradeLevel:
    case 10:
        discount += 0.03 
    case 12: 
        discount += 0.05  
discountAmount = tuitionFee * discount
finalTuitionFee = tuitionFee - discountAmount
print(f"Final Tuition Fee for {name} of Grade {gradeLevel} is :", finalTuitionFee)
