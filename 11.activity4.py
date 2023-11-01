
score = int(input("Enter the score: "))
age = int(input("Enter age: "))

# if the score is greater than 100, it's an invalid number.
if score > 100:
    print("Invalid Number! The maximum score only can be 100.")

elif score >= 90:
    if age < 10:
        print("Grade A+")
    else:
        print("Grade A")

elif score >= 80:
    if age < 10:
        print("Grade B+")
    else:
        print("Grade B")

elif score >= 70:
    print("Grade C")

elif score >= 60:
    print("Grade D")

elif score >= 0:
    print("Grade F")

else:
    print("Invalid Number! You can't enter a value less than 0.")
