from Crypto.Cipher import AES
from Crypto import Random


BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[:-ord(s[len(s)-1:])]


def encrypt(key, raw):
    raw = pad(raw)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(raw)


def decrypt(key, enc):
    iv = enc[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc[16:]))
