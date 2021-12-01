n = 435
last_n = n % 10
print(last_n)
string = 'str'
last_car = string[-1]
print(last_car)

n = 42
o = 42 // 10
print(o)

# A school has decided to create three new math groups and equip three 
# classrooms for them with new desks. Your task is to calculate the minimum 
# number of desks to be purchased. To do so, you'll need the following 
# information:

# The number of students in each of the three groups is known: your program 
# will receive three non-negative integers as the input. It is possible that 
# one or more of them will be zero, so you should take it into account.
# Each group will sit in its own classroom. It means that you should calculate 
# the number of desks for each classroom separately, and only then add them up!
# At most two students may sit at any desk. You are expected to output the 
# minimum number of desks to buy, so there should be as many as possible desks 
# taken by two students rather than one.
# Most probably, you'll need operations // and % in your program!

# a = 9
# numb_of_desks = (9 // 2) + (9 % 2)
# print(numb_of_desks)


b = 19
numb_of_desks = (b // 2) + (b % 2)
print(numb_of_desks)


b = "adam"
b += "s"
print(b)