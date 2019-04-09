from typing import List, Dict
from entity import Entity
from scheduler import Scheduler
from gamemap import GameMap


class GameState:
    def __init__(self):
        self.scheduler = Scheduler()
        self.entities: Dict[str, Entity] = {}
        self.maps: Dict[str, GameMap] = {}
        self.cur_map_id = "none"

    @property
    def cur_map(self) -> GameMap:
        return self.maps[self.cur_map_id]

    @property
    def cur_things(self) -> List[Entity]:
        return [e for e in self.entities.values() if e.map_id == self.cur_map_id]

    @property
    def player(self) -> Entity:
        return next((e for e in self.entities.values() if e.is_player), None)

    def things_at(self, x: int, y: int) -> List[Entity]:
        [e for e in self.cur_things if e.x == x and e.y == y]

    def pause(self):
        self.scheduler.running = False

    def resume(self):
        self.scheduler.running = True

    def add(self, entity: Entity):
        self.entities.update({entity.id: entity})
        if not entity.ai.empty:
            self.scheduler.add(entity)

    def remove(self, entity: Entity):
        del self.entities[entity.id]
        self.scheduler.remove(entity)

    def add_map(self, m: GameMap):
        self.maps[m.id] = m


GAME = GameState()
