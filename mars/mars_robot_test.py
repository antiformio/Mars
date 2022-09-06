import pytest
from mars_robot import Robot

TESTS = [
    ({
        "map_top_right": "5 5",
        "current_pos": "1 2 N",
        "orders": "L M L M L M L M M"
     },
     ("1 3 N")),
    ({
        "map_top_right": "5 5",
        "current_pos": "3 3 E",
        "orders": "M M R M M R M R R M"
    },
    ("5 1 E")),
]


class TestRobot:
    @pytest.mark.parametrize("test_input,expected", TESTS)
    def test_compute_orders(self, test_input, expected):
        rb = Robot()
        assert rb.compute_orders(test_input) == expected
