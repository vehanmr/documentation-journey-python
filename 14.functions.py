# # u_input = int(input("Enter an integer: "))
#
#
# def function1(u_input):
#     u_input = int(input("Enter an integer: "))
#
#     for num in range(1, u_input):
#         if num % 3 == 0 and num % 5 == 0:
#             print(f'fizzbuzz({num})')
#         elif num % 3 == 0:
#             print(f'fizz({num})')
#         elif num % 5 == 0:
#             print(f'buzz({num})')
#         else:
#             print(num)
#
#
# function1(u_input)

# u_input = int(input("Enter an integer: "))

num = int(input("Enter an integer: "))

def function1(num):
    # for num in range(1, u_input):
    if num % 3 == 0 and num % 5 == 0:
        print(f'fizzbuzz({num})')
    elif num % 3 == 0:
        print(f'fizz({num})')
    elif num % 5 == 0:
        print(f'buzz({num})')
    else:
        print(num)


function1(num)
