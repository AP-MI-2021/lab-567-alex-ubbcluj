from Domain.obiect import get_descriere, get_pret_achizitie, get_locatie


def mutare_obiecte(old_loc, new_loc, lst):
	"""
	muta toate obiectele dintr-o locatie in alta
	param. old_loc: locatia obiectelor de mutat
	param. new_loc: noua locatie
	return: lista dupa mutarea tuturor obiectele dintr-o locatie in alta
	"""
	for obiect in lst:
		if get_locatie(obiect) == old_loc:
			obiect["locatie"] = new_loc
	return lst


def concatenare_str(obiect, str):
	"""
	concateneaza un string la descrierea unui obiect
	param. obiect: obiectul
	param. str: stringul
	return: obiectul dupa concatenarea stringului la descriere
	"""
	obiect["descriere"] = get_descriere(obiect) + str
	return obiect


def pret_max_fiecare_locatie(lst):
	"""
	determina cel mai mare pret pentru fiecare locatie
	param. lst: lista de obiecte
	return: un dictionar in care cheile sunt locatiile si valorile sunt pretul maxim pentru ficare lcatie
	"""
	rezultat = {}
	for obiect in lst:
		pret = get_pret_achizitie(obiect)
		locatie = get_locatie(obiect)
		if locatie in rezultat:
			if pret > rezultat[locatie]:
				rezultat[locatie] = pret
		else:
			rezultat[locatie] = pret
	return rezultat


def ordonare_cresc_dupa_pret(lst):
	"""
	ordoneaza crescator o lista de obiecte in functie de pretul de achizitie
	param. lst: lista de obiecte
	return: lista ordonata crescator
	"""
	return sorted(lst, key = get_pret_achizitie)


def suma_fiecare_locatie(lst):
	"""
	afiseaza suma prețurilor pentru fiecare locație
	param. lst: lista de obiecte
	return: un dictionar in care cheile sunt locatiile si valorile sunt sumele preturilor pentru ficare lcatie
	"""
	rezultat = {}
	for obiect in lst:
		pret = get_pret_achizitie(obiect)
		locatie = get_locatie(obiect)
		if locatie in rezultat:
			rezultat[locatie] += pret
		else:
			rezultat[locatie] = pret
	return rezultat
