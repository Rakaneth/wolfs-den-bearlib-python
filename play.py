from ui import UIScene, decorate, UIElement, UIConfig
from bearlibterminal import terminal
from entity import Entity


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
        self.test_e = Entity()

    def render_map(self):
        self.map_p.put(self.test_e.x, self.test_e.y, self.test_e.glyph)

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
