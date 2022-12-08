from television import *


# Starts up the program.
def main():
    app = QApplication([])
    window = Television()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
