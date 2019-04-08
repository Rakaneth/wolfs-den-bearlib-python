from entity import Entity


class Command:
    def execute(self, entity: Entity) -> int:
        return 0


class MoveByCommand(Command):
    def __init__(self, dx: int, dy: int):
        self.dx = dx
        self.dy = dy

    def execute(self, entity: Entity) -> int:
        # TODO: try-move logic
        entity.x += self.dx
        entity.y += self.dy
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
