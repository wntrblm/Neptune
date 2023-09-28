# Neptune factory unit tests

1. Filter Core test
   - Goal: Make sure filter can fully cutoff both inputs, and that both inputs are functional
   
   - Input: 20 Hz ±5v peak to peak square to LP vol pin 2
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
   
5. Output VCA:
   - Goal: Make sure the output VCA is working to control output volume
   - Apply 4.3v (this value might need to get tweaked) to resonance CV input to start self oscillation
   - Apply 2.5v to cutoff pin 2 (simulate knob at center point)
   - Output should be roughly ±6v peak to peak 1khz sine wave
   - apply GND to vol input
   - output should be silent
   - Now we know that the volume VCA works.
   - Null all pins
   
6. Caveats:
   - This will not test any aspect of the potentiometers. If the pots are bad, or their connection to their references is bad, these tests will not catch that.