from components import ClockConfiguration, Peripheral
from clock_config_algorithm import ClockConfigAlgorithm
BUS_CLOCK = 16  # MHz
ACTIVE_INPUT_START_INDEX = 1


def main(bus_clock=BUS_CLOCK, required_clock_frequency=1, timing_entities=None):
    if timing_entities is None:
        timing_entities = {
            1: [2, 4, 8, 16],
            2: [2, 3, 4, 5]
        }

    clock = ClockConfiguration(timing_entities)
    peripheral = Peripheral(required_clock_frequency)

    alg = ClockConfigAlgorithm(clock)
    configuration, output_frequency = alg.calculate(bus_clock, peripheral)

    active_inputs = [[] for _ in configuration]
    for index_solution, solution in enumerate(configuration):
        print(f"Configuration option #{index_solution+1}")

        for indx, divisor in enumerate(solution):
            mux = indx + 1
            active_input = get_active_input(clock, indx, divisor)
            active_inputs[index_solution].append(active_input)
            print(f"Multiplexer {mux} active input {active_input}")

        print(f"Achieved frequency: {output_frequency}MHz\n")

    return active_inputs, output_frequency


def get_active_input(clock, indx, divisor):
    prescalers = list(clock.timing_entities.values())[indx]
    return prescalers.index(divisor) + ACTIVE_INPUT_START_INDEX


if __name__ == '__main__':
    main()

