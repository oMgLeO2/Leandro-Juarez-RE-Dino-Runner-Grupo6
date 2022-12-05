import pygame

pygame.init()


#WINDOW OF THE GAME

WIDTH = 900

HEIGHT = 600

screen = pygame.display.set_mode((WIDTH,HEIGHT))
title = pygame.display.set_caption("GAME OF DINO OF GOOGLE")

FPS = 60 #FPS FOR THE GAME LIKE 
#HOW MANY TIMES WILL RUN THAT PER SECOND

#COLORS

background_color = (73, 113, 182)

def drawing_on_screen():
    screen.fill(background_color)

    #REFRESING ALL THE TIME OF THE SCREEN FOR 
    #SHOWING THE CHANGES 
    pygame.display.update()

def game():

    clock = pygame.time.Clock()

    running = True

    while running:
        clock.tick(FPS)
        #THIS IS FOR THE EXIT FOR THE GAME 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #CALLING THE FUNCTION OF DRAWING INSIDE THE LOOP
        drawing_on_screen()

#GOOD PRACTICE FOR START 
#NAME IS THE DEFAULT OF THE ARCHIVE


if __name__ == "__main__":
     game()
