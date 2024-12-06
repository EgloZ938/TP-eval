class Disk:
    """
    Classe représentant un disque de stockage avec son espace total et utilisé.
    """
    def __init__(self, total: int, used: int):
        """
        Initialise un disque avec son espace total et utilisé.

        Args:
            total (int): Espace total du disque en Go
            used (int): Espace utilisé du disque en Go
        """
        self.total = total
        self.used = used

    @property
    def free(self) -> int:
        """
        Calcule l'espace libre sur le disque.
        
        Returns:
            int: Espace libre en Go
        """
        return self.total - self.used

    @property
    def used_perc(self) -> float:
        """
        Calcule le pourcentage d'espace utilisé.
        
        Returns:
            float: Ratio d'utilisation (entre 0 et 1)
        """
        return self.used / self.total

    def __str__(self) -> str:
        """
        Formate l'affichage du disque.
        
        Returns:
            str: Représentation du disque sous forme de chaîne
        """
        return f"Disk[total: {self.total} Gb, used: {self.used} Gb]"

    def __lt__(self, other) -> bool:
        """
        Compare deux disques selon leur pourcentage d'utilisation.
        Utilisé par sorted() pour le tri.
        
        Args:
            other (Disk): Autre disque à comparer
            
        Returns:
            bool: True si self a un pourcentage d'utilisation plus faible
        """
        return self.used_perc < other.used_perc

if __name__ == '__main__':
    # Tests des fonctionnalités
    disk1 = Disk(total=10, used=2)
    disk2 = Disk(total=20, used=5)

    # Test des propriétés
    print(f"Disk1 free space: {disk1.free}")  # Devrait afficher 8
    print(f"Disk2 free space: {disk2.free}")  # Devrait afficher 15
    print(f"Disk1 used percentage: {disk1.used_perc}")  # Devrait afficher 0.2
    print(f"Disk2 used percentage: {disk2.used_perc}")  # Devrait afficher 0.25

    # Test de l'affichage
    print(disk1)  # Devrait afficher "Disk[total: 10 Gb, used: 2 Gb]"

    # Test du tri
    disks = [disk2, disk1]  # Non trié
    disks_sorted = sorted(disks)  # Trié selon le pourcentage d'utilisation
    print("\nDisques triés par pourcentage d'utilisation:")
    for disk in disks_sorted:
        print(f"{disk} (used: {disk.used_perc*100}%)")