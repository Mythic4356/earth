serial.redirectToUSB()
let State = false
basic.forever(function on_forever() {
    
    if (Environment.sonarbit_distance(Environment.Distance_Unit.Distance_Unit_cm, DigitalPin.P16) < 3) {
        State = true
    } else {
        State = false
    }
    
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
    
    serial.writeLine("" + ("" + State))
})
