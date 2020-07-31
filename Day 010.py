import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

gameDisplay = pygame.display.set_mode((800, 600))
gameDisplay.fill(black)

pixAr = pygame.PixelArray(gameDisplay)

pixAr[10][20] = green


pygame.draw.line(gameDisplay, blue, (100, 200), (300, 450), 5)  # start, end

pygame.draw.rect(gameDisplay, red, (400, 400, 50, 25))  # width, height

pygame.draw.circle(gameDisplay, red, (150, 150), 70)  # center , radius

pygame.draw.polygon(
    gameDisplay, green, ((25, 75), (76, 125), (250, 100), (500, 500))
)  # tuple of point

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        print(event)
    pygame.display.update()
