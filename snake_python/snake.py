# To use mySnake.py instead of the solution code, replace "mySnake_sol" by "mySnake" in the following line.
from mySnake_sol import *
from sys import exit
import pygame

class Apple:
    x = 0
    y = 0
    step = 40

    def __init__(self,x,y):
        self.x = x * self.step
        self.y = y * self.step

    def draw(self, surface, image):
        surface.blit(image,(self.x, self.y))


class Player:
    x = [0]
    y = [0]
    step = 40
    direction = 0
    length = 3

    updateCountMax = 2
    updateCount = 0

    def __init__(self, length, x, y):
       self.length = length
       self.x = [x]
       self.y = [y]
       self.direction = 0
       for i in range(0,2000):
           self.x.append(-100)
           self.y.append(-100)

       # initial positions, no collision.
       self.x[1] = 1*self.step
       self.x[2] = 2*self.step

    def update(self):

        self.updateCount = self.updateCount + 1
        if self.updateCount > self.updateCountMax:

            # update previous positions
            for i in range(self.length-1,0,-1):
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]

            # update position of head of snake
            if self.direction == 0:
                self.x[0] = self.x[0] + self.step
            if self.direction == 1:
                self.x[0] = self.x[0] - self.step
            if self.direction == 2:
                self.y[0] = self.y[0] - self.step
            if self.direction == 3:
                self.y[0] = self.y[0] + self.step

            self.updateCount = 0


    def moveRight(self):
        self.direction = 0

    def moveLeft(self):
        self.direction = 1

    def moveUp(self):
        self.direction = 2

    def moveDown(self):
        self.direction = 3

    def draw(self, surface, image):
        for i in range(0,self.length):
            surface.blit(image,(self.x[i],self.y[i]))

    def myCollision(self, apple):
        if isCollision(apple.x,apple.y,self.x[0], self.y[0]):
            self.length = self.length + 1
            x = randint(0,19) * self.step
            y = randint(0,14) * self.step
            while(not valid_pos(self, x, y)):
                x = randint(0,19) * self.step
                y = randint(0,14) * self.step


            apple.x = x
            apple.y = y

    def selfCollision(self):
        for i in range(2,self.length):
            if isCollision(self.x[0],self.y[0],self.x[i], self.y[i]):
                return True
        return False

    def myWallCollision(self, width, height):
        if (wallCollision(self.x[0], self.y[0], width, height)):
            return True

        return False

class App:

    windowWidth = 800
    windowHeight = 600
    player = 0
    other_player = 0
    apple = 0
    window = 0
    button = 0
    level = 1
    speed = 1

    def __init__(self):
        self.gameOverPlayer = False
        self.gameOverOtherPlayer = False
        self.player = Player(3, 0, 0)
        self.other_player = Player(3, 1, 1)
        self.apple = Apple(5,5)
        self.window = None
        self.button = None
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)

        pygame.display.set_caption('Snake game')
        self._running = True
        self._image_surf = pygame.image.load("block.png").convert()
        self._apple_surf = pygame.image.load("pygame.png").convert()

    def setWindow(self, window):
        self.window = window

    def setButton(self, button):
        self.button = button

    def on_loop(self):
        self.player.update()
        self.other_player.update()

        # does snake eat apple?
        self.other_player.myCollision(self.apple)
        self.player.myCollision(self.apple)

        # does snake collide with itself?
        self.gameOverPlayer = self.other_player.selfCollision()
        self.gameOverOtherPlayer = self.other_player.selfCollision()

        # does snake collide with wall?
        self.gameOverPlayer = self.player.myWallCollision(self.windowWidth, self.windowHeight)
        self.gameOverOtherPlayer = self.other_player.myWallCollision(self.windowWidth, self.windowHeight)

        pass

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)

        pygame.display.set_caption('Pygame pythonspot.com example')
        self._running = True
        self._image_surf = pygame.image.load("block.png").convert()
        self._apple_surf = pygame.image.load("pygame.png").convert()

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_render(self):
        self._display_surf.fill((0,0,0))
        self.player.draw(self._display_surf, self._image_surf)
        self.other_player.draw(self._display_surf, self._image_surf)
        self.apple.draw(self._display_surf, self._apple_surf)

        if self.gameOverPlayer:
            self.window.setText("Joueur 1 à gagné !")
            self.window.draw()
            self.button.draw()
        elif self.gameOverOtherPlayer:
            self.window.setText("Joueur 2 à gagné !")
            self.window.draw()
            self.button.draw()

        pygame.display.flip()


    def on_cleanup(self):
        pygame.quit()
        exit

    def on_execute(self):

        while( self._running ):
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            movePlayer(self.player, keys)
            moveOtherPlayer(self.other_player, keys)

            if (keys[K_ESCAPE]):
                self._running = False

            if (keys[K_RETURN]):
                restart(self)

            for event in pygame.event.get():
                if (event.type == QUIT):
                    self._running = False
                elif (event.type == MOUSEBUTTONDOWN and self.gameOver):
                    self.button.getEvent(event)


            if(not self.gameOver):
                self.on_loop()

            self.on_render()
            self.speed = snakeSpeed(self.player.length)
            time.sleep (100.0 / (1000.0*self.level*self.speed));
        self.on_cleanup()

class Window():
    text = "You Lose !"
    def __init__(self, screen):
        self.screen = screen
        self.rect = Rect((200,150),(400,300))
        self.color = pygame.Color('White')

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        myfont = pygame.font.SysFont("monospace", 60, True)
        label = myfont.render(text, 1, pygame.Color('Red'))
        self.screen.blit(label, (230,230))

    def setText(text):
        self.text = text

class Button():
    def __init__(self, parent, restart, app):
        self.parent = parent
        self.rect = Rect((325,350), (150,50))
        self.color = pygame.Color('Black')
        self.screen = parent.screen
        self._visible = False
        self.restart = restart
        self.app = app

    def getEvent(self, event):
        if self.rect.collidepoint(event.pos):
            restart(self.app)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        myfont = pygame.font.SysFont("monospace", 20)
        label = myfont.render("restart", 1, pygame.Color('White'))
        self.screen.blit(label, (355,365))



def restart(app):
    app.player = None
    app.player = Player(3, 1, 1)
    app.apple = None
    app.apple = Apple(5,5)
    app.gameOver = False
