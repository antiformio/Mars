from auxiliary.aux import (
    MAP_DIRECTIONS_LEFT,
    MAP_DIRECTIONS_RIGHT,
    POSSIBLE_INSTRUCTIONS,
)
from exceptions.robot_exceptions import (
    InstructionUnknownException,
    InstructionEmptyException,
    RobotOutOfBound,
)


class Robot:
    @staticmethod
    def compute_orders(instructions: dict) -> str:
        """
        Calculates robot final co-ordinates and heading.

        Args:
            - Instructions: dict
                Instructions contains:
                - map upper-right coordinates,
                - Current position,
                - Current orientation.
        Returns:
            - Robot's final co-ordinates and heading
        """
        map_top_right_x, map_top_right_y = instructions["map_top_right"].split()

        current_pos = instructions["current_pos"].split()
        orders = instructions["orders"].split()

        current_direction = current_pos[2]
        current_position = (int(current_pos[0]), int(current_pos[1]))

        if not instructions:
            raise InstructionEmptyException("Instructions empty.")

        if any(instruction not in POSSIBLE_INSTRUCTIONS for instruction in orders):
            raise InstructionUnknownException("Received unknown robot order.")

        for instruction in orders:
            if instruction == "M":
                if current_direction == "N":
                    current_position = (current_position[0], current_position[1] + 1)
                elif current_direction == "S":
                    current_position = (current_position[0], current_position[1] - 1)
                elif current_direction == "E":
                    current_position = (current_position[0] + 1, current_position[1])
                elif current_direction == "W":
                    current_position = (current_position[0] - 1, current_position[1])
            elif instruction == "L":
                current_direction = MAP_DIRECTIONS_LEFT.get(current_direction)
            else:
                current_direction = MAP_DIRECTIONS_RIGHT.get(current_direction)

            if current_position[0] > int(map_top_right_x) or current_position[1] > int(
                map_top_right_y
            ):
                raise RobotOutOfBound("Robot is out of plateau !!!")
        return f"{current_position[0]} {current_position[1]} {current_direction}"
