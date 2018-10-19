def encrypt_vigenere(plaintext, keyword):
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    # PUT YOUR CODE HERE
    ciphertext = ''
    pos = 0
    for char in plaintext:
        if 65 <= ord(char) <= 90:
            ciphertext += chr((ord(char)+(ord(keyword[pos%len(keyword)]))-65)%26+65)
        elif 97 <= ord(char) <= 122:
            ciphertext += chr((ord(char)+(ord(keyword[pos%len(keyword)]))-97)%26+97)
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
    # PUT YOUR CODE HERE
    plaintext = ''
    pos = 0
    for char in ciphertext:
        if 65 <= ord(char) <= 90:
            plaintext += chr((ord(char)-(ord(keyword[pos%len(keyword)]))+26-65)%26+65)
        elif 97 <= ord(char) <= 122:
            plaintext += chr((ord(char)-(ord(keyword[pos%len(keyword)]))+26-97)%26+97)
        else:
            plaintext += char
        pos += 1
    return plaintext