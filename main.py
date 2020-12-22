def on_pin_pressed_p0():
    basic.show_leds("""
        # . . . #
        # . . . #
        # . . . #
        # # # # #
        # # # # #
        """)
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_pin_pressed_p2():
    basic.show_leds("""
        # . . . #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        """)
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_pin_pressed_p1():
    basic.show_leds("""
        # . . . #
        # . . . #
        # # # # #
        # # # # #
        # # # # #
        """)
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

basic.show_string("Level")
Radio = 0.5
Altura = 0.5
Volumen = 3.14 * (Altura * (Radio * Radio))
Litros = Volumen * 1000
basic.show_number(Litros)

def on_forever():
    pass
basic.forever(on_forever)
