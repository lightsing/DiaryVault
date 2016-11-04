from pathlib import Path

from Crypto.PublicKey import RSA

import config
from crypto import password


def new(bits):
    new_key = RSA.generate(bits, e=65537)
    return new_key


def write(new_key, passphrase):
    public_key = new_key.publickey().exportKey()
    with open('pubkey.pem', 'wb') as pub_key_file:
        pub_key_file.write(public_key)
    private_key = new_key.exportKey(passphrase=passphrase)
    input("Please insert a removable driver.\nPress enter to continue.")
    path = Path(config.mount_point)
    while True:
        driver_name = input("Please enter the name of the removable driver:")
        location = path / driver_name
        if location.is_dir():
            break
        else:
            input("Invalid driver name.\nPress enter to continue.")
    with Path.open(location / 'seckey.pem', 'wb') as sec_key_file:
        sec_key_file.write(private_key)
    return driver_name


def read(name,passphrase = None):
    with open(name, 'rb') as key_file:
        key_bin = key_file.read()
    return RSA.importKey(key_bin,passphrase=passphrase)


def generate():
    print("\n--------------RSA Generate--------------\n")
    print("Warning: this will cover the old RSA key pair.(if exists)")
    while True:
        try:
            bits = input("RSA bits length (1024, 2048, 4096; leave blank for 2048 as default):")
            if bits:
                bits = int(bits)
            else:
                bits = 2048
            assert(bits in (1024, 2048, 4096))
            break
        except:
            print("Invalid bit length.")
    passphrase = password.get("Please enter a passphrase for private key:")
    print("Generating RSA Key Pair.")
    driver_name = write(new(bits=bits),passphrase=passphrase)
    print("\n----------FINISH RSA Generate----------\n")
    return bits, driver_name
