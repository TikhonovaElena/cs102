
def encrypt_caesar(plaintext):
    """
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ''
    for char in plaintext:
        if  65 <= ord(char) <= 90:
            ciphertext += chr((ord(char)+3-65)%26+65)
        elif 97 <= ord(char) <= 122:
            ciphertext += chr((ord(char)+3-97)%26+97)
        else:
            ciphertext += char

    return ciphertext


def decrypt_caesar(ciphertext):
    """
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ''
    for char in ciphertext:
        if 65 <= ord(char) <= 90:
            plaintext += chr((ord(char)-3-65+26)%26+65)
        elif 97 <= ord(char) <= 122:
            plaintext += chr((ord(char)-3-97+26)%26+97)
        else:
            plaintext += char
    return plaintext

