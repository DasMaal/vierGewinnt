TITLE ="Pygame Zero demo"
WIDTH = 800
HEIGHT = 600

class Ball():
    def __init__(self):
        self.actor = Actor("ball", (150,150))

        self.speedx = 2
        self.speedy = 2

    def update(self):
        ball.actor.x += self.speedx
        ball.actor.y += self.speedy

        if self.actor.left < 0 or self.actor.right > WIDTH:
            self.bounce(xdir=True, ydir=False)
        if self.actor.right < 0 or self.actor.left > WIDTH:
            self.bounce(xdir=False, ydir=True)

    def bounce(self, xdir=True, ydir=False):
        if xdir:
            self.speedx *= -1
        if ydir:
            self.speedy *= -1

def update():
    ball.update()

def draw():
    screen.fill((128,0,0))
    ball.actor.draw()

def on_mouse_down(pos):
    if ball.actor.collidepoint(pos):
        ball.bounce()

ball = Ball()