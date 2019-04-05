class Tile:
    def __init__(self, ascii: int, tile: int, fg: str = None, bg: str = None):
        self.ascii = ascii
        self.tile = tile
        self.fg = fg
        self.bg = bg
