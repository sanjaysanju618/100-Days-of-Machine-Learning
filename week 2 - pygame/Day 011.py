import pygame
import time
import random

pygame.init()

display_width = 600
display_height = 700

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 200, 0)
red = (200, 0, 0)

bright_green = (0, 255, 0)
bright_red = (255, 0, 0)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Racer")
clock = pygame.time.Clock()

carImg = pygame.image.load("car.png")
car_width = 78


def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged : " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def crashed():
    message_display("You Crashed")
    time.sleep(2)
    game_loop()


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def button(btn_x, btn_y, text, active_color, inactive_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if (btn_x + 100) > mouse[0] > btn_x and btn_y + 50 > mouse[1] > btn_y:
        pygame.draw.rect(gameDisplay, active_color, (btn_x, btn_y, 100, 50))
        if click[0] == 1:
            action()
    else:
        pygame.draw.rect(gameDisplay, inactive_color, (btn_x, btn_y, 100, 50))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(text, smallText)
    textRect.center = ((btn_x + (100 / 2)), (btn_y + (50 / 2)))
    gameDisplay.blit(textSurf, textRect)


def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf", 80)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()


def quit_game():
    pygame.quit()
    quit()


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
        gameDisplay.fill(white)
        message_display("Carzy Car!...")
        button(
            btn_x=display_width * 0.2,
            btn_y=display_height * 0.8,
            text="Play",
            active_color=bright_green,
            inactive_color=green,
            action=game_loop,
        )
        button(
            btn_x=display_width * 0.65,
            btn_y=display_height * 0.8,
            text="Exit",
            active_color=bright_red,
            inactive_color=red,
            action=quit_game,
        )
        pygame.display.update()
        clock.tick(15)


def game_loop():
    x = display_width * 0.45
    y = display_height * 0.7

    x_change = 0
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100
    gameExit = False

    dodged = 0

    while not gameExit:
        for event in pygame.event.get():
            # Game logic
            if event.type == pygame.QUIT:
                quit_game()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        x += x_change
        gameDisplay.fill(white)

        things(
            thingx=thing_startx,
            thingy=thing_starty,
            thingw=thing_width,
            thingh=thing_height,
            color=black,
        )
        thing_starty += thing_speed
        car(x, y)
        things_dodged(dodged)

        # out of boundary....
        if x > display_width - car_width or x < 0:
            crashed()

        # place the things at random place....
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed += 0.5
            thing_width += dodged * 1.2

        # crash logic....
        if y < thing_starty + thing_height:
            if (
                x > thing_startx
                and x < thing_startx + thing_width
                or x + car_width > thing_startx
                and x + car_width < thing_startx + thing_width
            ):
                crashed()

        pygame.display.update()
        clock.tick(60)


game_intro()
game_loop()
quit_game()
