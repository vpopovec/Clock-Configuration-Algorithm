from itertools import product
from math import prod
from collections import defaultdict


class ClockConfigAlgorithm:
    """
    logic for finding the best configuration of multiplexers and prescalers
    """

    def __init__(self, clock):
        self.clock = clock

    def calculate(self, bus_clock, peripheral):
        timing_entities = self.clock.timing_entities
        required_frequency = peripheral.required_clock_frequency
        prescalers = timing_entities.values()

        result_combinations = defaultdict(list)
        min_deviation = None
        for prescaler_combination in product(*prescalers):
            output_frequency = bus_clock / prod(prescaler_combination)
            deviation = abs(required_frequency - output_frequency)
            # We could return prematurely after first match (deviation == 0) to save computing power

            if min_deviation is not None and deviation > min_deviation:
                continue
            min_deviation = deviation

            result_combinations[deviation].append(prescaler_combination)

        best_configurations = get_best_configuration(result_combinations)
        return best_configurations, bus_clock / prod(best_configurations[0])


def get_best_configuration(combs):
    min_deviation = min(combs.keys())
    return combs[min_deviation]
