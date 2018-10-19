import random

def testFerma(a,n):
    print(a, n, (a**(n-1)) % n)
    if ((a**(n-1)) % n == 1):
        return True
    else:
        return False

def is_prime(n):
    """
    Tests to see if a number is prime.
    >>> is_prime(2)
    True
    >>> is_prime(11)
    True
    >>> is_prime(8)
    False
    """
    isPrime = True
    lala = 1
    for i in range(0,100):
        while True:
            lala = random.randint(1,1000000000000)
            if lala % n != 0:
                break
        if testFerma(lala,n):
            continue
        else:
            isPrime = False
            break
    return isPrime


def gcd(a, b):
    """
    Euclid's algorithm for determining the greatest common divisor.
    >>> gcd(12, 15)
    3
    >>> gcd(3, 7)
    1
    """
    if a == b:
        return a
    elif a == 0:
        return b
    else:
        return gcd(b%a, a)


def multiplicative_inverse(e, phi):
    """
    Euclid's extended algorithm for finding the multiplicative
    inverse of two numbers.
    >>> multiplicative_inverse(7, 40)
    23
    """
    arr = [[],[],[],[],[],[]]
    b = e
    a = phi
    counter = 0
    while(a%b != 0):
        arr[0].append(a)
        arr[1].append(b)
        arr[2].append(a%b)
        arr[3].append(a//b)
        arr[4].append(0)
        arr[5].append(0)
        counter += 1
        c = a % b
        a = b
        b = c
    else:
        arr[0].append(a)
        arr[1].append(b)
        arr[2].append(a%b)
        arr[3].append(a//b)
        arr[4].append(0)
        arr[5].append(1)
        counter -= 1
    lala = counter + 2
    while counter >= 0:
        arr[4][counter] = arr[5][counter+1]
        arr[5][counter] = arr[4][counter+1] - arr[4][counter]*(arr[3][counter])
        counter -= 1
    for i in range(lala):
        for j in range(6):
            print(arr[j][i], end=' ')
        print('')
    return (arr[5][0]+phi)%phi


def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')

    n = pq
    # PUT YOUR CODE HERE

    phi = (p-1)(q-1)
    # PUT YOUR CODE HERE

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    # Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e, phi)
    while g != 1 and is_prime(e):
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)

    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))


def encrypt(pk, plaintext):
    # Unpack the key into it's components
    key, n = pk
    # Convert each letter in the plaintext to numbers based on
    # the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    # Return the array of bytes
    return cipher


def decrypt(pk, ciphertext):
    # Unpack the key into its components
    key, n = pk
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((char ** key) % n) for char in ciphertext]
    # Return the array of bytes as a string
    return ''.join(plain)


if __name__ == '__main__':
    print("RSA Encrypter/ Decrypter")
    p = int(input("Enter a prime number (17, 19, 23, etc): "))
    q = int(input("Enter another prime number (Not one you entered above): "))
    print("Generating your public/private keypairs now . . .")
    public, private = generate_keypair(p, q)
    print("Your public key is ", public, " and your private key is ", private)
    message = input("Enter a message to encrypt with your private key: ")
    encrypted_msg = encrypt(private, message)
    print("Your encrypted message is: ")
    print(''.join(map(lambda x: str(x), encrypted_msg)))
    print("Decrypting message with public key ", public, " . . .")
    print("Your message is:")
    print(decrypt(public, encrypted_msg))