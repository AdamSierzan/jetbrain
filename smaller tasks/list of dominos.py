import itertools
from os import PathLike, set_blocking
import random

nums = [0, 1, 2, 3, 4, 5, 6]
combinations_object = itertools.combinations_with_replacement(nums, 2)
combinations_object_list = list(combinations_object)
shuffled_list = random.sample(combinations_object_list, len(combinations_object_list))
player_1 = (shuffled_list[0:6])
player_1 = [list(x) for x in player_1]
player_2 = shuffled_list[6:12]
player_2 = [list(x) for x in player_2]
rest = shuffled_list[13::]
rest = [list(x) for x in rest]

print(player_1)
print(player_2)
print(rest)
