from ui import UIScene, write_center, decorate


class TitleScene(UIScene):
    def __init__(self):
        UIScene.__init__(self, "title")

    def render(self):
        write_center(
            20, f"Wolf's Den II: {decorate('Python + BearLib Edition', 'yellow')}")
        write_center(21, "by Rakaneth")
        write_center(23, "Press any key to start")

    def handle_input(self, key: int, shift_down: bool):
        print(f'Key {key} pressed. Shift: {"down" if shift_down else "not down"}')
