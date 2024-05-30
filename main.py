
def on_button_pressed_a():
    global State
    State = not (State)
input.on_button_pressed(Button.A, on_button_pressed_a)

State = False
State = False

def on_forever():
    if State:
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        f = open("data.json", "w")
        f.write("{'state':1}")
        f.close()
    else:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
        f = open("data.json", "w")
        f.write("{'state':0}")
        f.close()
basic.forever(on_forever)
