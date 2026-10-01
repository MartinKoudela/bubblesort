import sys


def main() -> None:
    if "--cli" in sys.argv[1:]:
        from frontend.cli import main as run
    else:
        from frontend.gui import main as run
    run()


if __name__ == "__main__":
    main()
