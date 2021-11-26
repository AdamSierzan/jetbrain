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
xo_tuples = [xo[0]+xo[1]+xo[2], xo[3]+xo[4]+xo[5], xo[6]+xo[7]+xo[8], 
             xo[0]+xo[3]+xo[6], xo[1]+xo[4]+xo[7], xo[2]+xo[5]+xo[8],
             xo[0]+xo[4]+xo[8], xo[2]+xo[4]+xo[6]]
print(xo_tuples)
type(xo_tuples)


x_nums = xo.count("X")
y_nums = xo.count("O")
if "XXX" in xo_tuples and "OOO" in xo_tuples  or abs(x_nums - y_nums) >= 2:
        print("Impossible")
elif "XXX"  not in xo_tuples and "OOO" not in xo_tuples and "_" not in xo_tuples:
    print("Draw")
elif "XXX"  not in xo_tuples and "OOO" not in xo_tuples:
    print("Game not finished")
elif "XXX" in xo_tuples:
    print("X wins")
elif "OOO" in xo_tuples:
    print("Y wins")

                
            
        
