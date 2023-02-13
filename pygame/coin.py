from random import randint


WIDTH = 400
HEIGHT = 400
score = 0
game_over = False
Avacadobear = Actor("ab1")
Avacadobear.pos = 100, 100

coin = Actor("coin")
coin.pos = 200, 200


def draw():
    screen.fill("tan")
    Avacadobear.draw()
    coin.draw()
    screen.draw.text("Score: " + str(score), color="dark red", topleft=(10, 10))

    if game_over:
        screen.fill("light blue")
        screen.draw.text("Final Score: " + str(score), topleft=(10, 10), fontsize=60)


def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))


def time_up():
    global game_over
    game_over = True


def update():
    global score

    if keyboard.left:
        Avacadobear.x = Avacadobear.x - 2
    elif keyboard.right:
        Avacadobear.x = Avacadobear.x + 2
    elif keyboard.up:
        Avacadobear.y = Avacadobear.y - 2
    elif keyboard.down:
        Avacadobear.y = Avacadobear.y + 2

    coin_collected = Avacadobear.colliderect(coin)
    if coin_collected:
        score = score + 10
        place_coin()


clock.schedule(time_up, 10.0)
place_coin()
