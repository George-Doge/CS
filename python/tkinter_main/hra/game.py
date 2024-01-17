import pygame

pygame.init()

SCREEN_WIDTH = 1080
SCREEN_HEIGHT =  int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# set framerate
clock = pygame.time.Clock()
FPS = 60

#IMAGES
grid_img = pygame.image.load('grid.png').convert_alpha()
grid_img = pygame.transform.scale(grid_img, (700, 700))

circle_img = pygame.image.load('circle.png').convert_alpha()
circle_img = pygame.transform.scale(circle_img, (300, 300))

cross_img = pygame.image.load('cross.png').convert_alpha()
cross_img = pygame.transform.scale(cross_img, (170, 170))

#VARIABLES AND COLOURS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
player = 1
font = pygame.font.SysFont('Futura', 80)

#functions

def draw_bg():
    screen.fill(WHITE)


def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	screen.blit(img, (x, y))


class Grid():
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = grid_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    

    def update(self):
        screen.blit(self.image, self.rect)


class Circle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = circle_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


    def update(self):
        screen.blit(self.image, self.rect)


class Cross(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = cross_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


    def update(self):
        screen.blit(self.image, self.rect)


#groups
circle_group = pygame.sprite.Group()
cross_group = pygame.sprite.Group()


run = True

grid = Grid(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)

while run:
    
    clock.tick(FPS)
    draw_bg()

    #get mouse pos
    mouse_pos = pygame.mouse.get_pos()
    x_pos = mouse_pos[0]
    y_pos = mouse_pos[1]

    grid.update()

    #update groups
    circle_group.update()
    circle_group.draw(screen)
    cross_group.update()
    cross_group.draw(screen)

    draw_text(f"Player {player} turn", font, BLACK, SCREEN_WIDTH//2 - 180, 20)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

            if event.key == pygame.K_c: #reset game
                player = 1
                circle_group.empty()
                cross_group.empty()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if player == 1:
                    circle = Circle(x_pos, y_pos)
                    circle_group.add(circle)
                    player += 1

                elif player == 2:
                    cross = Cross(x_pos, y_pos)
                    cross_group.add(cross)
                    player -= 1

    pygame.display.update()

pygame.quit()
