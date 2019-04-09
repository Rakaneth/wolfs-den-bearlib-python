from entity import Entity


class Command:
    def execute(self, entity: Entity):
        pass


class CommandResult:
    def __init__(self, energy_cost: int = 100, alt_cmd: Command = None):
        self.alternate: Command = alt_cmd
        if alt_cmd:
            self.__done = False
        else:
            self.__done = True
        self.cost = energy_cost


class MoveByCommand(Command):
    def __init__(self, dx: int, dy: int):
        self.dx = dx
        self.dy = dy

    def execute(self, entity: Entity) -> int:
        # TODO: try-move logic
        nx = entity.x + dx
        ny = entity.y + dy
        # if entity.g
        return 100


class WaitCommand(Command):
    def execute(self, entity: Entity) -> int:
        return 100


class OutOfWorldCommand(Command):
    def execute(self, entity: Entity) -> int:
        return 0


def process_command(actor: Entity, cmd: Command):
    spent = cmd.execute(actor)
    actor.energy -= spent
