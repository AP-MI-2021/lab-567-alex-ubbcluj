from Domain.obiect import creeaza_obiect, get_ID


def adauga_obiect(ID, nume, descriere, pret_achizitie, locatie, lst):
    """
    adauga un obiect intr-o lista
    param. ID: int (nenul)
    param. nume: string (nenul)
    param. descriere: string (nenul)
    param. pret_achizitie: float (exact 4 caractere)
    param. locatie: string (exact 4 caractere)
    param. lst: lista de obiecte
    return: o lista ce contine atat elementele vechi cat si noul obiect
    """
    obiect = creeaza_obiect(ID, nume, descriere, pret_achizitie, locatie)
    return lst + [obiect]


def get_by_ID(ID, lst):
    """
    param ID: int
    param lst: lista de obiecte
    return: obiectul cu ID-ul dat sau None, daca nu exista
    """
    for obiect in lst:
        if get_ID(obiect) == ID: return obiect
    return None


def sterge_obiect(ID, lst):
    """
    sterge din lista obiectul cu ID-ul dat
    param. ID: ID-ul obiectului ce trebuie sters
    param. lst: o lista de obiecte
    return: lista fara obiectul cu ID-ul dat
    """
    return [obiect for obiect in lst if get_ID(obiect) != ID]


def modifica_obiect(ID, nume, descriere, pret_achizitie, locatie, lst):
    """
    modifica obiectul cu ID-ul dat
    param. ID: int (nenul)
    param. nume: string (nenul)
    param. descriere: string (nenul)
    param. pret_achizitie: float (exact 4 caractere)
    param. locatie: string (exact 4 caractere)
    param. lst: lista de obiecte
    return: o lista in care obiectul cu ID-ul dat este modificat
    """
    new_lst = []
    for obiect in lst:
        if obiect == get_by_ID(ID, lst):
            obiect_nou = creeaza_obiect(ID, nume, descriere, pret_achizitie, locatie)
            new_lst.append(obiect_nou)
        else: new_lst.append(obiect)
    return new_lst
