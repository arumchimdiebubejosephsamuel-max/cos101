number= int(input("Enter a number:"))
print(f"MULTIPICATION TABLE FOR {number}")
for multiplier in range (1,13):
    result=number * multiplier
    print(f"{number} x {multiplier} = {result}")
number_2 = input("Enter end to quit :")
stop="exit"
if number_2 == stop:
    print("Goodbye this program has come to an end")

