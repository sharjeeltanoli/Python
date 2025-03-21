#Conditional Statement
age : int = 16
weight : int = 70

if ( age >= 18 and weight >= 50):
    print("You are eligible to donate blood")
else:
    print("You are not eligible to donate blood")


percentage : int = 1

if (percentage <= 100 and percentage >= 86):
    print("You Garade is A+")
elif (percentage <= 85 and percentage >= 71):
    print("You Garade is A")
elif (percentage <= 70 and percentage >= 61):
    print("You Garade is B")
elif (percentage <= 60 and percentage >= 41):
    print("You Garade is C")
elif (percentage <= 40 and percentage >= 1):
    print("You are Fail")
else:
    print("Percentage is not valid")



ishungry : bool = True
burger_lover : bool = True
pizza_lover : bool = False

if (ishungry and ( burger_lover or pizza_lover)):
    print("You can eat")
else:
    print("You can not eat")
