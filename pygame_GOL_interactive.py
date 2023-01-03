import pygame
import random
import sys
import time

while True:
    pygame.init()

    choice = input('random or pattern? ').strip().lower()

    # side-size of grid square = scale/side
    side = 120
    scale = 600
    grid = [[0 for x in range(side)] for x in range(side)]
    grid2 = [[0 for x in range(side)] for x in range(side)]

    width = scale/side
    height = scale/side
    black = (0,0,0)
    white = (255,255,255)
    x = 0
    y = 0

    def surroundCheck(a,b,c,d,e,f,g,h,i,j):
        if grid[i][j] == 1 and a+b+c+d+e+f+g+h < 2:
            grid2[i][j] = 0
        elif grid[i][j] == 1 and a+b+c+d+e+f+g+h > 3:
            grid2[i][j] = 0
        elif grid[i][j] == 0 and a+b+c+d+e+f+g+h == 3:
            grid2[i][j] = 1
        elif grid[i][j] == 1 and a+b+c+d+e+f+g+h == 3:
            grid2[i][j] = 1
        elif grid[i][j] == 1 and a+b+c+d+e+f+g+h == 2:
            grid2[i][j] = 1

    def iterate():
        global grid
        global grid2
        for n in range(side):
            for m in range(side):
                if n == 0:
                    if m == 0:
                        #print('TL')
                        surroundCheck(grid[n][m+1], grid[n][side-1], grid[n+1][m], grid[side-1][m], grid[n+1][m+1], grid[side-1][side-1], grid[n+1][side-1], grid[side-1][m+1], n, m)
                    elif m == side - 1:
                        #print('TR')
                        surroundCheck(grid[n][m-1], grid[n][0], grid[n+1][m], grid[side-1][m], grid[n+1][0], grid[n+1][m-1], grid[side-1][0], grid[side-1][side-2], n, m)
                    else:
                        #print('T')
                        surroundCheck(grid[n][m-1], grid[n][m+1], grid[n+1][m], grid[n+1][m+1], grid[n+1][m-1], grid[side-1][m], grid[side-1][m-1], grid[side-1][m+1], n, m)
                elif n == side - 1:
                    if m == 0:
                        #print('BL')
                        surroundCheck(grid[n][m+1], grid[n][side-1], grid[n-1][m], grid[n-1][m+1], grid[n-1][side-1], grid[0][m], grid[0][m+1], grid[0][side-1], n, m)            
                    elif m == side - 1:
                        #print('BR')
                        surroundCheck(grid[n][m-1], grid[n][0], grid[n-1][m], grid[0][m], grid[0][0], grid[n-1][0], grid[0][m-1], grid[n-1][m-1], n, m)
                    else:
                        #print('B')
                        surroundCheck(grid[n][m-1], grid[n][m+1], grid[n-1][m], grid[0][m], grid[n-1][m+1], grid[n-1][m-1], grid[0][m-1], grid[0][m+1], n, m)
                elif n != 0 and n != side - 1:
                    if m == 0:
                        #print('L')
                        surroundCheck(grid[n][m+1], grid[n][side-1], grid[n-1][m], grid[n+1][m], grid[n-1][m+1], grid[n+1][m+1], grid[n+1][side-1], grid[n-1][side-1], n, m)
                    elif m == side - 1:
                        #print('R')
                        surroundCheck(grid[n][m-1], grid[n][0], grid[n-1][m], grid[n+1][m], grid[n-1][m-1], grid[n+1][m-1], grid[n+1][0], grid[n-1][0], n, m)
                    else:
                        #print('I')
                        surroundCheck(grid[n][m+1], grid[n][m-1], grid[n+1][m], grid[n-1][m], grid[n+1][m+1], grid[n+1][m-1], grid[n-1][m+1], grid[n-1][m-1], n, m)

        for a in range(side):
            for b in range(side):
                grid[a][b] = grid2[a][b]

    def run_program():  
        window = pygame.display.set_mode((scale,scale))
        pygame.display.set_caption('Game of Life') 
        global x
        global y
        global width
        global height
        run = True
        while run:
            #quit if "exit" is pressed.
            for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                    pygame.quit()
                    sys.exit()

            #fill in the display with squares based on values from grid     
            for l in range(side):
                for i in range(side):
                        if grid[l][i] == 1:
                            color = white
                        else:
                            color = black
                        pygame.draw.rect(window, color, (x,y,width,height))
                        x += width
                y += height
                x = 0
            y = 0

            #update display    
            pygame.display.update()

            #update grid
            iterate()
            #time.sleep(3)


    if choice == 'random':
        print('press esc to quit.')
        grid = [[random.randint(0,1) for x in range(side)] for x in range(side)]
        window = pygame.display.set_mode((scale,scale))
        pygame.display.set_caption('Game of Life')
        run_program()
    elif choice == 'pattern':
        #These are all the preset patterns that are hard-coded in.
        print('press esc to quit.')
        while True:
            ran_y = random.randint(0,side*(3/4))
            ran_x = random.randint(0,side*(3/4))
            select = input('glider, glider gun, blinker, beacon, toad, pulsar, or spaceship? ').strip().lower()
            if select == 'glider':
                grid[2 + ran_y][0 + ran_x] = grid[1 + ran_y][2 + ran_x] = grid[2 + ran_y][2 + ran_x] = grid[3 + ran_y][1 + ran_x] = grid[3 + ran_y][2 + ran_x] = 1
                run_program()
            elif select == 'blinker':
                grid[ran_y][ran_x] = grid[1 + ran_y][ran_x] = grid[2 + ran_y][ran_x] = 1
                run_program()
            elif select == 'beacon':
                grid[ran_y][ran_x] = grid[ran_y][1 + ran_x] = grid[1 + ran_y][ran_x] = grid[1+ran_y][1+ran_x] = grid[2+ran_y][2+ran_x] = grid[2+ran_y][3+ran_x] = grid[3+ran_y][2+ran_x] = grid[3+ran_y][3+ran_x] = 1
                run_program()
            elif select == 'toad':
                grid[ran_y][ran_x+1] = grid[ran_y][ran_x+2] = grid[ran_y][ran_x+3] = grid[ran_y+1][ran_x] =grid[ran_y+1][ran_x+1] = grid[ran_y+1][ran_x+2] = 1
                run_program()
            elif select == 'spaceship':
                grid[ran_y][1 + ran_x] = grid[ran_y][2 + ran_x] = grid[1 + ran_y][ran_x] = grid[1 + ran_y][1 + ran_x] = grid[1 + ran_y][2 + ran_x] = grid[1 + ran_y][3 + ran_x] = grid[2 + ran_y][ran_x] = grid[2 + ran_y][1 + ran_x] = grid[2 + ran_y][3 + ran_x] = grid[2 + ran_y][4 + ran_x] = grid[3 + ran_y][2 + ran_x] = grid[3 + ran_y][3 + ran_x] = 1
                run_program()
            elif select == 'pulsar':
                grid[ran_y][2 + ran_x] = grid[ran_y][3+ran_x] = grid[ran_y][4+ran_x] = grid[ran_y][8+ran_x] = grid[ran_y][9+ran_x] = grid[ran_y][10+ran_x] = grid[2+ran_y][ran_x] = grid[2+ran_y][5+ran_x] = grid[2+ran_y][7+ran_x] = grid[2+ran_y][12+ran_x] = grid[3+ran_y][ran_x] = grid[3+ran_y][5+ran_x] = grid[3+ran_y][7+ran_x] = grid[3+ran_y][12+ran_x] = grid[4+ran_y][ran_x] = grid[4+ran_y][5+ran_x] = grid[4+ran_y][7+ran_x] = grid[4+ran_y][12+ran_x] = grid[5+ran_y][2+ran_x] = grid[5+ran_y][3+ran_x] = grid[5+ran_y][4+ran_x] = grid[5+ran_y][8+ran_x] = grid[5+ran_y][9+ran_x] = grid[5+ran_y][10+ran_x] = grid[7+ran_y][2+ran_x] = grid[7+ran_y][3+ran_x] = grid[7+ran_y][4+ran_x] = grid[7+ran_y][8+ran_x] = grid[7+ran_y][9+ran_x] = grid[7+ran_y][10+ran_x] = grid[8+ran_y][ran_x] = grid[8+ran_y][5+ran_x] = grid[8+ran_y][7+ran_x] = grid[8+ran_y][12+ran_x] = grid[9+ran_y][ran_x] = grid[9+ran_y][5+ran_x] = grid[9+ran_y][7+ran_x] = grid[9+ran_y][12+ran_x] = grid[10+ran_y][ran_x] = grid[10+ran_y][5+ran_x] = grid[10+ran_y][7+ran_x] = grid[10+ran_y][12+ran_x] = grid[12+ran_y][2+ran_x] = grid[12+ran_y][3+ran_x] = grid[12+ran_y][4+ran_x] = grid[12+ran_y][8+ran_x] = grid[12+ran_y][9+ran_x] = grid[12+ran_y][10+ran_x] = 1
                run_program()
            elif select == 'glider gun':
                grid[0][25] = grid[1][25] = grid[1][24] = grid[1][23] = grid[1][22] = grid[1][30] = grid[2][24] = grid[2][23] = grid[2][22] = grid[2][21] = grid[2][30] = grid[2][13] = grid[3][24] = grid[3][21] = grid[3][14] = grid[3][12] = grid[3][34] = grid[3][35] = grid[4][24] = grid[4][23] = grid[4][22] = grid[4][21] = grid[4][34] = grid[4][35] = grid[4][16] = grid[4][15] = grid[4][11] = grid[5][24] = grid[5][25] = grid[5][23] = grid[5][22] = grid[5][16] = grid[5][15] = grid[5][11] = grid[5][1] = grid[5][0] = grid[6][25] = grid[6][16] = grid[6][15] = grid[6][11] = grid[6][1] = grid[6][0] = grid[7][14] = grid[7][12] = grid[8][13] = 1
                run_program()
            else:
                print('invalid input. try again.')
