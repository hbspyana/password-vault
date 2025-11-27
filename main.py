from db import init_db
from gui import PassVaultGUI

def main():
    init_db()
    gui = PassVaultGUI()
    gui.run()

if __name__ == '__main__':
    main()
