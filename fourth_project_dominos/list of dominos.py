import itertools
import random

while True:
    nums = [0, 1, 2, 3, 4, 5, 6]
    combinations_object = itertools.combinations_with_replacement(nums, 2)
    combinations_object_list = list(combinations_object)
    shuffled_list = random.sample(combinations_object_list, len(combinations_object_list))
    player_1 = (shuffled_list[0:7])
    player_1 = [list(x) for x in player_1]
    computer = shuffled_list[7:14]
    computer = [list(x) for x in computer]
    rest = shuffled_list[14::]
    rest = [list(x) for x in rest]

    max_player_1 = []
    max_computer = []

    for i in player_1:
        if i[0] == i[1]:
            max_player_1.append(i)
    for i in computer:
        if i[0] == i[1]:
            max_computer.append(i)
    if max_player_1 and max_computer == []:
        continue
    
    elif max_player_1 and max_computer != []:
        if  max(max_player_1) > max(max_computer):
            domino_snake = max(max_player_1)            
            player_1.remove(max(max_player_1))
            status = "computer"
            break
        else:
            domino_snake = max(computer)
            computer.remove(max(computer))
            status = "player"
            break
    elif max_player_1 == []:
        domino_snake = max(computer)
        computer.remove(max(computer))
        status = "player"
        break
    else:
        domino_snake = max(max_player_1)            
        player_1.remove(max(max_player_1))
        status = "computer"
        break
        
# print(f'Stock pieces: {rest}')
# print(f'Computer pieces: {computer}')
# print(f'Player pieces: {player_1}')
# print(f'Domino snake: {[domino_snake]}')
# print(f'Status: {status}')


