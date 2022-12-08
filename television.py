from PyQt5.QtWidgets import *
from view import *



QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Television(QMainWindow, Ui_MainWindow):
    MIN_VOLUME = 0
    MAX_VOLUME = 25
    MIN_CHANNEL = 1
    MAX_CHANNEL = 13



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        # button functions
        self.power_Button.clicked.connect(lambda: self.power())
        self.mute_button.clicked.connect(lambda: self.mute())
        self.voldown_button.clicked.connect(lambda: self.volume_down())
        self.volup_button.clicked.connect(lambda: self.volume_up())
        self.chandown_button.clicked.connect(lambda: self.channel_down())
        self.chanup_button.clicked.connect(lambda: self.channel_up())

        # Starting Values
        self.__status = False
        self.__muted = True
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    #Power Button Function
    def power(self):
        self.__status = not self.__status
        self.screen()


    def mute(self):
        self.__muted = not self.__muted
        self.screen()

    #changes the channel variable to go up
    def channel_up(self):
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL
        self.screen()

    # changes the channel variable to go down
    def channel_down(self):
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL
        self.screen()

    def volume_up(self):
        self.__muted = True
        if self.__status and self.__volume < Television.MAX_VOLUME:
            self.__volume += 1
        self.screen()

    def volume_down(self):
        self.__muted = True
        if self.__status and self.__volume > Television.MIN_VOLUME:
            self.__volume -= 1
        self.screen()
#Updates GUI
    def screen(self):

        if self.__status:

            self.tv_output.setPixmap(QtGui.QPixmap(f"TV_Images/tv{self.__channel}.jpg"))
            if self.__muted:
                self.volume_output.setText(f'{self.__volume}/{Television.MAX_VOLUME}')
                self.volume_output.setStyleSheet("font-weight:bold; color:white")

                self.mute_output.setPixmap(QtGui.QPixmap("Computer_Science_icons/volume_on.jpeg"))
            else:
                self.volume_output.setText(f'{self.__volume}/{Television.MAX_VOLUME}')
                self.volume_output.setStyleSheet("font-weight:bold; color:white")

                self.mute_output.setPixmap(QtGui.QPixmap("Computer_Science_icons/volume_mute.jpg"))
        else:
            self.tv_output.setPixmap(QtGui.QPixmap("Computer_Science_icons/Very_Black_screen.jpg"))
            self.mute_output.setPixmap(QtGui.QPixmap("Computer_Science_icons/Very_Black_screen.jpg"))
            self.volume_output.setText('')

