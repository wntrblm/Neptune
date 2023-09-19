# Neptune pre-production prototype testing

1. [ ] Check low impedance inputs (10kΩ) for loading effects
    - [ ] LP in
    - [ ] HP in
    - [ ] FM1
    - [ ] FM2
2. [ ] Test all inputs and outputs overvoltage ±12V
3. [x] Input volume
    - [x] Test general functionality of LP input volume
    - [x] Test general functionality of HP input volume
4. [ ] Cutoff functionality
    - [x] Test general functionality of cutoff knob control
    - [ ] Check that cutoff CV range and the knob range are the same
5. [ ] Resonance& self oscillation
     - [x] Test general functionality of resonance knob control
     - [ ] Test that the CV range and the knob range are the same
     - [ ] Does the first half of the resonance knob travel seem not particularly effective?
     - [ ] Self oscillation LED comes on too early and too gradually
     - [x] Add transistor circuit to make this led pop on when self oscillation starts
     - [x] The pitch of the self oscillating wave is quite rough. Potential causes:
         - low tolerance 1nf caps used in prototype
         - Resonance VCA output is low voltage, making op amp drift potentially a factor. Changing two resistors and adding  two resistors to the resonance VCA output to increase the voltage of the op amp output. This has been changed in the schematic.
6. [ ] Instability
     - [x] Test general functionality of instability knob control
     - [ ] Test that the CV range and the knob range are the same
     - [ ] Remove solder jumpers
7. Output VCA
     - [x] Test general functionality of output VCA
     - [ ] Test that the default output volume is the same as +5v into the volume input
8. Vref:
     - [ ] Double check stability with C205 cap, see [app note](https://www.ti.com/lit/an/slva482a/slva482a.pdf?ts=1694821507442).
9. [x] FM1:
     - [x] Test general functionality of FM2 knob control
     - [x] Currently the knob is a bit sensitive (hard to dial in 0 modulation) and the LEDS aren't very sensitive. Add 4 resistors and moving a couple diodes around to increase deadzone of knob and led sensitivity.
10. [x] FM2:
      - [x] Test general functionality of FM2 knob control
