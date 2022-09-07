from auxiliary.aux import (
    # MAP_DIRECTIONS_LEFT,
    # MAP_DIRECTIONS_RIGHT,
    MAP_INPUT_DIRECTION_TO_COORDINATES,
    POSSIBLE_INSTRUCTIONS,
)
from exceptions.robot_exceptions import (
    InstructionUnknownException,
    InstructionEmptyException,
    RobotOutOfBound,
    InputProcessingException,
)


class Robot:
    def _process_input(self, instructions):
        self.map_top_right_x, self.map_top_right_y = instructions[
            "map_top_right"
        ].split()
        self.current_pos = instructions["current_pos"].split()
        self.orders = instructions["orders"].split()

        self.current_direction = MAP_INPUT_DIRECTION_TO_COORDINATES.get(self.current_pos[2])
        self.current_position = (int(self.current_pos[0]), int(self.current_pos[1]))

    def compute_orders(self, instructions: dict) -> str:
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
        try:
            self._process_input(instructions)
        except Exception as error:
            raise InputProcessingException(f"Error parsing input - {error}") from error

        if not instructions:
            raise InstructionEmptyException("Instructions empty.")

        if any(instruction not in POSSIBLE_INSTRUCTIONS for instruction in self.orders):
            raise InstructionUnknownException("Received unknown robot order.")

        for instruction in self.orders:
            if instruction == "M":
                self.current_position = (self.current_position[0] + self.current_direction[0], 
                                         self.current_position[1] + self.current_direction[1])
            elif instruction == "L":
                # A left rotation is equivalent of: direction_x, direction_y = -direction_y, direction_x
                self.current_direction[0], self.current_direction[1] = -self.current_direction[1], \
                                                                       self.current_direction[0]
            else:
                # A right rotation is equivalent of: direction_x, direction_y = direction_y, -direction_x
                self.current_direction[0], self.current_direction[1] = self.current_direction[1], \
                                                                       -self.current_direction[0]


            if self.current_position[0] > int(
                self.map_top_right_x
            ) or self.current_position[1] > int(self.map_top_right_y):
                raise RobotOutOfBound("Robot is out of plateau !!!")
        return f"{self.current_position[0]} {self.current_position[1]} " \
               f"{[k for k,v in MAP_INPUT_DIRECTION_TO_COORDINATES.items() if v == self.current_direction][0]}"
