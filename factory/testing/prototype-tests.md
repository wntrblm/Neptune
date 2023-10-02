# Neptune pre-production prototype testing

1. [x] Check low impedance inputs (10kΩ) for loading effects
    - [x] LP in
    - [x] HP in
    - [x] FM1
    - [x] FM2
    - **Notes**: These effects are significant, but initially acceptable.
2. [ ] Test all inputs and outputs overvoltage ±12V
3. [x] Input volume
    - [x] Test general functionality of LP input volume
    - [x] Test general functionality of HP input volume
4. [x] Cutoff functionality
    - [x] Test general functionality of cutoff knob control
    - [x] Check that cutoff CV range and the knob range are the same
5. [x] Resonance& self oscillation
    - [x] Test general functionality of resonance knob control
    - [x] Test that the CV range and the knob range are the same
    - [x] Self oscillation LED comes on too early and too gradually FIXED
    - [x] Add transistor circuit to make this led pop on when self oscillation starts
6. [x] Instability
    - [x] Test general functionality of instability knob control
    - [x] Test that the CV range and the knob range are the same
    - [x] Remove solder jumpers
7. [x] Output VCA
    - [x] Test general functionality of output VCA
    - [x] Test that the default output volume is the same as +5v into the volume input
8. [x] Vref:
    - [x] Double check stability with C205 cap, see [app note](https://www.ti.com/lit/an/slva482a/slva482a.pdf?ts=1694821507442).
    - [x] DNP'd C205 to enhance stability.
9. [x] FM1:
    - [x] Test general functionality of FM2 knob control
    - [x] Currently the knob is a bit sensitive (hard to dial in 0 modulation) and the LEDS aren't very sensitive. Add 4 resistors and moving a couple diodes around to increase deadzone of knob and led sensitivity.
10. [x] FM2:
    - [x] Test general functionality of FM2 knob control
11. [ ] Tests for Next Prototype:
    - [ ] Make sure resonance self oscillation light comes on at the right spot
    - [ ] Make sure FM1 LEDs look correct for input CV
    - [ ] Make sure resonance isn't effected by the added voltage divider
    - [ ] Make sure all LEDs look correct
    - [ ] Listen to resonance roughness
