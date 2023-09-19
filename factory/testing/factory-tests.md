# Neptune factory unit tests

1. LP test
   - Goal: Make sure low pass filter can fully cutoff input audio, as well leave it unaffected on the other side
   - Input: `20 Hz` square
   - Knob/CV fully CW should leave input unaffected
   - Knob/CV fully CCW should output less than `500 mV` (might want to change this threshold, whatever silence means to you)
2. HP test:
   - Goal: Make sure high pass filter can fully cutoff input audio, as well leave it unaffected on the other side
   - Input `20 kHz` sine (we could also change this to a slower square wave and use the fast rising edges as the high frequency information)
   - Knob/CV fully CCW should leave input unaffected
   - Knob/CV fully CW should output less than `500 mV` (might want to change this threshold, whatever silence means to you)
3. Resonance/self oscillation:
   - Goal: Make sure the filter starts self oscillating at the correct point, and the filter cutoff knob is properly centered around `1 kHz`
   - Self Oscillation should start at `~4.3 V` at the resonance CV input.
   - Knob at 12 o'clock self oscillation `1khz ± ? Hz`.
   - Knob fully CCW self oscillation `4 Hz ± ? Hz`.
4. Instability:
   - Goal: Make sure the instability circuit is functioning (what does functional instability mean really?)
5. FM1:
   - Goal: Make sure FM1 attenuverter is working to control cutoff frequency
6. Output VCA:
   - Goal: Make sure the output VCA is working to control output volume


