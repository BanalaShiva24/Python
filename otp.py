
import random
generated_otp = random.randint(1000,9999)
print(generated_otp)
count = 3
while(count > 0):
    otp = int (input("Enter the OTP : "))
    if(len(str(otp)) != 4):
        print("Please Enter 4 digit OTP only")
        count-=1
        continue
    if(generated_otp == otp):
        print(" OTP got matched")
        break
    else:
        print(" OTP did not match, please try again")
    count -= 1

else:
    print("Max attempts done, try after 24 hours")