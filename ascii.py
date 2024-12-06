def decrypt(message: [int]) -> str:
    """
    Déchiffre une liste de codes ASCII en texte.
    
    Args:
        message (list[int]): Liste des codes ASCII
    
    Returns:
        str: Le texte déchiffré
    """
    return ''.join(chr(code) for code in message)

if __name__ == '__main__':
    message_code = [84, 104, 105, 115, 32, 101, 120, 101, 114, 99, 105, 99, 101, 32, 105, 115, 32, 97, 119, 101, 115, 111, 109, 101, 32, 33]
    
    message_decode = decrypt(message_code)
    print(f"Message déchiffré: {message_decode}")