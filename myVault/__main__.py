from myVault.editor import Editor
from myVault.menu import Menu
from myVault.crypto import cryptoRSA


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
