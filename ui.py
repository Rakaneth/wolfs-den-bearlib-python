from bearlibterminal import terminal


class UIElement:
    def __init__(self, x: int, y: int, w: int, h: int, caption: str = None):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.x2 = self.x + self.width - 1
        self.y2 = self.y + self.height - 1
        self.caption = caption

    def print(self, x: int, y: int, text: str):
        terminal.print_(x + self.x, y + self.y, text)

    def put(self, x: int, y: int, code: int, fg: str = None, bg: str = None):
        if fg:
            terminal.color(fg)
        if bg:
            terminal.bkcolor(bg)
        terminal.put(x + self.x, y + self.y, code)
        terminal.color("white")
        terminal.bkcolor("black")

    def border(self):
        UL = 0x2554
        UR = 0x2557
        LL = 0x255A
        LR = 0x255D
        HORZ = 0x2550
        VERT = 0x2551
        x2 = self.width - 1
        y2 = self.height - 1

        for x in range(1, x2):
            self.put(x, 0, HORZ)
            self.put(x, y2, HORZ)

        for y in range(1, y2):
            self.put(0, y, VERT)
            self.put(x2, y, VERT)

        self.put(0, 0, UL)
        self.put(x2, 0, UR)
        self.put(0, y2, LL)
        self.put(x2, y2, LR)

        if self.caption:
            self.print(1, 0, self.caption)


class UIScene:
    def __init__(self, name: str):
        self.name = name

    def enter(self):
        print(f"Entered {self.name} screen")

    def exit(self):
        print(f"Exited {self.name} screen")

    def render(self):
        raise NotImplementedError

    def handle_input(self, key: int, shift: bool):
        raise NotImplementedError


class UIStack:
    def __init__(self):
        self.scenes = []

    def push(self, *scenes: UIScene):
        for scene in scenes:
            scene.enter()
            self.scenes.append(scene)

    def pop(self) -> UIScene:
        leaving = self.scenes.pop()
        leaving.exit()
        return leaving

    def render(self):
        for scene in self.scenes:
            scene.render()

    def peek(self) -> UIScene:
        return self.scenes[-1]

    def clear(self):
        while len(self.scenes) > 0:
            self.pop()

    @property
    def empty(self) -> bool:
        return len(self.scenes) == 0


class UIConfig:
    SCREEN_W = 100
    SCREEN_H = 40
    MAP_W = 60
    MAP_H = 30
    MAP_X = 0
    MAP_Y = 0
    STAT_W = SCREEN_W - MAP_W
    STAT_H = MAP_H
    STAT_X = MAP_W
    STAT_Y = 0
    MSG_W = MAP_W // 2
    MSG_H = SCREEN_H - MAP_H
    MSG_X = 0
    MSG_Y = MAP_H
    SKL_W = MSG_W
    SKL_H = MSG_H
    SKL_X = MSG_W
    SKL_Y = MSG_Y
    INFO_W = STAT_W
    INFO_H = MSG_H
    INFO_X = MAP_W
    INFO_Y = MSG_Y


def write_center(y: int, text: str):
    screen_w = int(terminal.get("ini.game.screen_width", "100"))
    w, _ = terminal.measure(text)
    x = (screen_w - w) // 2
    terminal.print_(x, y, text)


def decorate(text: str, color: str = None, background_color: str = None) -> str:
    prefix = ''
    postfix = ''
    if color:
        prefix += f'[color={color}]'
    if background_color:
        prefix += f'[bkcolor={background_color}]'
    if color or background_color:
        postfix = '[/color]'

    return f'{prefix}{text}{postfix}'


UIManager = UIStack()
