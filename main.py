import random as r
import stages
import numbers

# import the words file


def importfile():
    ###
    ###
    global words_content
    f = open('1-1000.txt', 'r')
    words_content = f.read().split()
    f.close()
# end

#set up the random word


def choose_rand_word(words_list):
    rand_word= str(r.choice(words_list)).lower()
    return rand_word
#end

#check if character is found in the random word
def check_letter_in_word(word, letter, word_lines):
    i=0;  j=0; global mistakes
    global already_tried_letters
    already_tried_letters.append(letter)
    for c in word:
        if c==letter:
            j+=1
            word_lines[i]=letter
        i+=1

    if j>0 :
        print(f"Right! Letter {letter} appears {j} times! ")
    else:
        print(f"Wrong! Letter {letter} doesn\'t appear in the word!")
        mistakes+=1
        print(stages.stages[len(stages.stages)-mistakes])

    return word_lines
#end

#main ----------------------------------
words_content = []
importfile()
chosen_word = choose_rand_word(words_content)
mistakes = 0
lines_word = []
already_tried_letters = []
for i in chosen_word:
    lines_word.append('_')

print("You have 7 tries to guess the word")


while lines_word.__contains__('_') and mistakes < 7:
    print(lines_word)
    letter = input("Choose a letter: ").lower()
    if len(letter) == 1 and letter != chr(13) and letter != ' ' and letter not in numbers.number and letter \
not in already_tried_letters:
        lines_word = check_letter_in_word(chosen_word,letter,lines_word)
        print("You have "+str(mistakes)+" mistakes so far!")
    elif letter in already_tried_letters:
        print("You have entered letter "+letter+" already! Try a different one!")
    else:
        print("Please type a letter!")
    print("\n")


print("\n")
if mistakes == 7:
    print("You have lost! You did "+str(mistakes)+" mistakes!")
    print(chosen_word)
else:
    print("Congrats! You managed to guess the word!")