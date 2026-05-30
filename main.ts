basic.showString("TE AMO", 150)
basic.pause(800)
basic.showString("MUCHO", 150)
basic.pause(1200)
// Corazón animado
basic.showIcon(IconNames.Heart)
basic.pause(600)
basic.showIcon(IconNames.SmallHeart)
basic.pause(400)
basic.showIcon(IconNames.Heart)
basic.pause(600)
basic.showIcon(IconNames.SmallHeart)
basic.pause(400)
// Repetir el mensaje
basic.forever(function () {
    basic.showString("TE AMO MUCHO <3", 100)
basic.pause(2000)
})
