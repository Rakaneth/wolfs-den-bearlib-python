from entity import Entity
from creatures import CREATURES


def make_creature(build_id: str, **more_opts) -> Entity:
    opts = CREATURES[build_id]
    opts['layer'] = 3
    opts.update(more_opts)
    return Entity(**opts)
