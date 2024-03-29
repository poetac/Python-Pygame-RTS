import pygame, sys, random
from pygame.locals import *
pygame.init()
mainClock = pygame.time.Clock()

# set up window
WINDOWWIDTH = 1200
WINDOWHEIGHT = 700
CAPTION = 'RTS SELECTION BOX TEST'
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption(CAPTION)

# set up the colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BACKGROUNDCOLOR = GREEN

# initial values
draw_new_selection_box = False
selection_completed = False
unit_size = 20

units = []
selected_units = []
units.append(pygame.Rect(500,200,unit_size, unit_size))

# game loop
game_loop = True
while game_loop:
    # check for events and change variables based on events
    for event in pygame.event.get():
        
        # check if user has quit
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        check_which_mouse_button = pygame.mouse.get_pressed()
        if event.type == MOUSEBUTTONDOWN:
            if check_which_mouse_button[0]:
                leftclick_down_location = pygame.mouse.get_pos()
                draw_new_selection_box = True
                selection_completed = False
   
                selected_units = []
        if event.type == MOUSEBUTTONUP:
            if not check_which_mouse_button[0]:
                leftclick_up_location = pygame.mouse.get_pos()
                draw_new_selection_box = False
                selection_completed = True
                # save the selection box
                completed_selection_box = selection_box

    # calculate selection box
    def calculate_current_selection_box():
        current_mouse_location = pygame.mouse.get_pos()
        selection_box_x = current_mouse_location[0] - leftclick_down_location[0]
        selection_box_y = current_mouse_location[1] - leftclick_down_location[1]
        top_left_corner = leftclick_down_location
        if selection_box_x < 0:
            selection_box_x = abs(selection_box_x)
            top_left_corner = (top_left_corner[0] - selection_box_x, top_left_corner[1])
        if selection_box_y < 0:
            selection_box_y = abs(selection_box_y)
            top_left_corner = (top_left_corner[0], top_left_corner[1] - selection_box_y)
        current_selection_box = pygame.Rect((top_left_corner), (selection_box_x, selection_box_y))
        return current_selection_box
        
    # checks a boolean and recieves the current selection box
    if draw_new_selection_box == True:
        selection_box = calculate_current_selection_box()

    #make a list of units currently in selection box, or completed_selection_box
    if selection_completed:
        counter = 0
        for unit in units:
            if completed_selection_box.colliderect(unit):
                selected_units.append(unit)
                counter += 1

    # draw the background onto surface
    windowSurface.fill(BACKGROUNDCOLOR)
    # draw selection box and units onto Windowsurface
    for unit in units:
        pygame.draw.rect(windowSurface, WHITE, unit, 2)
    if draw_new_selection_box:
        pygame.draw.rect(windowSurface, RED, selection_box, 2)
        for unit in units:
            if selection_box.colliderect(unit):
                pygame.draw.rect(windowSurface, BLUE, unit, 2)
    for selected_unit in selected_units:
        pygame.draw.rect(windowSurface, BLUE, selected_unit, 2)
    selection_completed = False

    # draw windowSurface onto the screen
    pygame.display.update()
    mainClock.tick(60)
