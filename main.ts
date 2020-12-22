let LVL1 = 0
let LVL3 = 0
input.onButtonPressed(Button.A, function () {
    if (LVL1 && LVL3) {
        basic.showLeds(`
            # . . . #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
    }
})
basic.forever(function () {
    LVL1 = pins.analogReadPin(AnalogPin.P0)
    LVL3 = pins.analogReadPin(AnalogPin.P0)
})
