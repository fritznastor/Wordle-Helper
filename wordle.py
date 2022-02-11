'------------------------------------------WORDLE_HELPER -_- -------------------------------------'
'-------------------------------------------Fritz Nastor------------------------------------------'  


'Initialized and assign all necessary variables'
all_words, word_list, letter, pos = [], [], 'f', 0

'''Opening the file with all possible five letter words to input in Wordle, 
then assigning a list to the words'''
with open('wordle_list.txt', 'r') as wl:
  all_words = wl.readlines()

'''Runs until user figures out word / no letter is inputted'''
while letter != '':

  '''
  deleting the word_list at the start everytime is necessary to keep track of all 
  current words that contain the correct letter
  '''
  del word_list[:]
  '''asks user for the letter and the color of the letter'''
  letter = input("Give me a letter: ")
  color = input("What color is the letter ( GREEN (g), YELLOW (y) , BLACK (b) ): ")
  
  '''
  if the given color is green or yellow, the program asks for which position the letter is in.
  It's necessary to give the position to sort through each word in the  'words' list
  to take out words that does not have that specific letter in it
  '''
  if color.capitalize() == 'G' or color.capitalize() == 'Y':
    pos = int(input("What position is it? (1 - 5)")) - 1
    
  ''' 
  There are 3 cases, each to handle what type of color the given letter is
  
  First case handles green letters, any word that has the letter in the exact position 
  given will be added to 'word_list', any other words are ignored

  Second case handles black letters, any word with the given letter will be ignored and every other word
  that does not contain the given letter will be added to 'word_list'

  Third case handles yellow letters, any word with the given letter no matter which position
  will be added to 'word_list'
  '''
  for word in all_words:

    if color.capitalize() == 'G':
      if word[pos] == letter:
        word_list.append(word)
  
    elif color.capitalize() == 'Y':
      if letter in word:
        if word[pos] != letter:
          word_list.append(word)

    elif color.capitalize() == 'B':
      if letter not in word:
        word_list.append(word)     
  '''
  At the end, 'words' is assigned a copy of 'word_list', which contains all possible words,
  then the user is shown all possible words of the given criteria
  '''
  all_words = word_list.copy()
  print(*word_list)

'''
As the user inputs more letters, and their positions and colors, the smaller the given list of
words to choose from is
'''  