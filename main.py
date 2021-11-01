from Tests.testAll import run_all_tests
from UI.console import run_meniu
from UI.commandLine import run_command_line


def main():
    run_all_tests()
    run_command_line([])


if __name__ == "__main__":
    main()
