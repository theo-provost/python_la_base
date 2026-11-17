from data_utils import *


def somme_cumulee(liste):
    """Compute the cumulative sum of a list.

    Parameters: liste (list of numbers)
    Returns: a list, e.g. [1, 2, 3, 4] -> [1, 3, 6, 10]
    """
    resultat = []
    total = 0
    for elt in liste:
        total += elt
        resultat.append(total)
    return resultat


def compter_occurrences(liste):
    """Count how many times each element appears in a list.

    Parameters: liste (list)
    Returns: a dictionary {element: number of occurrences}
    """
    occurrences = {}
    for elt in liste:
        occurrences[elt] = occurrences.get(elt, 0) + 1
    return occurrences


def inverser_dict(dictionnaire):
    """Swap the keys and the values of a dictionary.

    Parameters: dictionnaire (dict), the values must be hashable
    Returns: a new dictionary {value: key}
    """
    return {valeur: cle for cle, valeur in dictionnaire.items()}


def filtrer_pairs(liste):
    """Keep only the even numbers of a list.

    Parameters: liste (list of int)
    Returns: a new list with the even numbers
    """
    return [x for x in liste if x % 2 == 0]


def celsius_to_fahrenheit(celsius):
    """Convert a temperature from Celsius to Fahrenheit (F = C * 9/5 + 32).

    Parameters: celsius (int or float)
    Returns: the temperature in Fahrenheit (float)
    """
    return celsius * 9 / 5 + 32


def trouver_doublons(liste):
    """Find the elements that appear more than once in a list.

    Parameters: liste (list)
    Returns: a list of the duplicated elements (each one only once)
    """
    doublons = []
    for elt, nb in compter_occurrences(liste).items():
        if nb > 1:
            doublons.append(elt)
    return doublons


def calculer_moyenne_ponderee(valeurs, poids):
    """Compute the weighted mean of a list of values.

    Parameters: valeurs (list of numbers), poids (list of numbers, same length)
    Returns: sum(valeur * poids) / sum(poids) (float)
    """
    somme = 0
    for v, p in zip(valeurs, poids):
        somme += v * p
    return somme / sum(poids)
