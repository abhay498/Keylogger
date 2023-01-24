from cryptography.fernet import Fernet
import os

def decrypt_file(key, in_filename, out_filename=None):
    """ Decrypts a file using AES (CBC mode) with the
        given key.

        key:
            The encryption key - a bytes of length 32

        in_filename:
            Name of the input file

        out_filename:
            If None, '<in_filename>.dec' will be used.

    """
    if not out_filename:
        out_filename = in_filename + '.dec'

    cipher = Fernet(key)

    with open(in_filename, 'rb') as infile:
        data = infile.read()
        
    decrypted_data = cipher.decrypt(data)

    with open(out_filename, 'wb') as outfile:
        outfile.write(decrypted_data)

key = b'sSnWxAz72kqlgLWA6NrmwLHF4Nys9NImBkMR6KpRrLg='
decrypt_file(key, 'log.txt.enc')

