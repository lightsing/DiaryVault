import sys
import ctypes
import getpass
import util.crypto.cryptoRSA as RSA
import util.crypto.cryptoAES as AES
from Crypto.Cipher import PKCS1_v1_5 as RSA_chiper
from Crypto import Random

def wipe_object(obj):
    return ctypes.memset(id(obj), 0, sys.getsizeof(obj))


class HybirdCrypto(object):
    def __init__(self,
                 pubkey_name = 'pubkey.pem',
                 seckey_name = 'seckey.pem',
                 init_mode = 'write'):
        if init_mode == 'write' :
            self.__key = RSA.read(pubkey_name)
        else:
            passphrase = getpass.getpass('RSA Passphrase:')
            self.__key = RSA.read(seckey_name, passphrase = passphrase)
            wipe_object(passphrase)
            del passphrase
        self.__cipher = RSA_chiper.new(self.__key)

    def encrypt(self, data):
        aes_key = Random.new().read(32)
        enc_data = AES.encrypt(aes_key, data)
        aes_key = self.__cipher.encrypt(aes_key)
        return aes_key + enc_data

    def decrypt(self, data):
        aes_key = self.__cipher.decrypt(data[:256],Random.new().read)
        return AES.decrypt(aes_key, data[256:])
