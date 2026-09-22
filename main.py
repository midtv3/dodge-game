def meteor():
    global mySprite22
    mySprite22 = sprites.create(list2[randint(0, 6)], SpriteKind.projectile)
    mySprite22.set_velocity(0, 50)
    mySprite22.set_position(randint(10, 120), 10)
    mySprite22.set_flag(SpriteFlag.AUTO_DESTROY, True)

def on_on_destroyed(mySprite):
    info.set_life(0)
sprites.on_destroyed(SpriteKind.player, on_on_destroyed)

def on_on_overlap(sprite, otherSprite):
    global isInvincible
    if isInvincible == 0:
        info.change_life_by(-1)
        scene.camera_shake(8, 500)
        isInvincible = 1
        pause(2000)
        isInvincible = 0
sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, on_on_overlap)

def on_life_zero():
    global current_score, highScore
    current_score = info.score()
    controller.move_sprite(mySprite2, 0, 0)
    mySprite2.say_text("X_X")
    mySprite2.start_effect(effects.disintegrate, 1000)
    pause(1000)
    if highScore == None or highScore != highScore:
        highScore = 0
    if current_score >= highScore:
        highScore = current_score
        settings.write_number("hScore", highScore)
    game.splash("Score is: " + ("" + str(current_score)))
    game.splash("High Score is: " + ("" + str(highScore)))
    game.reset()
info.on_life_zero(on_life_zero)

current_score = 0
mySprite2: Sprite = None
diffuculty = 0
list2: List[Image] = []
isInvincible = 0
highScore = 0
mySprite22: Sprite = None
isInvincible = 0
mySprite22 = None
list2 = []
# Check if historical score exists safely
if settings.exists("hScore"):
    highScore = settings.read_number("hScore")
    if highScore == None or highScore != highScore:
        highScore = 0
else:
    highScore = 0
game.splash("Welcome to Dodge Game.")
userDifficulty = game.ask_for_number("Difficulty? 1-Easy, 2-Med, 3-Hard.", 1, True)
if userDifficulty == 1:
    diffuculty = 4000
    info.set_life(10)
elif userDifficulty == 2:
    diffuculty = 2000
    info.set_life(8)
elif userDifficulty == 3:
    diffuculty = 1000
    info.set_life(6)
elif userDifficulty == 4:
    diffuculty = 500
    info.set_life(4)
elif userDifficulty == 5:
    diffuculty = 250
    info.set_life(1)
else:
    diffuculty = 500
    info.set_life(4)
list2 = [assets.image("""
        myImage
        """),
    assets.image("""
        myImage0
        """),
    assets.image("""
        myImage1
        """),
    assets.image("""
        myImage2
        """),
    assets.image("""
        myImage3
        """),
    assets.image("""
        myImage4
        """),
    assets.image("""
        myImage5
        """)]
scene.set_background_image(assets.image("""
    bg-main
    """))
mySprite2 = sprites.create(assets.image("""
        female character
        """),
    SpriteKind.player)
mySprite2.set_position(13, 104)
mySprite2.set_flag(SpriteFlag.AUTO_DESTROY, True)
controller.move_sprite(mySprite2, 100, 0)
info.set_score(0)
nextLifeScore = 10000

def on_forever():
    global nextLifeScore
    if info.life() <= 0:
        return
    if userDifficulty == 1:
        info.change_score_by(1)
    elif userDifficulty == 2:
        info.change_score_by(2)
    elif userDifficulty == 3:
        info.change_score_by(3)
    elif userDifficulty == 4:
        info.change_score_by(4)
    elif userDifficulty == 5:
        info.change_score_by(5)
    else:
        info.change_score_by(4)
    if info.score() >= nextLifeScore:
        info.change_life_by(1)
        nextLifeScore += 10000
        effects.confetti.start_screen_effect(2000)
forever(on_forever)

def on_forever2():
    if info.life() <= 0:
        return
    meteor()
    pause(diffuculty)
forever(on_forever2)
