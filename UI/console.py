from Domain.obiect import to_string
from Logic.CRUD import adauga_obiect, sterge_obiect, modifica_obiect


def print_meniu():
    print("1. Adaugare obiect")
    print("2. Stergere obiect")
    print("3. Modificare obiect")
    print("a. Afisare obiecte")
    print("x. Iesire")


def console_adauga_obiect(lst):
    ID = int(input("Dati ID-ul: "))
    nume = input("Dati numele: ")
    descriere = input("Dati descrierea: ")
    pret_achizitie = float(input("Dati pretul de achizitie: "))
    locatie = input("Dati locatia: ")
    return adauga_obiect(ID, nume, descriere, pret_achizitie, locatie, lst)


def console_sterge_obiect(lst):
    ID = int(input("Dati ID-ul obiectului de sters: "))
    return sterge_obiect(ID, lst)


def console_modifica_obiect(lst):
    ID = int(input("Dati ID-ul obiectului de modificat: "))
    nume = input("Dati noul nume: ")
    descriere = input("Dati noua descriere: ")
    pret_achizitie = float(input("Dati noul pret de achizitie: "))
    locatie = input("Dati noua locatie: ")
    return modifica_obiect(ID, nume, descriere, pret_achizitie, locatie, lst)


def show_all(lst):
    for obiect in lst:
        print(to_string(obiect))


def run_meniu(lst):
    while True:
        print_meniu()
        optiune = input("Alegeti optiunea: ")
        if optiune == "1": 
            lst = console_adauga_obiect(lst)
        elif optiune == "2": 
            lst = console_sterge_obiect(lst)
        elif optiune == "3": 
            lst = console_modifica_obiect(lst)
        elif optiune == "a":
            show_all(lst)
        elif optiune == "x": 
            break
        else: 
            print("Optiune invalida!")

