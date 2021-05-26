"""
File: word_guess.py
-------------------
Fill in this comment.
"""
import random

LEXICON_FILE = "Lexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Initial number of guesses player starts with

def play_game(secret_word):
    INITIAL_GUESSES=8
    guessed_word ='-'*len(secret_word)
    flag=False
    while not flag:
    	print("The word now looks like this:",guessed_word)
    	print("you have",INITIAL_GUESSES,'guesses left')
    	letter=input("Type a single letter here, then press enter: ")
    	letter=letter.upper()
    	
    	if len(letter)==1:
    		i=0
    		if letter in secret_word:
    			while secret_word.find(letter,i)!=-1:
    				i=secret_word.find(letter,i)
    				guessed_word=guessed_word[:i]+secret_word[i]+guessed_word[i+1:]
    				i+=1
    			print("That guess is correct.")
    		else:
    			print('There are no '+str(letter)+"'s in the word.")
    			INITIAL_GUESSES-=1
    		if guessed_word==secret_word:
    			print('Congratulations, the word is: ',secret_word)
    			flag=True
    		if INITIAL_GUESSES==0:
    			print("Sorry, you lost. The secret word was: ",secret_word)
    			flag=True
    	else:
    		print("Guess should only be a single character.")
    		
    
def get_word():
    with open (LEXICON_FILE) as f:
    	text=f.readlines()
    a=[ ]
    [a.append(line.rstrip("\n")) for line in text ]
    length=len(a)
    random_number=random.randrange(length)
    secret_word=a[random_number]
    return secret_word
	

def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    secret_word=get_word()
    play_game(secret_word)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()