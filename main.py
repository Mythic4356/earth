serial.redirect_to_usb()
State = False

def on_forever():
    global State
    if Environment.sonarbit_distance(Environment.Distance_Unit.DISTANCE_UNIT_CM, DigitalPin.P16) < 3:
        State = True
    else:
        State = False
    if State:
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
    else:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
    serial.write_line("" + str((State)))
basic.forever(on_forever)
