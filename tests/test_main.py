import unittest
from main import main
from clock_config_algorithm import get_best_configuration


class TestAlgorithm(unittest.TestCase):
    timing_entities = {
        1: [2, 4, 8, 16],
        2: [2, 3, 4, 5]
    }

    def test_16_on_1(self):
        active_inputs, freq = main(bus_clock=16, required_clock_frequency=1, timing_entities=self.timing_entities)
        self.assertCountEqual(active_inputs, [[3, 4], [4, 2], [5, 1]], "Should yield 3 solutions")
        self.assertEqual(freq, 1, "Output frequency should be 1MHz")

    def test_32_on_4(self):
        active_inputs, freq = main(bus_clock=32, required_clock_frequency=4, timing_entities=self.timing_entities)
        self.assertCountEqual(active_inputs, [[2, 4], [3, 2], [4, 1]], "Should yield 3 solutions")
        self.assertEqual(freq, 4, "Output frequency should be 4MHz")

    def test_no_clocking(self):
        active_inputs, freq = main(bus_clock=8, required_clock_frequency=8, timing_entities=self.timing_entities)
        self.assertCountEqual(active_inputs, [[1, 1]], "Should yield active inputs 1 and 1")
        self.assertEqual(freq, 8, "Output frequency should be 8MHz")

    def test_one_mux(self):
        active_inputs, freq = main(bus_clock=16, required_clock_frequency=8, timing_entities=self.timing_entities)
        self.assertCountEqual(active_inputs, [[2, 1], [1, 2]], "Should yield two solutions")
        self.assertEqual(freq, 8, "Output frequency should be 8MHz")

    def test_get_best_configuration(self):
        combinations = {3.0: [(2, 2)], 1.66: [(2, 3)], 0.33: [(4, 3)], 0.0: [(4, 4), (8, 2)]}
        best_config = get_best_configuration(combinations)
        self.assertEqual(best_config, [(4, 4), (8, 2)], "Best config should equal 4, 4")
