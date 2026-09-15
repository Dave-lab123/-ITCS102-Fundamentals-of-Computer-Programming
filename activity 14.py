#activity 14
age = int(input("What is your age? "))
income = float(input("What is your yearly income? "))
collateral = input("Do you have collateral? (yes/no) ")
credit_score = int(input("What is your credit score? "))
employed = input("Are you currently employed? (yes/no) ")

if age >= 21 and employed == "yes":
    if credit_score >= 750:
        if income >= 100000 :
         print("Final rate is 4.5%")
        else:
         print("Final rate is 5.0%")
    elif 600 <= credit_score < 750: 
        if collateral == "yes":
         print("Final rate is 7.0%")
        else:
         print("Final rate is 8.0%")
    else:
     print("Credit score too low for a loan.")
else:
 print("You need to be 21 years old and employed to apply for a loan.")