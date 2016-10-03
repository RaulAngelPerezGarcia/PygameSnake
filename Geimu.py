#Import the pygame library
import pygame

#Imports time counting package, clock and calendar 
import time

#Initialize pygame module
pygame.init()

#Several variables

clock = pygame.time.Clock() 
FPS = 60
window_w = 1280
window_h = 800

#Colors RGB
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255,0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
purple = (255, 0, 255)

headsize = 10 

#Game resolution mode, several parameters can be added
gamedisplay = pygame.display.set_mode((window_w, window_h))

#Gamewindow caption
pygame.display.set_caption("Geimu") 

#Dislay messages outside of game with form, def _name_ (message, color rgb)
font = pygame.font.SysFont(None, 25)

def message_to_screen(msg, color):

    screen_text = font.render(msg, True, color) #(message, antialias, color rgb if antialias true)
    gamedisplay.blit(screen_text, [window_w/3, window_h/4]) #(text, position in window)


#Game exiting loop
def gameloop():

    head_x = window_w/2 - headsize #Middle of the screen 
    head_y = window_h/2 - headsize 
    head_x_change = 0 #Speed of the snake (change of the movement)
    head_y_change = 0
    geimuexit = False #Game exiting variable
    gameover = False #Game menu (after loosing) 

    while not geimuexit:
        while gameover == True:
            gamedisplay.fill(black)
            message_to_screen('You lost, Press (n) to start a new game or (Esc) to quit', red)
            pygame.display.update()

            for event in pygame.event.get():
                print(event) #This shows all events ocurring in the game window to the shell
                if event.type == pygame.KEYDOWN: #Key mapping for game menu
                    if event.key == pygame.K_ESCAPE:
                        geimuexit = True
                        gameover = False
                    if event.key == pygame.K_n:
                        gameloop()

            
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Pressing x button exits the game
                    geimuexit = True
            if event.type == pygame.KEYDOWN: #Key movement mapping        
                if event.key == pygame.K_LEFT:
                        head_x_change = -headsize
                        head_y_change = 0 #Avoids diagonal movement when the subsequent keypress changes the axis of movemet
                elif event.key == pygame.K_RIGHT:
                        head_x_change = headsize
                        head_y_change = 0
                elif event.key == pygame.K_UP:
                        head_y_change = -headsize
                        head_x_change = 0
                elif event.key == pygame.K_DOWN:
                        head_y_change = headsize
                        head_x_change = 0
                        
        if head_x >= window_w or head_x < 0 or head_y >= window_h or head_y < 0:
            gameover = True

        head_x += head_x_change
        head_y += head_y_change
        gamedisplay.fill(black)
        pygame.draw.rect(gamedisplay, white, [head_x, head_y, headsize, headsize]) #Draws a rectangle by drawing over the black screen params(screen var, color rgb, [x, y, pixx, pixy])
        #gamedisplay.fill(red, rect = [240, 90, 10, 10]) Draws a rectangle by changing the color of the screen background at the determined coordinates (color rgb, shape = [x, y, pixx, pixy])
        pygame.display.update()  #Updates the game window only after all the changes have been done,if not it updates everything as it comes up. Ineficient, so therefore this command
        clock.tick(FPS)

    #Ending pygame module
    pygame.quit()

    #Dont know what thid does really
    quit() 

gameloop()


    
        
'''            
To make the snake appear in the center (instant restart of game after loose) when it reaches the end of the game window                      
if head_x >= window_w or head_x < 0 or head_y >= window_h or head_y < 0: 
head_x_change = 0
head_y_change = 0
head_x = window_w/2 - headsize 
head_y = window_h/2 - headsize       
'''

        
