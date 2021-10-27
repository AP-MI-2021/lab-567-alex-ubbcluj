from Domain.obiect import to_string, get_pret_achizitie
from Logic.CRUD import adauga_obiect, sterge_obiect, modifica_obiect
from Logic.functionalitati import concatenare_str, ordonare_cresc_dupa_pret


def print_meniu():
    print("1. Adaugare obiect")
    print("2. Stergere obiect")
    print("3. Modificare obiect")
    #print("4. Mutarea tuturor obiectelor dintr-o locație în alta")
    print("5. Concatenarea unui string citit la toate descrierile obiectelor cu prețul mai mare decât o valoare citită")
    #print("6. Determinarea celui mai mare preț pentru fiecare locație")
    print("7. Afisarea obiectelor ordonate crescător după prețul de achiziție")
    #print("8. Afișarea sumelor prețurilor pentru fiecare locație")
    #print("9. Undo")
    print("a. Afisare obiecte")
    print("x. Iesire")


def console_adauga_obiect(lst):
    ID = int(input("Introduceti ID-ul: "))
    nume = input("Introduceti numele: ")
    descriere = input("Introduceti descrierea: ")
    pret_achizitie = float(input("Introduceti pretul de achizitie: "))
    locatie = input("Introduceti locatia: ")
    return adauga_obiect(ID, nume, descriere, pret_achizitie, locatie, lst)


def console_sterge_obiect(lst):
    ID = int(input("Introduceti ID-ul obiectului de sters: "))
    return sterge_obiect(ID, lst)


def console_modifica_obiect(lst):
    ID = int(input("Introduceti ID-ul obiectului de modificat: "))
    nume = input("Introduceti noul nume: ")
    descriere = input("Introduceti noua descriere: ")
    pret_achizitie = float(input("Introduceti noul pret de achizitie: "))
    locatie = input("Introduceti noua locatie: ")
    return modifica_obiect(ID, nume, descriere, pret_achizitie, locatie, lst)


def console_concatenare_str(lst):
    str = input("Introduceti stringul: ")
    console_pret = int(input("Introduceti un pret: "))
    for obiect in lst:
        if get_pret_achizitie(obiect) > console_pret:
            obiect = concatenare_str(obiect, str)
    return lst


def console_ordonare_cresc_dupa_pret(lst):
    show_all(ordonare_cresc_dupa_pret(lst))


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
        elif optiune == "4":
            pass
        elif optiune == "5":
            lst = console_concatenare_str(lst)
        elif optiune == "6":
            pass
        elif optiune == "7":
            console_ordonare_cresc_dupa_pret(lst)
        elif optiune == "8":
            pass
        elif optiune == "9":
            pass
        elif optiune == "a":
            show_all(lst)
        elif optiune == "x": 
            break
        else: 
            print("Optiune invalida!")
