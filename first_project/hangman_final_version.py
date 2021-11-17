import random
# print("H A N G M A N.")
words_list = ["python", "java", "kotlin", "javascript"]
chosen_word = list(random.choice(words_list))
chosen_word_hint = chosen_word[::] 
print("H A N G M A N.")
print()
j = 0
hint =  list(len(chosen_word_hint) * '-')
while j < 8:
    print()
    guessed_string = ''.join(hint)
    print(guessed_string)
    chosen_word_str = "".join(chosen_word)
    
    if guessed_string == chosen_word_str:
        print("You guessed the word!")
        print("You survived!")
        break
    else:
        chosen_letter = input("Input a letter:")
        if len(chosen_letter) != 1:
            print("You should input a single letter")

        elif not chosen_letter.islower():
            print("Please enter a lowercase English letter")
        
        
        elif not chosen_letter.islower():
                print("Please enter a lowercase English letter")
        elif chosen_letter in guessed_string:
                print("You've already guessed this letter")
                continue
        elif chosen_letter in chosen_word:
            for i in range(len(chosen_word)):
                if chosen_word[i] == chosen_letter:
                                    hint[i] = chosen_letter
        else:
            print("That letter doesn't appear in the word")
else:
    print("You lost!")