import tempfile, os
from subprocess import call

from util.crypto.hybirdCrypto import HybirdCrypto

class Editor(object):
    def __init__(self,
                 sys_editor="nano",
                 init_message= "Let's save your diary in vault."):
        self.__editor = os.environ.get('EDITOR', sys_editor)
        self.__initMessage = init_message

    def __new_msg(self):
        with tempfile.NamedTemporaryFile(mode='w+') as temp:
            temp.write(self.__initMessage)
            temp.flush()
            call([self.__editor, temp.name])
            temp.seek(0)
            return temp.read()

    @staticmethod
    def __save(file_name, data):
        with open(file_name, mode='w+b') as writer:
            writer.write(data)

    def load_file(self):
        file_name = input('Load File Name:')
        hybirdCrypto = HybirdCrypto(init_mode='read')
        with open(file_name, mode='rb') as reader:
            raw = reader.read()
            data = hybirdCrypto.decrypt(raw)
            with tempfile.NamedTemporaryFile(mode='w+b') as temp:
                temp.write(data)
                temp.flush()
                call([self.__editor, temp.name])

    def new_file(self):
        writeEncrypt = HybirdCrypto()
        self.__save(input('New File Name:'),
                    writeEncrypt.encrypt(self.__new_msg()))

