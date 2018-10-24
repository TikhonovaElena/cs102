
def encrypt_caesar(plaintext, shift):
    """
    >>> encrypt_caesar("PYTHON,3")
    'SBWKRQ'
    >>> encrypt_caesar("python, 3")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6, 3")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ''
    for char in plaintext:
        if ord('a') <= ord(char) <= ord('z'):
            ciphertext += chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
        elif ord('A') <= ord(char) <= ord('Z'):
            ciphertext += chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
        else:
            ciphertext += char

    return ciphertext


def decrypt_caesar(ciphertext, shift):
    """
    >>> decrypt_caesar("SBWKRQ, 3")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq, 3")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6, 3")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ''
    for char in ciphertext:
        if ord('a') <= ord(char) <= ord('z'):
            plaintext += chr((ord(char)-shift - ord('a') + 26) % 26 + ord('a'))
        elif ord('A') <= ord(char) <= ord('Z'):
            plaintext += chr((ord(char)-shift - ord('A') + 26) % 26 + ord('A'))
        else:
            plaintext += char
    return plaintext
