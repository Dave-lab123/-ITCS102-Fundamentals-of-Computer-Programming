age = int(input("Please input your age --->"))

if age <= 2 : 
    print("This age is considered as Infant")
elif age <= 12 :
    print("This age is considered as child")
elif age <= 19 :
    print("This age is considered as Teen")
elif age <=59:
    print("This age is considered as Adult")
elif age < 60:
    print("This age is considered as Senior")
else : age < 0 or age > 120 :
    print("This age is considered as Invalid")