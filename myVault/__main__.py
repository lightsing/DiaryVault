import myVault.editor.Editor as Editor
import myVault.menu.Menu as Menu
import myVault.crypto.cryptoRSA as RSA


if __name__ == '__main__':
    print("-------------My Vault v0.1-------------\n")
    editor = Editor()
    menu = Menu(
        ('New File','Load File','New KeyPair','Exit'),
        (editor.new_file,
         editor.load_file,
         RSA.generate,
         exit))
    while True:
        menu.display()
