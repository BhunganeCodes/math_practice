import unittest
from project_km5 import *


class TestProjectKM5(unittest.TestCase):
    def test_breakeven_point(self):
        # Parallel lines: no breakeven
        self.assertIs(
            breakeven_point((100, 10), (200, 10)),
            -1,
        )

        # Breakeven at 20 units
        self.assertAlmostEqual(
            breakeven_point((50, 5), (100, 3)),
            25.0,
        )

    def test_negative_slope(self):
        # Negative slope breakeven
        self.assertAlmostEqual(
            breakeven_point((300, 15), (100, 5)),
            -20.0,
        )

    def test_infinite_intersections(self):
        # Identical lines: infinite intersections treated as no breakeven
        self.assertIs(
            breakeven_point((100, 10), (100, 10)),
            -1,
        )

    def test_breakeven_zero(self):
        # Breakeven at zero units
        self.assertAlmostEqual(
            breakeven_point((0, 5), (0, 2)),
            0.0,
        )

    def test_larger_values(self):
        # Larger values
        self.assertAlmostEqual(
            breakeven_point((1000, 50), (500, 25)),
            -20.0,
        )

    def test_net_flow_accumulation(self):
        # Simple increasing flow
        self.assertAlmostEqual(
            net_flow_accumulation([2, 3, 4], 0, 2),
            19.333333333333332,
        )

    def test_negative_values(self):
        # Flow with negative values
        self.assertAlmostEqual(
            net_flow_accumulation([50, -20, 5], 1, 3),
            363.33333333333337,
        )

    def test_quadratic_flow(self):
        # Pure quadratic flow
        self.assertAlmostEqual(
            net_flow_accumulation([1, 0, 0], 0, 3),
            9.0,
        )

    def test_negative_coefficient(self):
        # Negative quadratic coefficient
        self.assertAlmostEqual(
            net_flow_accumulation([-2, 4, 1], 0, 2),
            4.666666666666667,
        )


if __name__ == "__main__":
    unittest.main()