from television import *

def main():
    app = QApplication([])
    window = Television()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()