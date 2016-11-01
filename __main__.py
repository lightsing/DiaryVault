from util.editor import Editor
from util.menu import Menu
from util.crypto import cryptoRSA


if __name__ == '__main__':
    print("-------------My Vault v0.1-------------\n")
    editor = Editor()
    menu = Menu(
        ('New File','Load File','New KeyPair','Exit'),
        (editor.new_file,
         editor.load_file,
         cryptoRSA.generate,
         exit))
    while True:
        menu.display()
