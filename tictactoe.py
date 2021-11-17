# In this stage, your program should:

# Take a string entered by the user and print the game grid as in the previous stage.
# Analyze the game state and print the result. Possible states:
# Game not finished when neither side has three in a row but the grid still has empty cells.
# Draw when no side has a three in a row and the grid has no empty cells.
# X wins when the grid has three X’s in a row.
# O wins when the grid has three O’s in a row.
# Impossible when the grid has three X’s in a row as well as three O’s in a row, or there are a lot more X's than O's or vice versa (the difference should be 1 or 0; if the difference is 2 or more, then the game state is impossible).
# In this stage, we will assume that either X or O can start the game.

# You can choose whether to use a space or underscore _ to print empty cells.


xo = "XXXOO__O_"



xo_join = " ".join(xo)
print("---------")
print(f"| {xo_join[0:6]}|")
print(f"| {xo_join[6:12]}|")
print(f"| {xo_join[12::]} |")
print("---------")
print(xo.count("X"))


# Impossible option
x_nums = xo.count("X")
y_nums = xo.count("O")

if abs(x_nums - y_nums) >= 3:
    print("impossible")
    
elif (xo[0:3] or xo[3:6] or xo[6::] or xo[0:-1:3] or xo[1::3] or xo[2::3] or xo[0::4] or xo[2:-1:2]) != ("XXX" or "OOO"):
    if "_" in xo:
        print("Game not finished")
    else:
        print("Draw")

elif (xo[0:3] or xo[3:6] or xo[6::] or xo[0:-1:3] or xo[1::3] or xo[2::3] or xo[0::4] or xo[2:-1:2]) == ("XXX" or "OOO"):
    print("Xwins")




# if xo[0:3] or xo[3:6] or xo[6::] or xo[0:-1:3] or xo[1::3] or xo[2::3] or xo[0::4] or xo[2:-1:2] is "XXX" and "OOO" and  x_nums - y_nums > 1 or y_nums - x_nums > 1: 
#     print("impossible")
#     if xo[0:3] or xo[3:6] or xo[6::] or xo[0:-1:3] or xo[1::3] or xo[2::3] or xo[0::4] or xo[2:-1:2] is "XXX":

   





#  and "OOO" and (x_nums - y_nums) > 1 or (y_nums - x_nums) > 1:
#     print("impossible")
#     print(abs(x_nums - y_nums))

    
    
    
    








# if abs(x_nums - y_nums) <= 2 or y_nums and x_nums == 3:
#     print("impossible")


# if "_" in xo and x_nums <= 3 and y_nums <= 3:
#     print("Game not finished")


# elif abs(x_nums - y_nums) <= 2 or y_nums and x_nums == 3:
#     print("impossible")



# if xo[0:3] or xo[3:6] or xo[6:-1] or xo[0:-1:3] or xo[1:-1:3] or xo[2::3] or xo[0::4] or xo[2:-1:2] is "XXX":
#     if abs(x_nums - y_nums) <= 2 or abs(y_nums - x_nums) :
#         print("impossible")
#     if x_nums == 3:
#         print("X wins")
#     if y_nums == 3:
#         print("Y wins")

    
        
# if xo[3] and xo[4] and xo[5] == "X" or "O":
#     print("win")
# if xo[6] and xo[7] and xo[8] == "X" or "O":
#     print("win")
# if xo[0] and xo[4] and xo[8] == "X" or "O":
#     print("win")
# if xo[2] and xo[4] and xo[6] == "X" or "O":
#     print("win")
# if xo[0] and xo[3] and xo[6] == "X" or "O":
#     print("win")

# if xo[1] and xo[4] and xo[5] == "X" or "O":
#     print("win")

# if xo[2] and xo[5] and xo[8]] == "X" or "O":
#     print("win")












# win_list = [[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6],[0,3,6],[1,4,5],[2,5,8]]
# x_list = (i for i in win_list)
# print(x_list)



# xo_list = []
# for i in xo:
#     xo_list.append(i)
# xo_div = [xo_list[i:i+3] for i in range(0,len(xo_list),3)]
# print(xo_div)
# #     for j in xo_list:
# #         xo_list.append(xo_join[i])
# # print(xo_list)






