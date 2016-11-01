import sys
import ctypes
import getpass
import myVault.crypto.cryptoRSA as RSA
import myVault.crypto.cryptoAES as AES
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
            try:
                self.__key = RSA.read(pubkey_name)
            except:
                print('Could not load public key.\nFile damaged or does not exist.')
                exit(-1)
        else:
            passphrase = getpass.getpass('RSA Passphrase:')
            try:
                self.__key = RSA.read(seckey_name, passphrase = passphrase)
            except:
                print('Could not load public key.\nWrong passphrase or File damaged or does not exist.')
                exit(-1)
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
