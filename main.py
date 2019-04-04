from bearlibterminal import terminal


def main():
    terminal.open()
    terminal.print_(0, 0, "Hello Python and BearLib!")
    terminal.refresh()

    while terminal.read() != terminal.TK_CLOSE:
        pass

    terminal.close()


if __name__ == "__main__":
    main()
