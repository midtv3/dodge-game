function meteor () {
    mySprite22 = sprites.create(list2[randint(0, 6)], SpriteKind.Projectile)
    mySprite22.setVelocity(0, 50)
    mySprite22.setPosition(randint(10, 120), 10)
    mySprite22.setFlag(SpriteFlag.AutoDestroy, true)
}
sprites.onDestroyed(SpriteKind.Player, function (mySprite) {
    info.setLife(0)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Projectile, function (sprite, otherSprite) {
    if (isInvincible == 0) {
        info.changeLifeBy(-1)
        scene.cameraShake(8, 500)
        isInvincible = 1
        pause(2000)
        isInvincible = 0
    }
})
info.onLifeZero(function () {
    current_score = info.score()
    controller.moveSprite(mySprite2, 0, 0)
    mySprite2.sayText("X_X")
    mySprite2.startEffect(effects.disintegrate, 1000)
    pause(1000)
    if (highScore == null || highScore != highScore) {
        highScore = 0
    }
    if (current_score >= highScore) {
        highScore = current_score
        settings.writeNumber("hScore", highScore)
    }
    game.splash("Score is: " + ("" + current_score))
    game.splash("High Score is: " + ("" + highScore))
    game.reset()
})
let current_score = 0
let mySprite2: Sprite = null
let diffuculty = 0
let list2: Image[] = []
let isInvincible = 0
let highScore = 0
let mySprite22 : Sprite = null
isInvincible = 0
mySprite22 = null
list2 = []
// Check if historical score exists safely
if (settings.exists("hScore")) {
    highScore = settings.readNumber("hScore")
if (highScore == null || highScore != highScore) {
        highScore = 0
    }
} else {
    highScore = 0
}
game.splash("Welcome to Dodge Game.")
let userDifficulty = game.askForNumber("Difficulty? 1-Easy, 2-Med, 3-Hard.", 1, true)
if (userDifficulty == 1) {
    diffuculty = 4000
    info.setLife(10)
} else if (userDifficulty == 2) {
    diffuculty = 2000
    info.setLife(8)
} else if (userDifficulty == 3) {
    diffuculty = 1000
    info.setLife(6)
} else if (userDifficulty == 4) {
    diffuculty = 500
    info.setLife(4)
} else if (userDifficulty == 5) {
    diffuculty = 250
    info.setLife(1)
} else {
    diffuculty = 500
    info.setLife(4)
}
list2 = [
assets.image`myImage`,
assets.image`myImage0`,
assets.image`myImage1`,
assets.image`myImage2`,
assets.image`myImage3`,
assets.image`myImage4`,
assets.image`myImage5`
]
scene.setBackgroundImage(assets.image`bg-main`)
mySprite2 = sprites.create(assets.image`female character`, SpriteKind.Player)
mySprite2.setPosition(13, 104)
mySprite2.setFlag(SpriteFlag.AutoDestroy, true)
controller.moveSprite(mySprite2, 100, 0)
info.setScore(0)
let nextLifeScore = 10000
forever(function () {
    if (info.life() <= 0) {
        return
    }
    if (userDifficulty == 1) {
        info.changeScoreBy(1)
    } else if (userDifficulty == 2) {
        info.changeScoreBy(2)
    } else if (userDifficulty == 3) {
        info.changeScoreBy(3)
    } else if (userDifficulty == 4) {
        info.changeScoreBy(4)
    } else if (userDifficulty == 5) {
        info.changeScoreBy(5)
    } else {
        info.changeScoreBy(4)
    }
    if (info.score() >= nextLifeScore) {
        info.changeLifeBy(1)
        nextLifeScore += 10000
        effects.confetti.startScreenEffect(2000)
    }
})
forever(function () {
    if (info.life() <= 0) {
        return
    }
    meteor()
    pause(diffuculty)
})
