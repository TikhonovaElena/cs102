
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
        if  65 <= ord(char) <= 90:
            ciphertext += chr((ord(char)+shift-65)%26+65)
        elif 97 <= ord(char) <= 122:
            ciphertext += chr((ord(char)+shift-97)%26+97)
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
        if 65 <= ord(char) <= 90:
            plaintext += chr((ord(char)-shift-65+26)%26+65)
        elif 97 <= ord(char) <= 122:
            plaintext += chr((ord(char)-shift-97+26)%26+97)
        else:
            plaintext += char
    return plaintext

