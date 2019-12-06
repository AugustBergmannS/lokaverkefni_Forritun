import pygame

pygame.init()

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20

# This sets the margin between each cell
MARGIN = 5

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(8):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(8):
            grid[row].append(0)  # Append a cell


display_width = 550
display_height = 400

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('chess bord fix')

black = (0, 0, 0)
white = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
gray = (176, 164, 164)

#chess_bord = pygame.image.load('./chess_pieces/chess_gray.png')

done = False

clock = pygame.time.Clock()


#--------------------  Game  ----------------------



while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            grid[row][column] = 1
            print("Click ", pos, "Grid coordinates: ", row, column)

    gameDisplay.fill(gray)

    for row in range(8):
        for column in range(8):
            color = white
            if grid[row][column] == 1:
                color = black
            pygame.draw.rect(gameDisplay,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])



   # gameDisplay.blit(chess_bord,(0,0))
    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
quit()
