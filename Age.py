age  = int(input("Enter your age: "))
if age < 0:
    print("Invalid age") 
elif age in range(0, 4):
    print("You are a toddler")     
elif age in range(4, 10):
    print("You are a kid")    
else:
    print("You are older than a kid")