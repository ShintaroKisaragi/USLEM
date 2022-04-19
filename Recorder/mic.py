# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

liste=['C1', 'Db1', 'D1', 'Eb1', 'E1', 'F1', 'Gb1', 'G1', 'Ab1', 'A1', 'Bb1', 'B1', 'C2', 'Db2', 'D2', 'Eb2', 'E2', 'F2', 'Gb2', 'G2', 'Ab2', 'A2', 'Bb2', 'B2', 'C3', 'Db3', 'D3', 'Eb3', 'E3', 'F3', 'Gb3', 'G3', 'Ab3', 'A3', 'Bb3', 'B3', 'C4', 'Db4', 'D4', 'Eb4', 'E4', 'F4', 'Gb4', 'G4', 'Ab4', 'A4', 'Bb4', 'B4', 'C5', 'Db5', 'D5', 'Eb5', 'E5', 'F5', 'Gb5', 'G5', 'Ab5', 'A5', 'Bb5', 'B5', 'C6', 'Db6', 'D6', 'Eb6', 'E6', 'F6', 'Gb6', 'G6', 'Ab6', 'A6', 'Bb6', 'B6', 'C7', 'Db7', 'D7', 'Eb7', 'E7', 'F7', 'Gb7', 'G7', 'Ab7', 'A7', 'Bb7', 'B7']




from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import*
import sys
from datetime import *
import os
from random import *
import simpleaudio as sa

import os.path
import sounddevice as sd
from scipy.io.wavfile import write
from time import*
import time





############################################################# Main #################################################################################
"""----------------------------------------------------------------------------------------------------------------------------------------------"""
####################################################################################################################################################

def textchanged(text):
    global filename
    filename = text
    

    
    

def save():
    global name
    global name2
    name=filename       #fonction d'enregistrement du fichier. Le nom du fichier est dans la variable "filename" définie avec la fonction juste au dessus
    i=1
    cn=1
    
    while cn==1:
        path="midi/"+name+".mid"
        path2="audio/"+name+".wav"
        if os.path.isfile(path) or os.path.isfile(path2):
            name=filename+"("+str(i)+")"
            i=i+1
        else:
            cn=0
            
filename="Nom de l'enregistrement"
save()


class Ui_MainWindow(QMainWindow):

        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(891, 685)
        MainWindow.setMinimumSize(QtCore.QSize(400, 150))
        MainWindow.setMaximumSize(QtCore.QSize(400, 150))
        MainWindow.setBaseSize(QtCore.QSize(1280, 720))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("sound.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(54, 57, 63);")
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setWindowTitle("Mic")

               
        

        self.enregistrer = QtWidgets.QPushButton(self.centralwidget)
        self.enregistrer.setGeometry(QtCore.QRect(10, 35, 75, 23))
        self.enregistrer.setStyleSheet("background-color: rgb(0, 185, 0);")
        self.enregistrer.setText("Enregistrer")
        self.enregistrer.clicked.connect(save)          #précise la fonction d'enregistrement à appeler. Peut être remplacé par une autre fonction

 
            
        self.choix3 = QtWidgets.QComboBox(self.centralwidget)
        self.choix3.setGeometry(QtCore.QRect(160, 80, 80, 20))
        self.choix3.setStyleSheet("background-color: rgb(255, 127, 0);")
        
        for i in range(1,86401):
            self.choix3.addItem(str(i))
           


  

                
                

        
    




        def rec33():
            self.rec2.setStyleSheet("background-color: rgb(0, 185, 0);")



        def rec3(a,seconds):
            
            fs = 44100  # this is the frequency sampling; also: 4999, 64000
 
            seconds=int(seconds)
            myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)


            print("Starting: Speak now!")
            
            
            sd.wait()  # Wait until recording is finished
            
            print("finished")
            
            

            
            b='audio/'
            c='.wav'
            d=b+a+c
          
            write(d, fs, myrecording)  # Save as WAV file
            self.rec2.setStyleSheet("background-color: rgb(255, 0, 0);")
            
        def selection4(self):
            save()
            z=(self.choix3.currentText())
            rec3(name,z)
            
        self.rec2 = QtWidgets.QPushButton(self.centralwidget)
        self.rec2.setGeometry(QtCore.QRect(10, 60, 120, 60))
        self.rec2.setStyleSheet("background-color: rgb(0, 185, 0);")
        self.rec2.setText("Exporter en Audio\n ou \n Enregistrer Micro")
        self.rec2.clicked.connect(lambda:selection4(self)) 

   

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.textChanged.connect(textchanged)
        self.lineEdit.setGeometry(QtCore.QRect(90, 35, 300, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 127, 0);")
        self.lineEdit.setText("Nom de l'enregistrement")

        self.refresh = QtWidgets.QPushButton(self.centralwidget)
        self.refresh.setGeometry(QtCore.QRect (250, 80, 80, 20))
        self.refresh.setStyleSheet("background-color: rgb(0, 185, 0);")
        self.refresh.setText("Rafraîchir")
        self.refresh.clicked.connect(lambda:rec33())          #précise la fonction d'enregistrement à appeler. Peut être remplacé par une autre fonction



        
        

       
            

        


        


        MainWindow.setCentralWidget(self.centralwidget)
        
        

        
        


        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


