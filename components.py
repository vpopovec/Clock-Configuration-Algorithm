class ClockConfiguration:
    def __init__(self, timing_entities):
        """
        :param timing_entities: dict of multiplexers, each containing all possible prescaler divisors,
                                e.g. {1: [2, 4, 8, 16]}
        """

        # Assign direct input
        self.timing_entities = {
            mux: [1, *prescalers] for mux, prescalers in timing_entities.items()
        }


class Peripheral:
    """
    specifications of the peripheral and the required clock frequency
    """

    def __init__(self, required_clock_frequency):
        """
        :param required_clock_frequency: inputted in MHz
        """
        self.required_clock_frequency = required_clock_frequency
