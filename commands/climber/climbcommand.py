from wpilib.command import Command

import subsystems

class ClimbCommand(Command):
    # Initialize the named command.
    def __init__(self):
        super().__init__('Climb')

        self.requires(subsystems.climber)

    def initialize(self):
        subsystems.climber.start()

    def isFinished(self):
        return subsystems.climber.atTop()

    def end(self):
        subsystems.climber.stop()