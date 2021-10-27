from Domain.obiect import get_descriere, get_pret_achizitie


def concatenare_str(obiect, str):
	"""
	concateneaza un string la descrierea unui obiect
	param. obiect: obiectul
	param. str: stringul
	return: obiectul dupa concatenarea stringului la descriere
	"""
	obiect["descriere"] = get_descriere(obiect) + str
	return obiect


def ordonare_cresc_dupa_pret(lst):
	"""
	ordoneaza crescator o lista de obiecte in functie de pretul de achizitie
	param. lst: lista de obiecte
	return: lista ordonata crescator
	"""
	return sorted(lst, key = get_pret_achizitie)
