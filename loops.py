# times = int(input('How many times should I say "Hello"?'))
# for i in range(times):
#     print('Hello!')




# n = 2
# sum_1 = 0
# for n in range(n):
#     sum_1 += n
# print(sum_1 // n)

# num = 13
# nums  = []


# if num % 3 == 0:
#     nums.append(num)
#     print(nums)

a = -5
b = 12
devidible = []
for i in range(a,b):
    if i % 3 == 0:
        devidible.append(i)
print(sum(devidible) / len(devidible))

string = ""
for i in range(1, 20, 4):
    string += "&" * i

print(string)

# phone_num = 131
# phone_num_list = ["zero", "one", "two"]
# for _ in phone_num:
#     print(phone_num_list[int[_]])

# print(phone_num_list)


for _ in range(1,100):
    if _ % 5 == 0  or _ % 3 == 0:
        if _ % 5 == 0 and _ % 3 != 0:
            print("fizz")
        if _ % 5 != 0 and _ % 3 == 0:
            print("buzz")
        else:
            print("fizzbuzz")
    else:
        print(_)