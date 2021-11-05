import random
print("H A N G M A N\nThe game will be available soon.")
words_list = ["python", "java", "kotlin", "javascript"]
chosen_word = random.choice(words_list)
chosen_word_hint = chosen_word[0:3] 
chosen_word_rest_of_chars = chosen_word 

hint = (len(chosen_word) - len(chosen_word_hint)) * '-'
complete_word = chosen_word_hint + hint
print(complete_word)
player_word = input("Guess the word:")


if player_word == chosen_word:
    print("You survived!")
else:
    print("You lost!")