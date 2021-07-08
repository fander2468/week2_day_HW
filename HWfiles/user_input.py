# Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors

age = int(input("Please enter your age"))
if(age >= 1 and age <= 18):
    print("kids")
elif(age >= 18 and age <= 65):
    print("adults")
elif(age > 65):
    print("seniors")
else:
    print("Please enter a valid age more than 0")
    

