if __name__ == '__main__':
    pass

def several_zeros():
    """
    Renvoie une liste de 10 zéros.
    """
    return [0] * 10

def several_zeros_custom(nb_zeros=10):
    """
    Renvoie une liste de nb_zeros zéros.
    La valeur par défaut est 10 pour correspondre au comportement de several_zeros().
    
    Args:
        nb_zeros (int): Nombre de zéros à générer
    
    Returns:
        list: Une liste contenant le nombre spécifié de zéros
    """
    return [0] * nb_zeros

def matrix(rows, cols):
    """
    Crée une matrice (liste de listes) remplie de zéros.
    
    Args:
        rows (int): Nombre de lignes de la matrice
        cols (int): Nombre de colonnes de la matrice
    
    Returns:
        list: Une matrice représentée comme une liste de listes, remplie de zéros
    """
    return [[0 for _ in range(cols)] for _ in range(rows)]

if __name__ == '__main__':
    # Test de several_zeros
    print("Test de several_zeros():")
    print(several_zeros())
    
    # Test de several_zeros_custom
    print("\nTest de several_zeros_custom():")
    print(several_zeros_custom(10))
    print(several_zeros_custom())
    
    # Test de matrix
    print("\nTest de matrix():")
    result = matrix(2, 3)
    print(result)
    print(result[2][3])
    print(result[1][2])
    print(result[0])