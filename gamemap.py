from tile import Tile
from typing import List
from opensimplex import OpenSimplex
from utils import clamp
from ui import UIConfig


class MapTile(Tile):
    def __init__(self, name: str = "null", glyph: int = 0, tile: int = None, fg: str = None, bg: str = None, walk: bool = False, see: bool = False):
        Tile.__init__(self, glyph, tile, fg, bg)
        self.walk = walk
        self.see = see
        self.name = name


class GameMap:
    TILES = {
        '#': MapTile(name="wall", glyph=ord(' ')),
        '.': MapTile(name="floor", glyph=ord(' '), tile=0xE541, walk=True, see=True),
        '+': MapTile(name="closed door", glyph=ord('+'), fg="white", bg="sepia"),
        '/': MapTile(name="open door", glyph=ord('/'), fg="white", bg="sepia", walk=True, see=True),
        'x': MapTile(),
        '>': MapTile(name="down stairs", glyph=ord('>'), fg="yellow", walk=True, see=True),
        '<': MapTile(name="up stairs", glyph=ord('<'), fg="yellow", walk=True, see=True)
    }

    def __init__(self, **opts):
        self.width = opts['width']
        self.height = opts['height']
        self.tiles = {}
        self.lit = opts.get('lit', True)
        self.connections = {}
        self.id = opts['id']
        self.name = opts['name']
        self.explored = set()
        self.wall_color = opts.get('wall_color', 'dark stone')
        self.floor_color = opts.get('floor_color', 'stone')

    def in_bounds(self, x: int, y: int) -> bool:
        return (0 <= x < self.width) and (0 <= y < self.height)

    def get_tile(self, x: int, y: int) -> MapTile:
        tile_symbol = self.tiles.get((x, y), 'x')
        return GameMap.TILES[tile_symbol]

    def set_tile(self, x: int, y: int, tile_symbol: str):
        self.tiles.update({(x, y): tile_symbol})

    def explore(self, x: int, y: int):
        self.explored.add((x, y))

    def is_explored(self, x: int, y: int) -> bool:
        return (x, y) in self.explored

    def neighbors(self, x: int, y: int) -> List[tuple]:
        return [
            (xs, ys)
            for xs in range(x-1, x+2)
            for ys in range(y-1, y+2)
            if self.get_tile(xs, ys).walk
            if xs != x or ys != y]

    def cam(self, x: int, y: int) -> tuple:
        def calc(p: int, m: int, s: int):
            return clamp(p - s // 2, 0, max(0, m-s))

        left = calc(x, self.width, UIConfig.MAP_W)
        top = calc(y, self.height, UIConfig.MAP_H)
        return (left, top)

    def to_screen(self, x: int, y: int, fx: int, fy: int) -> tuple:
        cx, cy = self.cam(fx, fy)
        return (x-cx, y-cy)


def generate_caves(w: int, h: int, name: str, id: str, lit: bool = True) -> GameMap:
    new_map = GameMap(width=w, height=h, name=name, id=id, lit=lit)
    simp = OpenSimplex()
    for x in range(w):
        for y in range(h):
            nx = x / w
            ny = y / h
            o1 = simp.noise2d(nx, ny)
            o2 = simp.noise2d(2 * nx, 2 * ny) * 0.5
            o3 = simp.noise2d(4 * nx, 4 * ny) * 0.25
            o4 = simp.noise2d(8 * nx, 8 * ny) * 0.125
            v = o1 + o2 + o3 + o4
            if v > -0.2:
                new_map.set_tile(x, y, '.')
    return new_map
