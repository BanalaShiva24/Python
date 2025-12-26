# This is like the main heading that we don't change often so we use TUPLES

SYSTEM_INFO = ("LMS Students Portal","v1.0","Edify University")
ADMIN_INFO = ("admin@edify.ai","+91-7981854913","101")

# Display the Heading
print("="*50)
print(f"Welcome to {SYSTEM_INFO[0]} of {SYSTEM_INFO[1]} version")
print(f"Developed by {SYSTEM_INFO[2]} students")

#Store Students Info
students = {}

#Design Menu Systems file for various operations
while True:
    print("Choose an option")
    print("1 . ADD a student")
    print("2 . Modify a student")
    print("3 . Delete a student")
    print("4 . List all students")
    print("5 . Exit App")

    choice = input("Enter what u want (1-5)")
    if choice == "1":
        print("Performing choice 1 operation")
        student_Id = input("Enter the student ID:")
        if student_Id in students :
            print("Already exists in the students list ")
        else :
            name = input("Enter the name : ").strip().title()
#=================== prepare to store multiple scores=======================
            scores = []
            while True :
                score = input("Enter the score or type done").strip()
                if score == "done":
                    break
                if score.isdigit():
                    score = int(score)
                    if score in range(0,100):
                        scores.append(score)
                    else :
                        print("Invalid Score")
                else:
                    print("Please enter the numbers as input")
#========================Store unique skills=================================
            skills = set()
            while True :
                skill = input("Please enter u r skills or type done")
                if skill == "done":
                    break
                skills.add(skill.strip().title())
#--------------------Save the students detail as far-----------------------
            students [student_Id] = {"name" :name ,
                                     "scores" : score,
                                     "skills":skill }
#---------------------------------------------------------------------------
    elif choice == "2":
        print("Performing choice 2 operation")
        student_Id = input("Enter the student id that need to be updated :")
        if student_Id in students :
            new_name = input(" Enter new name : ").strip().title()
            students[student_Id] ["name"] = new_name
            print("Student updated successfully")
        else:
            print("Student ID not found : ")

    elif choice == "3":
        print("Performing choice 3 operation")
        student_Id = input("Enter the student id to delete")
        remove = students.pop(student_Id,None)
        if remove:
            print("student deleted")
        else:
            print("student id not found")

    elif choice == "4":
         print("Performing choice 4 operation")
         if not students:
            print("No student found")
         else:
             print(" all the information ")
             for sid , data in students.items():
                 name = data["name"]  # ravi
                 scores = data["scores"]  # 90,80,90

                 if scores:
                     avg = sum(scores) / len(scores)
                 else:
                     avg = 0

                 if scores:
                     top_score = max(scores)
                 else:
                     top_score = 0

                 skills = data["skills"]  # git, python

                 print(f"ID: {sid}")
                 print(f"Name: {name}")
                 print(f"Scores: {scores}")
                 print(f"Average Score: {avg}")
                 print(f"Top Score: {top_score}")
                 print(f"Skills: {skills}")
                 print(f"Skills Count: {len(skills)}")

    elif choice == "5":
        print("Performing choice 5 operation")
        print("=" * 50)
        print("Contact Admin For Further Help")
        print(f"Mobile Number {ADMIN_INFO[1]}")
        print(f"Email ID {ADMIN_INFO[0]}")
        print("=" * 50)
        break
    else:
        print("Invalid choice")