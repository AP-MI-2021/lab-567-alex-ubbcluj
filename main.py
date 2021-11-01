from Tests.testAll import run_all_tests
from UI.console import run_meniu
from UI.commandLine import run_command_line


def main():
    run_all_tests()
    choose_UI = input("Alegeti '1' pentru consola sau '2' pentru command line (functionalitati limitate!): ")
    if choose_UI == "1":
        run_meniu([])
    elif choose_UI == "2":
        run_command_line([])


if __name__ == "__main__":
    main()
