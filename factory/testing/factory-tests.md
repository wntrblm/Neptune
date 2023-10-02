# Neptune factory unit tests

1. Filter Core test

    - **Goal**: Make sure filter can fully cutoff both inputs, and that both inputs are functional
    - _Input_: 20 Hz ±5v peak to peak square to LP vol pin 2
    - Connect Cutoff Pin 2 to 8v (full cutoff)
    - Output should be unfiltered input, but with some saturation because of full volume
    - Apply 5v to FM1 pin 3, 5v to pin 2, GND to pin 1 (full modulation)
    - Connect Cutoff Pin 2 to -2.56v (minimum cutoff)
    - Output should be unfiltered input, but with some saturation because of full volume
    - Disconnect FM1 pins
    - connect FM2 Pin 2 to 5v
    - Output should be unfiltered input, but with some saturation because of full volume
    - disconnect FM2 pins
    - Output should be silent (whatever your threshold is)
    - At this point we know that the filter core, low pass input, and FM1, and FM2 circuit are all functional
    - Null all pins

    - Input: 20khz ±5v peak to peak sine wave into HP Vol pin 2
    - Connect HP Vol Pin 2 to Pin 3 (full volume)
    - Connect Cutoff Pin 2 to -2.56v (minimum cutoff)
    - Output should be unfiltered input, but with some saturation because of full volume
    - Apply 5v to FM1 pin 3, GND to pin 2, GND to pin 1 (full inversion)
    - Connect Cutoff Pin 2 to 8v (full cutoff)
    - Output should be unfiltered input, but with some saturation because of full volume
    - Disconnect FM1 pins
    - Output should be silent (whatever your threshold is)
    - Now we know that the filter core, both inputs, and FM1, and FM2, are all functional (we could probably get rid of the FM1 aspect of this section of the test, since it is being tested in the lp test)
    - Null all pins

2. Resonance/self oscillation test:

    - Goal: Make sure the filter starts self oscillating at the correct point, and the filter cutoff knob is properly centered around `1 kHz`
    - Apply 4.3v (this value might need to get tweaked) to resonance CV input
    - apply 2.5v to cutoff pin 2 (simulate knob at center point)
    - output should be relatively clean 1khz sine wave around ±6v peak to peak
    - Now we know that the filter self oscillates at the correct point and that the filter cutoff knob is correctly centered, and that the resonance VCA works
    - Null all pins

3. Salt:

    - Goal: Make sure the salt circuit is functioning
    - Apply 4.3v (this value might need to get tweaked) to resonance CV input to start self oscillation
    - Apply 2.58v to cutoff pin 2 (simulate knob at center point)
    - Apply 5v to salt CV input
    - Output should be chaotic oscillation
    - Now we know that the instability circuit is connected and the VCA for it is functioning
    - Null all pins

4. Output VCA:

    - Goal: Make sure the output VCA is working to control output volume
    - Apply 4.3v (this value might need to get tweaked) to resonance CV input to start self oscillation
    - Apply 2.5v to cutoff pin 2 (simulate knob at center point)
    - Output should be roughly ±6v peak to peak 1khz sine wave
    - apply GND to vol input
    - output should be silent
    - Now we know that the volume VCA works.
    - Null all pins

5. Caveats:
    - This will not test any aspect of the potentiometers. If the pots are bad, or their connection to their references is bad, these tests will not catch that.

## Hubble connection table

| test point             | requirements                   | connection                                         |
| ---------------------- | ------------------------------ | -------------------------------------------------- |
| LP Vol pot             | Fully CW, Fully CCW            | 2:1 MUX between pins                               |
| HP Vol pot             | Fully CW, Fully CCW            | 2:1 MUX between pins                               |
| Cutoff pot             | Fully CW, Center, Fully CCW    | 3:1 MUX between pins, with 5k resistors for center |
| FM1 pot                | Fully CW, Center, Fully CCW    | 3:1 MUX between pins, with 5k resistors for center |
| FM2 pot                | Fully CW, Fully CCW            | 2:1 MUX between pins                               |
| Reso pot               | Fully CW, Fully CCW            | 2:1 MUX between pins                               |
| Salt pot               | Fully CW, Fully CCW            | 2:1 MUX between pins                               |
| LP jack                | Mute, 1kHz, 20kHz, sine/square | 3:1 MUX: GND, Ext FG ch1, FS DAC Ch1               |
| HP jack                | same as LP                     | 3:1 MUX: GND, Ext FG ch2, FS DAC Ch1               |
| FM1 jack               | 0-5V                           | FS DAC Ch2                                         |
| FM2 jack               | 0-5V                           | FS DAC Ch3                                         |
| Reso jack              | 0-5V                           | FS DAC Ch4                                         |
| Salt jack              | 0-5V                           | FS DAC Ch5                                         |
| Vol jack               | 0-5V                           | FS DAC Ch6                                         |
| Out jack               | Audio out                      | FS ADC Ch1, Ext Osc Ch1                            |
| TP201: 2.5V            | Voltage reference, unbuffered  | FS ADC Ch2, Ext MM Ch1                             |
| TP202: +8V             | Voltage reference, buffered    | FS ADC Ch3, Ext MM Ch2                             |
| TP203: -8V             | Voltage reference, buffered    | FS ADC Ch4, Ext MM Ch3                             |
| TP401: Cutoff CV mix   | DC voltage, mV                 | FS ADC Ch5                                         |
| TP501: Filter core CV  | DC voltage, mV                 | Unused                                             |
| TP502: Low pass in     | AC voltage, mV                 | Unused                                             |
| TP503: Resonance core  | AC voltage, mV                 | Unused                                             |
| TP504: High pass in    | AC voltage, mV                 | Unused                                             |
| TP505: Ladder top      | AC voltage, mV                 | Unused                                             |
| TP506: Ladder bottom   | AC voltage, mV                 | Unused                                             |
| TP507: Filter core     | AC voltage, mV                 | Unused                                             |
| TP508: Filter core out | AC voltage, V                  | Unused                                             |
| TP701: Salt rectifier  | AC voltage, mV                 | Unused                                             |
| TP702: Instability out | AC voltage, mV                 | Unused                                             |
