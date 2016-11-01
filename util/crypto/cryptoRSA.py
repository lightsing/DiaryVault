from Crypto.PublicKey import RSA
from util.crypto import password

def new(bits=2048):
    new_key = RSA.generate(bits, e=65537)
    return new_key


def write(new_key, passphrase):
    public_key = new_key.publickey().exportKey()
    with open('pubkey.pem', 'wb') as pub_key_file:
        pub_key_file.write(public_key)
    private_key = new_key.exportKey(passphrase=passphrase)
    with open('seckey.pem', 'wb') as sec_key_file:
        sec_key_file.write(private_key)


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
    write(new(bits=bits),passphrase=passphrase)
    print("\n----------FINISH RSA Generate----------\n")
