# angle_a = 59
# angle_b = 60
# angle_c = 60
# if angle_a == angle_b == angle_c and (angle_a and angle_b and angle_c <= 60):
#     print("The triangle is valid!")
# else:
#     print("The triangle is not valid!")



first_num = float(input())
second_num = float(input())
operation = input()

first_num_float = float(first_num)
second_num_float = float(second_num)

if operation == "+":
    print(first_num_float + second_num_float)
elif operation == "-":
    print(first_num_float - second_num_float)
elif operation == "*":
    print(first_num_float * second_num_float)
elif operation == "**":
    print(first_num_float ** second_num_float)
elif operation == "mod":
    if second_num == 0:
        print("Division by 0!")
    else:
        print(first_num % second_num)
elif operation == "div":
    if second_num == 0:
        print("Division by 0!")
    else:
        print(first_num // second_num)
elif operation == "/":   
    if second_num == 0:
        print("Division by 0!")
    else:
        print(first_num / second_num)
