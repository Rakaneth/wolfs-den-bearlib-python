from ai import AI
from gamestate import GAME
from random import choice


class PlayerAI(AI):
    def take_action(self):
        GAME.pause()


class WanderAI(AI):
    DIRS = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']

    def take_action(self, actor):
        d = choice(WanderAI.DIRS)
        actor.move_by(d)
        actor.energy -= 100


class EffectAI(AI):
    def __init__(self, duration: int, affected, eff_cb):
        self.eff_cb = eff_cb
        self.duration = duration
        self.affected = affected

    def take_action(self, actor):
        self.eff_cb(self.affected)
        self.duration -= 1
        if self.duration <= 0:
            GAME.remove(actor)
