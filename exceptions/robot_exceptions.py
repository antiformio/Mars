class RobotException(Exception):
    """General robot exception"""

    def __init__(self, message):
        self.message = message


class InstructionUnknownException(RobotException):
    pass


class InstructionEmptyException(RobotException):
    pass


class RobotOutOfBound(RobotException):
    pass


class InputProcessingException(RobotException):
    pass
