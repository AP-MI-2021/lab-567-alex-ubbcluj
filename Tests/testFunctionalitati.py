from Domain.obiect import creeaza_obiect, get_descriere, get_ID
from Logic.CRUD import adauga_obiect
from Logic.functionalitati import concatenare_str, ordonare_cresc_dupa_pret


def test_concatenare_str():
    obiect = creeaza_obiect(256, "Monitor Dell", "23.8'', Full HD, 144Hz", 1099, "C503")
    str = " string de test"
    obiect = concatenare_str(obiect, str)
    assert get_descriere(obiect) == "23.8'', Full HD, 144Hz string de test"


def test_ordonare_cresc_dupa_pret():
    lst = []
    lst = adauga_obiect(1, "obiect test 1", "descriere 1", 4000, "----", lst)
    lst = adauga_obiect(2, "obiect test 2", "descriere 2", 1000, "----", lst)
    lst = adauga_obiect(3, "obiect test 3", "descriere 3", 3000, "----", lst)
    lst = adauga_obiect(4, "obiect test 4", "descriere 4", 2000, "----", lst)
    lst = ordonare_cresc_dupa_pret(lst)
    assert get_ID(lst[0]) == 2
    assert get_ID(lst[1]) == 4
    assert get_ID(lst[2]) == 3
    assert get_ID(lst[3]) == 1