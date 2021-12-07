import itertools

xo = "X________"    #input()
xo_join = " ".join(xo)
def print_score():
    print("---------")
    print(f"| {xo_join[0:6]}|")
    print(f"| {xo_join[6:12]}|")
    print(f"| {xo_join[12::]} |")
    print("---------")
print_score()

mylist = []
new_list = []
for i in xo:
    mylist.append(i)
for i in range(0, len(mylist), 3):
    new_list.append(mylist[i:i+3])
count = 1

while True:
    xo_string = "".join(itertools.chain(*new_list))
    print(xo_string)

    winning_tuple = [xo_string[0] + xo_string[1] + xo_string[2], 
                    xo_string[3] + xo_string[4] + xo_string[5], 
                    xo_string[6] + xo_string[7] + xo_string[8], 
                    xo_string[0] + xo_string[3] + xo_string[6], 
                    xo_string[1] + xo_string[4] + xo_string[7], 
                    xo_string[2] + xo_string[5] + xo_string[8],
                    xo_string[0] + xo_string[4] + xo_string[8], 
                    xo_string[2] + xo_string[4] + xo_string[6]]
    
    if "XXX" in winning_tuple:
        print("X wins")
        break
    elif "OOO" in winning_tuple:
        print("Y wins")
        break
    elif "XXX"  not in xo_string and "OOO" not in xo_string and "_" not in xo_string:
        print("Draw")
        break
    x, y = input("Enter the coordinates: ").split()
    try:
        x, y = int(x), int(y)
        if x in range(1,4) and y in range(1,4):
            if new_list[x-1][y-1] != "_":
                print("This cell is occupied! Choose another one!")
                continue
            else:
                if count % 2 == 1:
                    new_list[x-1][y-1] = "X" 
                    count += 1

                else:
                    new_list[x-1][y-1] = "O"
                    count += 1
        else:
            print("Coordinates should be from 1 to 3!")
    except ValueError:
        print("That's not an int!")
        continue
    
    mylist = " ".join(itertools.chain(*new_list))
    print("---------")
    print(f"| {mylist[0:6]}|")
    print(f"| {mylist[6:12]}|")
    print(f"| {mylist[12::]} |")
    print("---------")