from ui import UIScene, decorate, UIElement, UIConfig
from bearlibterminal import terminal
from entity import Entity
from gamemap import GameMap, generate_caves


class PlayScene(UIScene):
    def __init__(self):
        UIScene.__init__(self, "play")
        self.map_p = UIElement(
            UIConfig.MAP_X, UIConfig.MAP_Y, UIConfig.MAP_W, UIConfig.MAP_H)
        self.stat_p = UIElement(
            UIConfig.STAT_X, UIConfig.STAT_Y, UIConfig.STAT_W, UIConfig.STAT_H, "Stats")
        self.msg_p = UIElement(
            UIConfig.MSG_X, UIConfig.MSG_Y, UIConfig.MSG_W, UIConfig.MSG_H, "Messages")
        self.skl_p = UIElement(
            UIConfig.SKL_X, UIConfig.SKL_Y, UIConfig.SKL_W, UIConfig.SKL_H, "Skills")
        self.info_p = UIElement(
            UIConfig.INFO_X, UIConfig.INFO_Y, UIConfig.INFO_W, UIConfig.INFO_H, "Info")
        self.test_map = generate_caves(85, 85, "Mines", "mines")
        self.test_e = Entity()

    def render_map(self):
        start_x, start_y = self.test_map.cam(self.test_e.x, self.test_e.y)
        fg = None
        bg = None
        glyph = 0
        wall = GameMap.TILES['#']
        for x in range(start_x, start_x + UIConfig.MAP_W):
            for y in range(start_y, start_y + UIConfig.MAP_H):
                t = self.test_map.get_tile(x, y)
                neis = self.test_map.neighbors_int(x, y)
                if t.name == "null" and neis > 0:
                    bg = self.test_map.wall_color
                    glyph = wall.ascii
                elif t.name == "floor":
                    bg = self.test_map.floor_color
                    glyph = t.ascii
                else:
                    fg = t.fg
                    bg = t.bg
                    glyph = t.ascii
                if neis > 0:
                    screen_x, screen_y = self.test_map.to_screen(
                        x, y, self.test_e.x, self.test_e.y)
                    self.map_p.put(screen_x, screen_y, glyph, fg, bg)

        ps_x, ps_y = self.test_map.to_screen(
            self.test_e.x, self.test_e.y, self.test_e.x, self.test_e.y)
        self.map_p.put(ps_x, ps_y, self.test_e.glyph)

    def render_skills(self):
        self.skl_p.border()

    def render_stats(self):
        self.stat_p.border()

    def render_msgs(self):
        self.msg_p.border()

    def render_info(self):
        self.info_p.border()

    def render(self):
        self.render_skills()
        self.render_info()
        self.render_msgs()
        self.render_info()
        self.render_stats()
        self.render_map()

    def handle_input(self, key, shift):
        moves = {
            terminal.TK_KP_8: 'N',
            terminal.TK_UP: 'N',
            terminal.TK_KP_9: 'NE',
            terminal.TK_KP_6: 'E',
            terminal.TK_RIGHT: 'E',
            terminal.TK_KP_3: 'SE',
            terminal.TK_KP_2: 'S',
            terminal.TK_DOWN: 'S',
            terminal.TK_KP_1: 'SW',
            terminal.TK_KP_4: 'W',
            terminal.TK_LEFT: 'W',
            terminal.TK_KP_7: 'NW'
        }

        d = moves.get(key, None)

        if d:
            self.test_e.move_by(d)
        else:
            print(f'Key {key} was pressed.')
