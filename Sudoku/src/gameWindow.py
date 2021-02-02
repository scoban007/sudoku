from copy import deepcopy
from random import randint
import pygame, sys, sudoku, boards

board = boards.boards[randint(0,len(boards.boards)-1)]  #randomly selects a 2D sudoku array
copy = deepcopy(board)  #a deepcopy of the selected 2D sudoku array
solved = deepcopy(board)    #a deepcopy of the selected 2D sudoku array, used as the solution
sudoku.solve(solved)    #solves the "solved" array

WHITE = (255,255,255)
GREEN = (0,255,128)

def main():
    '''
    Main function that runs the Sudoku game window.
    '''
    global window, font
    pygame.init()   #Initialize game window
    font = pygame.font.SysFont('None',50)
    window = pygame.display.set_mode((630,700))
    pygame.display.set_caption("Sudoku")
    window.fill((64,64,64)) #sets the background colour of the game window
    m_pos = None    #mouse cursor position, default: None
    gridColour = WHITE  #colour of grid lines, default: White
    while True:     
        addButtons()
        drawGrid(gridColour)
        drawNumbers(board)
        pygame.display.update()
        for event in pygame.event.get():    #listen for events
            if event.type == pygame.QUIT:   #window closes when user clicks red X button
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  #user performs a left-click
                m_pos = pygame.mouse.get_pos()
                if (m_pos[1]<=629):
                    selection(m_pos)
                elif (m_pos[0]<=315):   #user clicks on solve button
                    gameSolve()
                else:                   #user clicks on reset button
                    gameReset()
            if event.type == pygame.KEYDOWN:    #user presses a key
                addNumber(m_pos,pygame.key.name(event.key))
                selection(m_pos)
        if board == solved:     #grid lines become green, indicating the puzzle is complete, otherwise, remain white
            gridColour = GREEN
        else:
            gridColour = WHITE

def selection(pos):
    '''
    Highlights the selected space.

    Argument(s):
    pos: the coordinates of the selected space on the sudoku board
    '''
    if (pos is not None) and (pos[0]<=630) and (pos[1]<=630):     #checks if a space was selected by user, and if selected coordinate is valid
        window.fill((64,64,64))
        rect = pygame.Rect(pos[0]-(pos[0]%70),pos[1]-(pos[1]%70),68,68)
        pygame.draw.rect(window,(51,153,255),rect,6)

def addNumber(pos,key):
    '''
    Adds a digit onto the board when inputted by user.

    Argument(s):
    pos: the coordinates on the sudoku board
    key: the digit to place on the board as inputted by user
    '''
    if (pos is not None) and (key.isdigit()) and (pos[0]<=630) and (pos[1]<=630):   #checks if a space was selected by user, if key pressed is a digit, and if selected coordinate is valid
        x = pos[0]-(pos[0]%70)+24
        y = pos[1]-(pos[1]%70)+19
        board[(y-19)//70][(x-24)//70] = int(key)
        window.fill((64,64,64))
        drawNumbers(board)

def drawGrid(colour):
    '''
    Draws the lines for the grid. 

    Argument(s):
    colour: the colour of the lines
    '''
    for i in range(9):
        for j in range(3):
            rect = pygame.Rect(i*210,j*210,210,210)
            pygame.draw.rect(window,colour,rect,5)
        for k in range(9):
            rect = pygame.Rect(i*70,k*70,70,70)
            pygame.draw.rect(window,colour,rect,1)

def drawNumbers(thisBoard):
    '''
    Draws the 2D Sudoku array onto the game board.

    Argument(s):
    thisBoard: the 2D Sudoku array to draw on the game board
    '''
    y = 19
    for i in thisBoard:
        x = 24
        for j in i:
            if j != 0:
                num = font.render(str(j),True,(255,255,255))
                window.blit(num,(x,y))
            x += 70
        y += 70

def gameSolve():
    '''
    Solves the puzzle and draws the solution onto the game board.
    '''
    window.fill((64,64,64))
    for i in range(len(board)):
        board[i] = deepcopy(solved[i])
    drawNumbers(board)


def gameReset():
    '''
    Resets the game to its default state. Any digits not originally
    on the board will be removed.
    '''
    window.fill((64,64,64))
    for i in range(len(board)):
        board[i] = copy[i].copy()
    drawNumbers(board)

def addButtons():
    '''
    Adds the solve and reset buttons onto the game window.
    '''
    rect = pygame.Rect(3,636,315,60)    #creates the solve button
    pygame.draw.rect(window,(0,76,153),rect,0)
    num = pygame.font.SysFont('None',30).render(str("Show solution"),True,(255,255,255))
    window.blit(num,(72,655))

    rect = pygame.Rect(322,636,305,60)  #creates the reset button
    pygame.draw.rect(window,(204,102,0),rect,0)
    num = pygame.font.SysFont('None',30).render(str("Reset"),True,(255,255,255))
    window.blit(num,(450,655))

  
main()  #to run the main function
