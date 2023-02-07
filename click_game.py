Avacadobear = Actor("ab1")
Avacadobear.pos = 100, 50

WIDTH = 500
HEIGHT = Avacadobear.height + 20

def draw():
    screen.clear()
    screen.fill((255, 255, 255))
    Avacadobear.draw()

def update():
    Avacadobear.left = Avacadobear.left + 2
    if Avacadobear.left > WIDTH:
        Avacadobear.right = 0
