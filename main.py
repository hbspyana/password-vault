from src.db import init_db
from src.gui import PassVaultGUI

def main():
    init_db()
    gui = PassVaultGUI()
    gui.run()

if __name__ == '__main__':
    main()
