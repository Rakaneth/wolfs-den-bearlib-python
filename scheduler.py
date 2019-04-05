from entity import Entity
from typing import List


class Scheduler:
    def __init__(self):
        self.actors: List[Entity] = []
        self.running = False

    def process(self):
        if self.running:
            self.actors.sort(key=lambda a: a.get_spd)
            for actor in self.actors:
                actor.gain_energy()
                if actor.energy >= 100:
                    if actor.is_player:
                        self.running = False
                    else:
                        actor.take_action()

    def add(self, actor: Entity):
        self.actors.append(actor)
