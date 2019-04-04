from bearlibterminal import terminal
from ui import UIStack
from title import TitleScene


def main():
    terminal.open()

    # generate opening scene
    ui_stack = UIStack()
    ui_stack.push(TitleScene())
    key = 0
    shift_down = False

    while key != terminal.TK_CLOSE:
        ui_stack.render()
        terminal.refresh()
        key = terminal.read()
        shift_down = bool(terminal.check(terminal.TK_SHIFT))
        ui_stack.peek().handle_input(key, shift_down)

    terminal.close()


if __name__ == "__main__":
    main()
