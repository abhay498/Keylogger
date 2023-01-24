#C:\Users\Ankur>pip3 install cryptography

from cryptography.fernet import Fernet
import os

def encrypt_file(key, in_filename, out_filename=None):
    """ Encrypts a file using AES (CBC mode) with the
        given key.

        key:
            The encryption key - a bytes of length 32

        in_filename:
            Name of the input file

        out_filename:
            If None, '<in_filename>.enc' will be used.

    """
    if not out_filename:
        out_filename = in_filename + '.enc'

    cipher = Fernet(key)

    with open(in_filename, 'rb') as infile:
        data = infile.read()
        
    encrypted_data = cipher.encrypt(data)

    with open(out_filename, 'wb') as outfile:
        outfile.write(encrypted_data)

key = Fernet.generate_key()
print(key)
encrypt_file(key, 'log.txt')
