print ("THE FIRST CONDITION")


number=float(input("Enter a Number:"))
if number>0:
    print("Positive number")
elif number<0:
    print("Negative number")
else:
    print("Zero")
##########################################################################################
print("THE SECOND CONDITION")


num=float(input("Enter the first number:"))
if num>=0 and num<=50:
    print("fair")
else:
    print("error")
##########################################################################################
print("THE THIRD CONDITION")

score = float(input("Enter your score:"))
if score > 0 and  score > 100:
    print (score)
    print("Invalid score")
elif score < 50 :
    print("You failed")
elif score > 50:
    print("You passed")
