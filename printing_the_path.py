import itertools

xo = "X_X_O____"    #input()
xo_join = " ".join(xo)
print("---------")
print(f"| {xo_join[0:6]}|")
print(f"| {xo_join[6:12]}|")
print(f"| {xo_join[12::]} |")
print("---------")
mylist = []
new_list = []
for i in xo:
    mylist.append(i)
for i in range(0, len(mylist), 3):
    new_list.append(mylist[i:i+3])
print(new_list)
nums = range(1,4)

# while True:
#     x, y = input("Enter the coordinates: ").split()
#     try:
#         x, y = int(x), int(y)
#         if (0 > x > 3) or (0 > y > 3):
#             print("Coordinates should be from 1 to 3!")
#             continue
#         elif new_list[x-1][y-1] != "_":
#             print("This cell is occupied! Choose another one!")
#             continue
#         else:
#             new_list[x-1][y-1] = "X"
#             break
#     except ValueError:
#         print("That's not an int!")
#         continue
    

print(new_list)
mylist = ''.join(itertools.chain(*new_list))
print("".join(mylist))
        
while True:
    x, y = input("Enter the coordinates: ").split()
    try:
        x, y = int(x), int(y)
        if x and y in range(0,3):
            if new_list[x-1][y-1] != "_":
                print("This cell is occupied! Choose another one!")
                continue
            else:
                new_list[x-1][y-1] = "X" 
                break
        else:
            print("Coordinates should be from 1 to 3!")
    except ValueError:
        print("That's not an int!")
        continue

print(new_list)
mylist = ''.join(itertools.chain(*new_list))
print("".join(mylist))