import pygame

pygame.init()

#   Game parameters:

#Default oard size and number of columns / lines
length, height = 720, 720
lines, columns = 9, 9
bigSquaresThickness = 3

#Board colors
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
black = (0,0,0)

#Pop the window up
window = pygame.display.set_mode((length, height), pygame.RESIZABLE)
pygame.display.set_caption("Méta-Morpion")

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
                             (column * window.get_width() // columns, line * window.get_height() // lines, window.get_width() // columns, window.get_height() // lines), 1)
            if line % 3 == 0 and line > 0:
                pygame.draw.line(window, red, (0, line * (window.get_width() // lines)), 
                                 (window.get_width(), line * (window.get_height() // lines)), bigSquaresThickness)
            if column % 3 == 0 and column > 0:
                pygame.draw.line(window, red, (column * (window.get_width() // columns), 0),
                                  (column * (window.get_width() // columns), window.get_height()), bigSquaresThickness)
    
    pygame.display.update()