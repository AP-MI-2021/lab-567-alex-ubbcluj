from Domain.obiect import to_string
from Logic.CRUD import adauga_obiect, modifica_obiect, sterge_obiect


def print_help():
    print("Comenzi disponibile:")
    print("help")
    print("print")
    print("add")
    print("update")
    print("delete")
    print("stop")


def cmd_show_all(lst):
    for obiect in lst:
        print(to_string(obiect))


def run_command_line(lst):
    while True:
        cmd = input()
        if cmd == "help":
            print_help()
        elif cmd == "print":
            cmd_show_all(lst)
        elif cmd == "stop":
            break
        else:
            try:
                lista_comenzi = cmd.split("; ")
                for comanda in lista_comenzi:
                    lista_param = comanda.split(", ")
                    if lista_param[0] == "add":
                        lst = adauga_obiect(int(lista_param[1]), lista_param[2], lista_param[3], float(lista_param[4]), lista_param[5], lst)
                    elif lista_param[0] == "update":
                        lst = modifica_obiect(int(lista_param[1]), lista_param[2], lista_param[3], float(lista_param[4]), lista_param[5], lst)
                    elif lista_param[0] == "delete":
                        lst = sterge_obiect(int(lista_param[1]), lst)
            except ValueError as ve:
                print("Eroare: {}".format(ve))
