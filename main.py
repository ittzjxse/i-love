basic.show_string("TE AMO", 150)
basic.pause(800)
basic.show_string("MUCHO", 150)
basic.pause(1200)
# Corazón animado
basic.show_icon(IconNames.HEART)
basic.pause(600)
basic.show_icon(IconNames.SMALL_HEART)
basic.pause(400)
basic.show_icon(IconNames.HEART)
basic.pause(600)
basic.show_icon(IconNames.SMALL_HEART)
basic.pause(400)
# Repetir el mensaje

def on_forever():
    basic.show_string("TE AMO MUCHO <3", 100)
    basic.pause(2000)
basic.forever(on_forever)
