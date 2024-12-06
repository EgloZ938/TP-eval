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

def my_sort(my_list: [int]) -> [int]:
    """
    Implémentation du tri à bulles.
    Renvoie une nouvelle liste triée sans modifier la liste d'origine.
    
    Args:
        my_list (list[int]): Liste d'entiers à trier
    
    Returns:
        list[int]: Nouvelle liste triée par ordre croissant
    """
    result = my_list.copy()
    n = len(result)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if result[j] > result[j+1]:
                result[j], result[j+1] = result[j+1], result[j]
    
    return result

class Matrix:
    """
    Classe représentant une matrice de zéros.
    """
    def __init__(self, rows: int, cols: int):
        """
        Initialise une matrice de dimensions rows x cols remplie de zéros.
        
        Args:
            rows (int): Nombre de lignes
            cols (int): Nombre de colonnes
        """
        self.__data = [[0 for _ in range(cols)] for _ in range(rows)]

    def get_value(self, row: int, col: int) -> int:
        """
        Récupère la valeur à la position spécifiée.
        
        Args:
            row (int): Index de la ligne
            col (int): Index de la colonne
            
        Returns:
            int: Valeur à la position [row][col]
        """
        return self.__data[row][col]

    def __eq__(self, other) -> bool:
        """
        Compare deux matrices.
        Renvoie True si les matrices ont les mêmes dimensions et les mêmes valeurs.
        
        Args:
            other (Matrix): Autre matrice à comparer
            
        Returns:
            bool: True si les matrices sont égales, False sinon
        """
        if not isinstance(other, Matrix):
            return False
        return self.__data == other.__data

if __name__ == '__main__':
    # Tests des fonctions précédentes
    print("Test de several_zeros():")
    print(several_zeros())
    
    print("\nTest de several_zeros_custom():")
    print(several_zeros_custom(5))
    print(several_zeros_custom())
    
    print("\nTest de matrix():")
    result = matrix(2, 3)
    print(result)
    
    # Test de my_sort
    print("\nTest de my_sort():")
    test_list = [2, 6, 1, 9, 3]
    print(f"Liste originale: {test_list}")
    print(f"Liste triée: {my_sort(test_list)}")
    print(f"Liste originale après tri: {test_list}")
    
    # Test de la classe Matrix
    print("\nTest de la classe Matrix:")
    m1 = Matrix(2, 3)
    m2 = Matrix(2, 3)
    print(f"Test égalité de matrices: {m1 == m2}")
    print(f"Valeur en position (1,1): {m1.get_value(1, 1)}")