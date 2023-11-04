# If a number is divisible by 3, print fizz
# If a number is divisible by 5, print buzz
# If a number is divisible by both, print fizzbuzz
# GOOD LUCK :)

for num in range(1, 100):
    if num % 3 == 0 and num % 5 == 0:
        print(f'fizzbuzz({num})')
    elif num % 3 == 0:
        print(f'fizz({num})')
    elif num % 5 == 0:
        print(f'buzz({num})')
    else:
        print(num)
