import myVault.config
import myVault.editor
import myVault.menu
import myVault.crypto.cryptoRSA



if __name__ == '__main__':
    print("------------My Vault v%s------------\n" % myVault.config.version)
    editor = myVault.editor.Editor()
    menu = myVault.menu.Menu(
        ('New File','Load File','New KeyPair','Exit'),
        (editor.new_file,
         editor.load_file,
         myVault.crypto.cryptoRSA.generate,
         exit))
    while True:
        menu.display()
