import random
# print("H A N G M A N.")
words_list = ["python", "java", "kotlin", "javascript"]
chosen_word = list(random.choice(words_list))
chosen_word_hint = chosen_word[::] 
print("H A N G M A N.")
print("""Type "play" to play the game, "exit" to quit:""")
play_or_exit = input()
print()
j = 0
missed_letters = []
hint =  list(len(chosen_word_hint) * '-')
if play_or_exit == "play":
    while j < 8:
        # missed_letters = []
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
            elif chosen_letter in missed_letters:
                print("You've already guessed this letter")
            else:
                missed_letters += chosen_letter
                j += 1
                print("That letter doesn't appear in the word")
                
    else:
        print("You lost!")
    print("""Type "play" to play the game, "exit" to quit:""")
