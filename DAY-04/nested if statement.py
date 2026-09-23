var=185
if var<200:
    print("Expressions value is less than 200")
    if(var>150 and var<170):
        print("Which is greater than 150 less than 170")
    elif(var==100 or var>180):
        print("Which is equal to 100 or greater than 180")
    elif var==50:
        print("Which is 50")
    elif var<50:
        print("Expression value is less than 50")
else:
    print("Could not find true expressions")

print("Good bye!")
