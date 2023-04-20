# Clock Configuration Algorithm


To be honest, I had no prior experience with MCUs and Algorithm design. I studied the subject for a few hours to gain an
overview of how a MCU works. The solution is my own and I have implemented it from scratch.

This algorithm uses permutations to find all possible combinations of timing entities and returns a list of active inputs
on MUXs.

## Analysis
Based upon my understanding, I think that the best approach
is to create three classes
* Peripheral,which would store required peripheral clock
* ClockConfiguration which would store information on prescalers and multiplexers
* ClockConfigAlgorithm
which would contain logic for finding the best configuration.

## Technical details

### main.py
* Contains logic for working with the algorithm
* Takes in bus_clock frequency, required clock frequency and timing_entities (multiplexers and prescalers)
* I kept some print statements (_to showcase the code_) instead of redundant comments

### components.py
* Contains ClockConfiguration and Peripheral classes
* ClockConfiguration for setting timing_entities
* Peripheral for setting required clock frequency of a peripheral

### clock_config_algorithm.py
* Contains logic for finding the best configuration of multiplexers and prescalers
* Used as an instance, takes in ClockConfiguration parameter during instantiation

## Testing
I have created tests dictionary for storing test scripts. I have tested a few edge cases:
* Only one MUX modifies clock signal
* No modification of clock signal
* Two random inputs