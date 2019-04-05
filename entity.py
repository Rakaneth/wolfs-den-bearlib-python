from direction import DIRS


class Entity:
    def __init__(self, **opts):
        opts = opts or {}
        self.x = 0
        self.y = 0
        glyph = opts.get('glyph', None)
        if type(glyph) is str and len(glyph) == 1:
            self.glyph = ord(glyph)
        elif type(glyph) is int:
            self.glyph = glyph
        else:
            self.glyph = ord('@')

        self.color = opts.get('color', 'white')

    def move(self, x, y):
        self.x = x
        self.y = y

    def move_by(self, direction: str):
        d = DIRS[direction]
        dx, dy = d
        self.move(dx + self.x, dy + self.y)
