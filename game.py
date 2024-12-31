import pygame
import math

def rotation(x, y, xcentre, ycentre, angle):
    norme = math.sqrt((x-xcentre)**2 + (y-ycentre)**2)
    cosalpha = (x-xcentre)/( norme )
    alpha = math.acos(cosalpha)
    if ycentre > y: alpha = -alpha
    print(norme)
    return (xcentre + norme * math.cos(alpha+angle), ycentre + norme* math.sin(alpha+angle))
class Player:
    def __init__(self, X, Y):
        self.x = X
        self.y = Y
        self.speed = 3.3
        self.mode = 1
        self.teta = 0
        self.ray_ind = 0

class Cible:
    x = 0
    y = 0
    list_rayons = []
    n = 0
    def __init__(self, X, Y, nb_cercles, l_r):
        self.x = X
        self.y = Y
        self.n = nb_cercles
        self.list_rayons = []
        for i in l_r:
            self.list_rayons.append(i)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 800))
        self.player = Player(50, 50)
        self.clock = pygame.time.Clock()
        self.running = True 
        self.cible = Cible(300, 400, 100, [i for i in range(100, 200)])
        self.joueur = Player(0, 0)

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)

    def quitGame(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False

    def handle_events(self):
        self.quitGame()
        self.movements()

    def moveRight(self):
        self.player.x += self.player.speed

    def moveLeft(self):
        self.player.x -= self.player.speed

    def moveUp(self):
        self.player.y -= self.player.speed

    def moveDown(self):
        self.player.y += self.player.speed

    def moveUpRight(self):
        self.player.y -= (self.player.speed / (2 ** 0.5))
        self.player.x += (self.player.speed / (2 ** 0.5))

    def moveUpLeft(self):
        self.player.y -= (self.player.speed / (2 ** 0.5))
        self.player.x -= (self.player.speed / (2 ** 0.5))

    def moveDownRight(self):
        self.player.y += (self.player.speed / (2 ** 0.5))
        self.player.x += (self.player.speed / (2 ** 0.5))

    def moveDownLeft(self):
        self.player.y += (self.player.speed / (2 ** 0.5))
        self.player.x -= (self.player.speed / (2 ** 0.5))

    def updateMode1(self):
        self.player.x = self.cible.x + self.cible.list_rayons[self.joueur.ray_ind] * math.cos(self.joueur.teta)
        self.player.y = self.cible.y + self.cible.list_rayons[self.joueur.ray_ind] * math.sin(self.joueur.teta)

    def moveLeftMode1(self):
        self.joueur.teta += 0.07

    def moveRightMode1(self):
        self.joueur.teta -= 0.07

    def moveUpMode1(self):
        if (self.cible.n-1) > self.joueur.ray_ind:
            self.joueur.ray_ind += 1

    def moveDownMode1(self):
        if self.joueur.ray_ind > 0:
            self.joueur.ray_ind -= 1

    def movements(self):
        key = pygame.key.get_pressed()
        if self.joueur.mode == 0:
            if key[pygame.K_UP] and key[pygame.K_RIGHT]:
                self.moveUpRight()
            elif key[pygame.K_UP] and key[pygame.K_LEFT]:
                self.moveUpLeft()
            elif key[pygame.K_DOWN] and key[pygame.K_RIGHT]:
                self.moveDownRight()
            elif key[pygame.K_DOWN] and key[pygame.K_LEFT]:
                self.moveDownLeft()
            elif key[pygame.K_RIGHT]:
                self.moveRight()
            elif key[pygame.K_LEFT]:
                self.moveLeft()
            elif key[pygame.K_UP]:
                self.moveUp()
            elif key[pygame.K_DOWN]:
                self.moveDown()
        elif self.player.mode == 1:
            if key[pygame.K_RIGHT]:
                self.moveLeftMode1()
            elif key[pygame.K_LEFT]:
                self.moveRightMode1()
            if key[pygame.K_UP]:
                self.moveUpMode1()
            elif key[pygame.K_DOWN]:
                self.moveDownMode1()
            self.updateMode1()
            print(self.joueur.ray_ind)

    def update(self):
        self.handle_events()

    def draw(self):
        self.screen.fill(Colors.BLACK)
        for i in range(self.cible.n):
            pygame.draw.circle(self.screen, Colors.PURPLE, (self.cible.x, self.cible.y), self.cible.list_rayons[i], 1)
        if self.player.mode == 0:
            pygame.draw.rect(self.screen, Colors.RED, pygame.Rect(self.player.x, self.player.y, 16, 16))
        else:
            pygame.draw.rect(self.screen, Colors.WHITE, pygame.Rect(self.player.x, self.player.y, 16, 16))
        pygame.display.flip()

class Colors:
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    PURPLE = (200, 0, 100)

if __name__ == "__main__":
    game = Game()
    game.run()
