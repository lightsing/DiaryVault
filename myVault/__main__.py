from . import config
from . crypto import cryptoRSA
from . import editor
from . import menu

if __name__ == '__main__':
    print("------------My Vault v%s------------\n" % config.version)
    editor = editor.Editor()
    menu = menu.Menu(
        ('New File','Load File','New KeyPair','Exit'),
        (editor.new_file,
         editor.load_file,
         cryptoRSA.generate,
         exit))
    while True:
        menu.display()

