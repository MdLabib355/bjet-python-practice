number1 = int(input("Enter your number out of 100 in mid: "))
number2 = int(input("Enter your number out of 100 in final: "))
avg = (number1 + number2) / 2

if (number1 == 100 or number2 == 100) or avg >= 70:
    if (number1 == 100 or number2 == 100):
        print("Perfect number on either mid or final")
    
    if avg >= 70:
        print("Passed")
    else:
        print("Failed")

