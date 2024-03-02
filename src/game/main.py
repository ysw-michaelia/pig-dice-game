from menu import Menu
from score import Score


def main():
    """Run the main program."""
    score = Score()
    menu = Menu(score)
    menu.menu_main()


if __name__ == "__main__":
    main()
