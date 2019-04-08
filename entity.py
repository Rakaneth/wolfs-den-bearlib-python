from direction import DIRS
from stats import *
from typing import List
from copy import deepcopy
from ai import AIStack
from ai_types import PlayerAI
from commands import Command


class Entity:
    COUNTER = 1

    def __init__(self, **opts):
        opts = opts or {}
        self.x = 0
        self.y = 0
        self.energy = 0
        self.stats: Stats = deepcopy(opts.get('stats', None))
        self.sec_stats: SecondaryStats = deepcopy(opts.get('sec_stats', None))
        self.vitals: Vitals = deepcopy(opts.get('vitals', None))
        self.is_player = False
        self.tags: List[str] = deepcopy(opts.get('tags', []))
        self.enemies: List[str] = deepcopy(opts.get('enemies', []))
        self.allies: List[str] = deepcopy(opts.get('allies', []))
        self.map_id = opts.get('map_id', "none")
        self.ai: AIStack = AIStack()
        self.blocking = False
        self.layer = opts.get('layer', 2)
        glyph = opts.get('glyph', None)
        if type(glyph) is str and len(glyph) == 1:
            self.glyph = ord(glyph)
        elif type(glyph) is int:
            self.glyph = glyph
        else:
            self.glyph = ord('@')

        self.id = Entity.COUNTER
        Entity.COUNTER += 1
        self.color = deepcopy(opts.get('color', 'white'))
        self.name = deepcopy(opts.get('name', 'No name'))
        self.desc = deepcopy(opts.get('desc', 'No desc'))

    def move(self, x, y):
        self.x = x
        self.y = y

    def move_by(self, direction: str):
        d = DIRS[direction]
        dx, dy = d
        self.move(dx + self.x, dy + self.y)

    def gain_energy(self):
        if self.stats:
            self.energy += self.stats.spd
        else:
            self.energy += 10

    def spend_energy(self, amt):
        self.energy -= amt

    @property
    def get_spd(self) -> int:
        if self.stats:
            return self.stats.spd
        else:
            return 0

    def set_player(self):
        self.is_player = True

    def take_action(self) -> Command:
        return self.ai.take_action(self)

    def push_player_action(self, cmd):
        for a in self.ai:
            if isinstance(a, PlayerAI):
                a.provide_cmd(cmd)
                break
