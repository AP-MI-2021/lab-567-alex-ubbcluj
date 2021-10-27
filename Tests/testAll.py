from Tests.testCRUD import test_adauga_obiect, test_get_by_ID, test_sterge_obiect, test_modifica_obiect
from Tests.testDomain import test_creeaza_obiect
from Tests.testFunctionalitati import test_concatenare_str, test_ordonare_cresc_dupa_pret


def run_all_tests():
    test_creeaza_obiect()
    test_adauga_obiect()
    test_get_by_ID()
    test_sterge_obiect()
    test_modifica_obiect()
    test_concatenare_str()
    test_ordonare_cresc_dupa_pret()
