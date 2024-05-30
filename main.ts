input.onButtonPressed(Button.A, function () {
    State = !(State)
    serial.writeLine("" + (State))
})
let State = false
serial.redirectToUSB()
State = false
basic.forever(function () {
    if (State) {
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
    } else {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
    }
})
