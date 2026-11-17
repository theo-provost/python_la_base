PI = 3.141592653589793
E = 2.718281828459045


def carre(x):
    """Return the square of x.

    Parameters: x (int or float)
    Returns: x * x
    """
    return x * x


def cube(x):
    """Return the cube of x.

    Parameters: x (int or float)
    Returns: x * x * x
    """
    return x * x * x


def factorielle(n):
    """Compute the factorial of a positive integer.

    Parameters: n (int), must be >= 0
    Returns: n! (int)
    """
    resultat = 1
    for i in range(2, n + 1):
        resultat *= i
    return resultat


def valeur_absolue(x):
    """Return the absolute value of x.

    Parameters: x (int or float)
    Returns: x if x >= 0, otherwise -x
    """
    if x < 0:
        return -x
    return x


def maximum(liste):
    """Return the biggest element of a list.

    Parameters: liste (list of numbers)
    Returns: the maximum value
    """
    max_val = liste[0]
    for elt in liste:
        if elt > max_val:
            max_val = elt
    return max_val


def minimum(liste):
    """Return the smallest element of a list.

    Parameters: liste (list of numbers)
    Returns: the minimum value
    """
    min_val = liste[0]
    for elt in liste:
        if elt < min_val:
            min_val = elt
    return min_val


def moyenne(liste):
    """Return the mean of a list of numbers.

    Parameters: liste (list of numbers)
    Returns: sum of the elements divided by their number (float)
    """
    return sum(liste) / len(liste)


def ecart_type(liste):
    """Return the (population) standard deviation of a list of numbers.

    Parameters: liste (list of numbers)
    Returns: the standard deviation (float)
    """
    m = moyenne(liste)
    variance = sum((x - m) ** 2 for x in liste) / len(liste)
    return variance ** 0.5


def mediane(liste):
    """Return the median of a list of numbers.

    Parameters: liste (list of numbers)
    Returns: the middle value (or the mean of the two middle values)
    """
    triee = sorted(liste)
    n = len(triee)
    milieu = n // 2
    if n % 2 == 1:
        return triee[milieu]
    return (triee[milieu - 1] + triee[milieu]) / 2
