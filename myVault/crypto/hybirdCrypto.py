import sys, ctypes, getpass
from pathlib import Path

from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5 as RSA_chiper

import myVault.config
import myVault.crypto.cryptoRSA as RSA
import myVault.crypto.cryptoAES as AES


def wipe_object(obj):
    return ctypes.memset(id(obj), 0, sys.getsizeof(obj))


class HybirdCrypto(object):
    def __init__(self,
                 length,
                 driver_name,
                 pubkey_name='pubkey.pem',
                 seckey_name='seckey.pem',
                 init_mode='write'):
        if init_mode == 'write':
            try:
                self.__key = RSA.read(pubkey_name)
            except:
                print('Could not load public key.\nFile damaged or does not exist.')
                exit(-1)
        else:
            path = Path(myVault.config.mount_point) / driver_name / seckey_name
            passphrase = getpass.getpass('RSA Passphrase:')
            try:
                self.__key = RSA.read(str(path), passphrase = passphrase)
            except:
                print('Could not load public key.\nWrong passphrase or File damaged or does not exist.')
                exit(-1)
            wipe_object(passphrase)
            del passphrase
        self._length = length // 8
        self._cipher = RSA_chiper.new(self.__key)

    def encrypt(self, data):
        aes_key = Random.new().read(32)
        enc_data = AES.encrypt(aes_key, data)
        aes_key = self._cipher.encrypt(aes_key)
        return aes_key + enc_data

    def decrypt(self, data):
        aes_key = self._cipher.decrypt(data[:self._length], Random.new().read)
        return AES.decrypt(aes_key, data[self._length:])
