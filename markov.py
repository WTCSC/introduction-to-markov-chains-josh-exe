import random


with open("shakespeare.txt", 'r') as file:  #----------/------------------------------------> Opens the file containing the text, and reads it
    text = file.read()  #-----------------------------/


text = text.lower() #----------------------------------------------------------------------->  Makes the entire text lowercase
words = text.split() #---------------------------------------------------------------------->  Splits the words into separate strings

transitions = {}    #----------------------------------------------------------------------->  The dictionary containing each word


for i in range(len(words) - 1): #----------------------------\
    current_word = words[i] #                                 \
    next_word = words[i + 1]    #                              |---------------------------->  Looks at each word in the text, and adds them to the dictionary if they are not already in it
    if current_word not in transitions: #                      |
        transitions[current_word] = []  #                     /
    transitions[current_word].append(next_word) #------------/


def generate_text(start_word, num_words):   #
    punctuation_search = ('.', '!', '?', ',')   #------------------------------------------->  Defines which punctuation to search for
    punctuation = ('.', '!', '?')   #------------------------------------------------------->  Defines what punctuation should be used

    current_word = start_word.lower()   #---------------------------/----------------------->  Makes every word lowercase except for the first word
    result = [current_word.capitalize()]    #----------------------/
    
    for _ in range(num_words - 1):  #--------------------------------------\
        if current_word in transitions: #                                   \
            next_word = random.choice(transitions[current_word])  #          |-------------->  Generates the words as separate strings. The word generated depends on if it appears in the text after the word prior to it
            result.append(next_word)    #                                   /
            current_word = next_word    #----------------------------------/
            
        else:
            break

    generated_text = " ".join(result)   #--------------------------------------------------->  Joins the generated words together with spaces

    generated_text = generated_text[0].upper() + generated_text[1:] #----------------------->  The first letter of the first word is capitalized.
    
    if not generated_text.endswith(punctuation_search): #-----------------/----------------->  Punctuation is added if the generated text does not have any
        generated_text += random.choice(punctuation)    #----------------/

    return (generated_text.replace(" i ", " I ")).replace('"', "")  #----------------------->  Returns the complete generated text



start_word = input("Enter a starting word: ").lower()   #----------------------------------->  Takes a word to begin the generation, and makes it lowercase
num_words = int(input("Enter the number of words to generate: "))   #----------------------->  Takes a number, which decides how many words are generated
file.close()    #--------------------------------------------------------------------------->  Closes the shakespeare.txt file

print(generate_text(start_word, num_words))