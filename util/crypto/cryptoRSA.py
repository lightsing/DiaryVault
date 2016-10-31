from Crypto.PublicKey import RSA

def generate(bits=2048):
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

