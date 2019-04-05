from entity import Entity
from creatures import CREATURES


def make_creature(build_id: str) -> Entity:
    opts = CREATURES[build_id]
    return Entity(**opts)
