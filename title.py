from ui import UIScene, write_center, decorate, UIManager
from bearlibterminal import terminal
from play import PlayScene


class TitleScene(UIScene):
    def __init__(self):
        UIScene.__init__(self, "title")

    def render(self):
        write_center(
            20, f"Wolf's Den II: {decorate('Python + BearLib Edition', 'yellow')}")
        write_center(21, "by Rakaneth")
        write_center(23, "Press any key to start")

    def handle_input(self, key: int, shift_down: bool):
        UIManager.pop()
        UIManager.push(PlayScene())
