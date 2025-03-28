def on_a_pressed():
    if jogador.is_hitting_tile(CollisionDirection.BOTTOM):
        jogador.y += -10
        pause(15)
        jogador.y += -10
        pause(15)
        jogador.y += -10
        pause(15)
        jogador.y += -10
        pause(15)
        jogador.y += -10
        pause(15)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    sprites.destroy(sprite)
    info.change_life_by(-1)
    info.change_score_by(-1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.player, on_on_overlap)

def on_left_pressed():
    jogador.x += -10
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_pressed():
    jogador.x += 10
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_on_destroyed(sprite2):
    info.change_score_by(1)
sprites.on_destroyed(SpriteKind.player, on_on_destroyed)

morcego: Sprite = None
jogador: Sprite = None
tiles.set_current_tilemap(tilemap("""
    level1
    """))
jogador = sprites.create(img("""
        . . . . . . . c c . . . . . . .
        . . . . . . . c 5 c . . . . . .
        . . . . c c c 5 5 5 c c . . . .
        . . c c b c 5 5 5 5 c c c c . .
        . c b b 5 b 5 5 5 5 b 5 b b c .
        . c b 5 5 b b 5 5 b b 5 5 b c .
        . . f 5 5 5 b b b b 5 5 5 c . .
        . . f f 5 5 5 5 5 5 5 5 f . . .
        . . f f e e b f e e e f . . . .
        . . f f f b 1 f b b e f . . . .
        . . . f f b b b b b b f . . . .
        . . . e e f e e e e f . . . . .
        . . . e b b e b b 5 f . . . . .
        . . . e b b e 5 5 5 5 f . . . .
        . . . . e e 5 5 5 5 b c . . . .
        . . . . . f f f f f f . . . . .
        """),
    SpriteKind.player)
jogador.set_scale(2, ScaleAnchor.MIDDLE)
jogador.set_position(20, 80)
info.set_life(4)

def on_forever():
    if jogador.is_hitting_tile(CollisionDirection.BOTTOM):
        jogador.vy = 0
    else:
        jogador.ay = 400
    scene.center_camera_at(jogador.x, 50)
forever(on_forever)

def on_forever2():
    global morcego
    pause(randint(2000, 3000))
    morcego = sprites.create_projectile_from_side(img("""
            . f f f . . . . . . . . f f f .
            f f c . . . . . . . f c b b c .
            f c c . . . . . . f c b b c . .
            c f . . . . . . . f b c c c . .
            c f f . . . . . f f b b c c . .
            f f f c c . c c f b c b b c . .
            f f f c c c c c f b c c b c . .
            . f c 3 c c 3 b c b c c c . . .
            . c b 3 b c 3 b b c c c c . . .
            c c b b b b b b b b c c . . . .
            c b 1 b b b 1 b b b b f c . . .
            f b b b b b b b b b b f c c . .
            f b c b b b c b b b b f . . . .
            . f 1 f f f 1 b b b c f . . . .
            . . f b b b b b b c f . . . . .
            . . . f f f f f f f . . . . . .
            """),
        -50,
        0)
    morcego.set_flag(SpriteFlag.AUTO_DESTROY, True)
    morcego.set_position(160, randint(50, 80))
forever(on_forever2)
