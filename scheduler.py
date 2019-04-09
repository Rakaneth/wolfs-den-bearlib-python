from entity import Entity
from collections import deque
from commands import Command, process_command


class Scheduler:
    ACTION_REQ_ENERGY = 100

    def __init__(self):
        self.actors: deque = deque()
        self.running = False
        self.__clock = 0.0

    def process(self):
        while True:
            cur_actor = self.actors.pop()
            cur_actor.gain_energy()
            if cur_actor.energy >= Scheduler.ACTION_REQ_ENERGY:
                if cur_actor.is_player and cur_actor.needs_input:
                    return
                else:
                    cmd = cur_actor.take_action()
                    process_command(cur_actor, cmd)
        self.__clock += 0.1

    @property
    def clock(self):
        return self.__clock

    def add(self, actor: Entity):
        self.actors.append(actor)

    def remove(self, actor: Entity):
        self.actors.remove(actor)
