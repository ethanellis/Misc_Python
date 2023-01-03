import random
play = True

def print_grid(a):
    print(' ')
    print(f'{a[0][0]} | {a[0][1]} | {a[0][2]}')
    print('---------')
    print(f'{a[1][0]} | {a[1][1]} | {a[1][2]}')
    print('---------')
    print(f'{a[2][0]} | {a[2][1]} | {a[2][2]}')
    print(' ')

def player():
    again = True
    while again:
        print(f'player 1:')
        play = list(input('row, column: ').replace(' ','').replace(',','').strip())
        if len(play) != 2:
            print('not a valid play. try again.')
        else:
            row = int(play[0])
            col = int(play[1])
            if grid[row-1][col-1] != 'x' and grid[row-1][col-1] != 'o':
                grid[row-1][col-1] = 'x'
                AI_grid[row-1][col-1] = 1
                again = False
            else:
                print('that spot is taken. try again.')

def strat(x,y,z):
    if x[0][0] + x[0][1] + x[0][2] == z:
        if x[0][0] == 0:
            x[0][0] = -1
            y[0][0] = 'o'
        elif x[0][1] == 0:
            x[0][1] = -1
            y[0][1] = 'o'
        elif x[0][2] == 0:
            x[0][2] = -1
            y[0][2] = 'o'
        return True
            
    elif x[1][0] + x[1][1] + x[1][2] == z:
        if x[1][0] == 0:
            x[1][0] = -1
            y[1][0] = 'o'
        elif x[1][1] == 0:
            x[1][1] = -1
            y[1][1] = 'o'
        elif x[1][2] == 0:
            x[1][2] = -1
            y[1][2] = 'o'
        return True
        
    elif x[2][0] + x[2][1] + x[2][2] == z:
        if x[2][0] == 0:
            x[2][0] = -1
            y[2][0] = 'o'
        elif x[2][1] == 0:
            x[2][1] = -1
            y[2][1] = 'o'
        elif x[2][2] == 0:
            x[2][2] = -1
            y[2][2] = 'o'
        return True
        
    elif x[0][0] + x[1][0] + x[2][0] == z:
        if x[0][0] == 0:
            x[0][0] = -1
            y[0][0] = 'o'
        elif x[1][0] == 0:
            x[1][0] = -1
            y[1][0] = 'o'
        elif x[2][0] == 0:
            x[2][0] = -1
            y[2][0] = 'o'
        return True
        
    elif x[0][1] + x[1][1] + x[2][1] == z:
        if x[0][1] == 0:
            x[0][1] = -1
            y[0][1] = 'o'
        elif x[1][1] == 0:
            x[1][1] = -1
            y[1][1] = 'o'
        elif x[2][1] == 0:
            x[2][1] = -1
            y[2][1] = 'o'
        return True
        
    elif x[0][2] + x[1][2] + x[2][2] == z:
        if x[0][2] == 0:
            x[0][2] = -1
            y[0][2] = 'o'
        elif x[1][2] == 0:
            x[1][2] = -1
            y[1][2] = 'o'
        elif x[2][2] == 0:
            x[2][2] = -1
            y[2][2] = 'o'
        return True
        
    elif x[0][0] + x[1][1] + x[2][2] == z:
        if x[0][0] == 0:
            x[0][0] = -1
            y[0][0] = 'o'
        elif x[1][1] == 0:
            x[1][1] = -1
            y[1][1] = 'o'
        elif x[2][2] == 0:
            x[2][2] = -1
            y[2][2] = 'o'
        return True
        
    elif x[0][2] + x[1][1] + x[2][0] == z:
        if x[0][2] == 0:
            x[0][2] = -1
            y[0][2] = 'o'
        elif x[1][1] == 0:
            x[1][1] = -1
            y[1][1] = 'o'
        elif x[2][0] == 0:
            x[2][0] = -1
            y[2][0] = 'o'
        return True
    
    else:
        return False

            
def computer():
    count = 0 
    if(strat(AI_grid,grid,-2)):
        count += 1
    elif(strat(AI_grid,grid,2)):
        count += 1
    else:
        while count < 1:
            a = random.randint(0,2)
            b = random.randint(0,2)
            if grid[a][b] != 'x' and grid[a][b] != 'o':
                grid[a][b] = 'o'
                AI_grid[a][b] = -1
                count += 1
            else:
                continue

def check():
    winner = False
    if grid[0][0] == grid[1][0] == grid[2][0] == 'x' or grid[0][1] == grid[1][1] == grid[2][1] == 'x' or grid[0][2] == grid[1][2] == grid[2][2] == 'x' or grid[0][0] == grid[0][1] == grid[0][2] == 'x' or grid[1][0] == grid[1][1] == grid[1][2] == 'x' or grid[2][0] == grid[2][1] == grid[2][2] == 'x' or grid[0][0] == grid[1][1] == grid[2][2] == 'x' or grid[0][2] == grid[1][1] == grid[2][0] == 'x':
        print('player 1 wins!')
        winner = True
    elif grid[0][0] == grid[1][0] == grid[2][0] == 'o' or grid[0][1] == grid[1][1] == grid[2][1] == 'o' or grid[0][2] == grid[1][2] == grid[2][2] == 'o' or grid[0][0] == grid[0][1] == grid[0][2] == 'o' or grid[1][0] == grid[1][1] == grid[1][2] == 'o' or grid[2][0] == grid[2][1] == grid[2][2] == 'o' or grid[0][0] == grid[1][1] == grid[2][2] == 'o' or grid[0][2] == grid[1][1] == grid[2][0] == 'o':
        print('player 2 wins!')
        winner = True
    return winner

def catscratch(n):
    scratch = True
    a = 0
    while a < 3:
        for i in n[a]:
            if i == 0:
                scratch = False
            else:
                continue
        a += 1
    return scratch
                
while play:
    
    grid = [[' ',' ',' '],
            [' ',' ',' '],
            [' ',' ',' ']]

    AI_grid = [[0,0,0],
               [0,0,0],
               [0,0,0]]

    first = int(input('player 1 or player 2 first? player: ').strip())
    
    if first != 1 and first != 2:
        print('invalid first player. try again.')
    else:
        while True:
            if first == 1:
                print_grid(grid)
                player()
                if check():
                    print_grid(grid)
                    break
                elif catscratch(AI_grid):
                    print_grid(grid)
                    print('catscratch!')
                    break
                computer()
                if check():
                    print_grid(grid)
                    break
            elif first == 2:
                 computer()
                 if check():
                    print_grid(grid)
                    break
                 elif catscratch(AI_grid):
                    print('catscratch!')
                    print_grid(grid)
                    break
                 print_grid(grid)
                 player()
                 if check():
                    print_grid(grid)
                    break
                
        ambiguous = False
        while not ambiguous:
            play_again = input('do you want to play again? ').strip().lower()
            if play_again != 'n' and play_again != 'y':
                print('invalid answer. y or n?')
            else:
                if play_again == 'n':
                    ambiguous = True
                    play = False
                elif play_again == 'y':
                    ambiguous = True
                    continue

