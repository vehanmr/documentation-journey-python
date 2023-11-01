fnum = input("What's the first number? ")
snum = input("What's the second number? ")

if fnum > snum:
    print(f"The first number ({fnum}) is bigger.")
elif fnum < snum:
    print(f"The second number ({snum}) is bigger.")
else:
    print("The numbers are same.")
