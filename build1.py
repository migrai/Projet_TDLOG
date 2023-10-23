import pygame

pygame.init()

#   Game parameters:

#Board size and number of columns / lines
length, height = 720, 720
lines, columns = 9, 9
bigSquaresThickness = 3

#Board colors
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
black = (0,0,0)

#Pop the window up
window = pygame.display.set_mode((length, height))
pygame.display.set_caption("Jeu de nom à définir")

execute = True

#Loop for executing the game
while execute == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            execute = False
    
    #Creating the board, filling the background in white
    window.fill(white)

    #Creating the squares, small and big ones
    for line in range(lines):
        for column in range(columns):
            # color = white if (line + column) % 2 == 0 else black
            pygame.draw.rect(window, black, 
                             (column * length // columns, line * height // lines, length // columns, height // lines), 1)
            if line % 3 == 0 and line > 0:
                pygame.draw.line(window, red, (0, line * (height // lines)), 
                                 (length, line * (length // lines)), bigSquaresThickness)
            if column % 3 == 0 and column > 0:
                pygame.draw.line(window, red, (column * (length // columns), 0),
                                  (column * (length // columns), height), bigSquaresThickness)
    
    pygame.display.update()