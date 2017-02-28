from wpilib.command import CommandGroup
from wpilib.command.conditionalcommand import ConditionalCommand

from custom.config import Config

from ..drive.movecommand import MoveCommand
from ..drive.turncommand import TurnCommand
from .waitforliftcommand import WaitForLiftCommand
from .scoregearcommand import ScoreGearCommand

# Initiate procedure for hanging the gear at the beginning of the match.
class GearAutonomousCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('Score a Gear Autonomously')

        move = ConditionalCommand('Move Toward Lift', MoveCommand(50))
        move.condition = lambda: Config("Autonomous/robotLocation") != 0
        self.addSequential(move)
        self.addSequential(TurnCommand(Config("Autonomous/robotLocation")))
        self.addSequential(WaitForLiftCommand())
        self.addSequential(ScoreGearCommand())
