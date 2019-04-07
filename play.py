from ui import UIScene, decorate, UIElement, UIConfig
from bearlibterminal import terminal
from entity import Entity
from gamemap import GameMap, generate_caves
from factory import make_creature
from gamestate import GAME
from ai_types import PlayerAI


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

    def render_map(self):
        m = GAME.cur_map
        p = GAME.player
        start_x, start_y = m.cam(p.x, p.y)
        fg = None
        bg = None
        glyph = 0
        wall = GameMap.TILES['#']
        for x in range(start_x, start_x + UIConfig.MAP_W):
            for y in range(start_y, start_y + UIConfig.MAP_H):
                t = m.get_tile(x, y)
                neis = m.neighbors_int(x, y)
                if t.name == "null" and neis > 0:
                    bg = m.wall_color
                    glyph = wall.ascii
                elif t.name == "floor":
                    bg = m.floor_color
                    glyph = t.ascii
                else:
                    fg = t.fg
                    bg = t.bg
                    glyph = t.ascii
                if neis > 0:
                    screen_x, screen_y = m.to_screen( x, y, p.x, p.y)
                    self.map_p.put(screen_x, screen_y, glyph, fg, bg)

        for e in sorted(GAME.cur_things, key=lambda a: a.layer, reverse=True):
            ps_x, ps_y = m.to_screen(e.x, e.y, e.x, e.y)
            if 0 <= ps_x < UIConfig.MAP_W and 0 <= ps_y < UIConfig.MAP_H:
                self.map_p.put(ps_x, ps_y, e.glyph, e.color)

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
            GAME.player.move_by(d)
        else:
            print(f'Key {key} was pressed.')
    
    def enter(self):
        player=Entity(layer=4, color='cyan', map_id="mines")
        player.set_player()
        player.ai.push(PlayerAI())
        player.move(1, 1)
        wolf = make_creature('wolf', color='yellow', map_id="mines")
        mines = generate_caves(85, 85, "Mines", "mines")
        GAME.add_map(mines)
        GAME.add(player)
        GAME.add(wolf)
        GAME.cur_map_id = "mines"
        UIScene.enter(self)
