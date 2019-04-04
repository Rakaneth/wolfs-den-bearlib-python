from ui import UIScene, write_center


class TitleScene(UIScene):
    def __init__(self):
        UIScene.__init__(self, "title")

    def render(self):
        write_center(20, "Wolf's Den II: Python + BearLib Edition")
        write_center(21, "by Rakaneth")
        write_center(23, "Press any key to start")

    def handle_input(self, key: int, shift_down: bool):
        print(f'Key {key} pressed. Shift: {"down" if shift_down else "not down"}')
