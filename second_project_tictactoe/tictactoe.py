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


xo = "012345678"
x_wins = "XXX"
y_wins = "OOO"

xo_join = " ".join(xo)
print("---------")
print(f"| {xo_join[0:6]}|")
print(f"| {xo_join[6:12]}|")
print(f"| {xo_join[12::]} |")
print("---------")

x_nums = xo.count("X")
y_nums = xo.count("O")

if 0 < x_nums >= 3 and 0 < y_nums >= 3 or abs(x_nums - y_nums) > 1:
    print("Impossible")

elif xo[0:3] == x_wins or xo[3:6] == x_wins or xo[6::] == x_wins or xo[0:-1:3] == x_wins or xo[1::3] == x_wins or xo[2::3] == x_wins or xo[0::4]  == x_wins or xo[2:-1:2] == x_wins:
    print("X wins")
elif xo[0:3] == y_wins or xo[3:6] == y_wins or xo[6::] == y_wins or xo[0:-1:3] == y_wins or xo[1::3] == y_wins or xo[2::3] == y_wins or xo[0::4]  == y_wins or xo[2:-1:2] == y_wins:

   print("O wins")

elif xo[0:3] != x_wins or xo[3:6] != x_wins or xo[6::] != x_wins or xo[0:-1:3] != x_wins or xo[1::3] != x_wins or xo[2::3] != x_wins or xo[0::4]  != x_wins or xo[2:-1:2] != x_wins:
    if "_" in xo:
        print("Game not finished")
    else:  
        print("Draw")
elif xo[0:3] != y_wins or xo[3:6] != y_wins or xo[6::] != y_wins or xo[0:-1:3] != y_wins or xo[1::3] != y_wins or xo[2::3] != y_wins or xo[0::4]  != y_wins or xo[2:-1:2] != y_wins:
    if "_" in xo:
        print("Game not finished")
    else:  
        print("Draw")



# elif xo[0:3] or xo[3:6] or xo[6::] or xo[0:-1:3] or xo[1::3] or xo[2::3] or xo[0::4] or xo[2:-1:2] == y_wins:
#     print("YWins")
# elif (xo[0:3] and xo[3:6] and xo[6::] and xo[0:-1:3] and xo[1::3] and xo[2::3] and xo[0::4] and xo[2:-1:2]) != ("XXX" or "OOO"):
#     print("Game not finished")
# elif x_nums > 2 
    










