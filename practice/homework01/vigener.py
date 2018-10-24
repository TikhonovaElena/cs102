def encrypt_vigenere(plaintext, keyword):
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ''
    pos = 0
    for char in plaintext:
        if ord('a') <= ord(char) <= ord('z'):
            ciphertext += chr(
                (ord(char) + (ord(keyword[pos % len(keyword)])) - ord('a')) %
                26 + ord('a'))
        elif ord('A') <= ord(char) <= ord('Z'):
            ciphertext += chr(
                (ord(char) + (ord(keyword[pos % len(keyword)])) - ord('A')) %
                26 + ord('A'))
        else:
            ciphertext += char
        pos += 1
    return ciphertext


def decrypt_vigenere(ciphertext, keyword):
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ''
    pos = 0
    for char in ciphertext:
        if ord('a') <= ord(char) <= ord('z'):
            plaintext += chr(
                (ord(char) - (
                    ord(keyword[pos % len(keyword)])) +
                    26 - ord('a')) %
                26 + ord('a'))
        elif ord('A') <= ord(char) <= ord('Z'):
            plaintext += chr(
                (ord(char) - (
                    ord(keyword[pos % len(keyword)])) +
                    26 - ord('A')) %
                26 + ord('A'))
        else:
            plaintext += char
        pos += 1
    return plaintext
