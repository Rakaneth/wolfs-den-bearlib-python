from bearlibterminal import terminal
from ui import UIStack, UIManager
from title import TitleScene


def main():
    terminal.open()

    # generate opening scene
    UIManager.push(TitleScene())
    key = 0
    shift_down = False

    # main game loop
    while key != terminal.TK_CLOSE:
        terminal.clear()
        UIManager.render()
        terminal.refresh()
        key = terminal.read()
        shift_down = bool(terminal.check(terminal.TK_SHIFT))
        UIManager.peek().handle_input(key, shift_down)

        # if no UIs to show, game is closed
        if UIManager.empty:
            break

    # cleanup
    UIManager.clear()  # if the close button was clicked with UIs on the stack
    terminal.close()


if __name__ == "__main__":
    main()
