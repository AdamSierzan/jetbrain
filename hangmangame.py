import random
# print("H A N G M A N.")
words_list = ["python", "java", "kotlin", "javascript"]
chosen_word = list(random.choice(words_list))
chosen_word_hint = chosen_word[::] 
hint =  list(len(chosen_word_hint) * '-')


print("H A N G M A N.")
print()
j = 0
guessed_word = ""
while j < 8:
    print(''.join(hint))
    print()
    chosen_letter = input("Input a letter: ")    
    if chosen_letter in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == chosen_letter:
                hint[i] = chosen_letter
                print(i)
            print()
    else:
        print('No such letter in the word\n')
    j += 1

print("Thanks for playing!\rWe'll see how well you did in the next stage")

