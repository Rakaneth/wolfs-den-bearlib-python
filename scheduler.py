from entity import Entity
from typing import List


class Scheduler:
    ACTION_REQ_ENERGY = 100

    def __init__(self):
        self.actors: List[Entity] = []
        self.running = False
        self.__clock = 0.0

    def process(self):
        if self.running:
            self.actors.sort(key=lambda a: a.get_spd)
            for actor in self.actors:
                actor.gain_energy()
                if actor.energy >= Scheduler.ACTION_REQ_ENERGY:
                    actor.take_action()
            self.__clock += 0.1

    @property
    def clock(self):
        return self.__clock

    def add(self, actor: Entity):
        self.actors.append(actor)

    def remove(self, actor: Entity):
        self.actors.remove(actor)
