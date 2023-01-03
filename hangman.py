import random

hangman=[

    """
' -----    '
' |   |    '
' |        '
' |        '  
' |        '
' |______  '
'          '
""",

   """
' -----    '
' |   |    '
' |   o    '
' |        '  
' |        '
' |______  '
'          '
""",

   """
' -----    '
' |   |    '
' |   o    '
' |   |    '  
' |        '
' |______  '
'          '
""",

   """
' -----    '
' |   |    '
' |   o    '
' |  /|    '  
' |        '
' |______  '
'          '
""",

   """
' -----    '
' |   |    '
' |   o    '
' |  /|\   '  
' |        '
' |______  '
'          '
""",

   """
' -----    '
' |   |    '
' |   o    '
' |  /|\   '  
' |  /     '
' |______  '
'          '
""",

   """
' -----    '
' |   |    '
' |   o    '
' |  /|\   '  
' |  / \   '
' |______  '
'          '
"""]

play = True

while play:

    words = ['handsome', 'dollar', 'running', 'laptop', 'python', 'phantom', 'scream', 'computer', 'lizard', 'alien', 'spaceship', 'hangman', 'jobs',
             'random', 'careful', 'delicate', 'decide', 'castle', 'utopia', 'book', 'cardboard', 'distill', 'shelf', 'skull', 'shipwreck', 'boat', 'dungeon',
             'television', 'despot', 'hardware', 'electronics', 'couch', 'worm', 'window', 'screen', 'program', 'desire', 'love', 'disaster', 'dynamic']

    selected_word = words[random.randint(0,len(words))-1]

    blank_word = '-'*len(selected_word)

    print(blank_word)

    tries = 0

    while True:

        print(hangman[tries])
        
        if '-' not in blank_word:
            print('you solved it!')
            break

        if tries > 5:
            print(f'oops! you lose. the word was {selected_word.upper()}')
            tries = 0
            break
        
        letter_guess = input('guess a letter or the word. ').lower().strip()


        if len(letter_guess) == 1:

            count = 0
            replace = 0
            
            while count <= len(selected_word) - 1:
                if selected_word[count] == letter_guess:
                    blank_word = blank_word[:count] + letter_guess + blank_word[count + 1:]
                    count += 1
                    replace += 1
                else:
                    count += 1
            print(blank_word)
            if replace == 0:
                tries += 1
                print(f'sorry. no dice. {6 - tries} tries left.')
            
        elif len(letter_guess) == len(selected_word):
            if letter_guess == selected_word:
                print('you solved it!')
                break
            else:
                print(f'sorry. not it. {6 - tries} tries left.')
                tries += 1


    ambiguous = True
    
    while ambiguous:
        repeat = input('do you want to play again? (y/n) ')
        if repeat != 'y' and repeat != 'n':
            print('invalid option. try again.')
        elif repeat == 'y':
            ambiguous = False
        else:
            ambiguous = False
            play = False
