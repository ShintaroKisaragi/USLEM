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
from clavier import*
import pygame
from pygame.locals import *
from pygame import*
from midiutil import*
import pygame.midi
from clavier2 import*
from clavier3 import*
from clavier4 import*
import os.path
import sounddevice as sd
from scipy.io.wavfile import write
from time import*
import time



midi_port=0

instrumen="Piano"
instrument="Piano"
reco=0




    

def rec(self):
    global reco
    
    
    if reco==1:
        reco=0
        self.Clavier2.setStyleSheet("background-color: rgb(0, 185, 0);")
    elif reco==0:
        self.Clavier2.setStyleSheet("background-color: rgb(255, 0, 0);")
        reco=1
        
      
                
        


############################################################ clavier_maitre #######################################################################

try:  # Ensure set available for output example
    set
except NameError:
    from sets import Set as set




def print_device_info():
    pygame.midi.init()
    _print_device_info()
    pygame.midi.quit()


def _print_device_info():
    for i in range( pygame.midi.get_count() ):
        r = pygame.midi.get_device_info(i)
        (interf, name, input, output, opened) = r

        in_out = ""
        if input:
            in_out = "(input)"
        if output:
            in_out = "(output)"

        print ("%2i: interface :%s:, name :%s:, opened :%s:  %s" %
               (i, interf, name, opened, in_out))
        





        


 




############################################################# clavier ##############################################################################
"""----------------------------------------------------------------------------------------------------------------------------------------------"""
####################################################################################################################################################


    ################### Musique #######################


def debut():
    print("salut")
    #debut=time.time()
def fin():
    fin=time.time()
    duration=fin-debut
    



   

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
   
    
def jouerNote(note):
    wave_obj = notes[note]
    play_obj = wave_obj.play()

notes = {
    'Do1': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/C1.wav"),
    'ReMin1': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/Db1.wav"),
    'Re1': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/D1.wav"),
    'MiMin1': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/Eb1.wav"),
    'Mi1': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/E1.wav"),
    'Fa1': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/F1.wav"),
    'SolMin1': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/Gb1.wav"),
    'Sol1': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/G1.wav"),
    'LaMin1': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/Ab1.wav"),
    'La1': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/A1.wav"),
    'SiMin1': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/Bb1.wav"),
    'Si1': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/B1.wav"),
    'Do2': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/C2.wav"),
    'ReMin2': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/Db2.wav"),
    'Re2': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/D2.wav"),
    'MiMin2': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/Eb2.wav"),
    'Mi2': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/E2.wav"),
    'Fa2': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/F2.wav"),
    'SolMin2': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/Gb2.wav"),
    'Sol2': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/G2.wav"),
    'LaMin2': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/Ab2.wav"),
    'La2': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/A2.wav"),
    'SiMin2': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/Bb2.wav"),
    'Si2': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/B2.wav"),
    'Do3': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/C3.wav"),
    'ReMin3': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/Db3.wav"),
    'Re3': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/D3.wav"),
    'MiMin3': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/Eb3.wav"),
    'Mi3': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/E3.wav"),
    'Fa3': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/F3.wav"),
    'SolMin3': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/Gb3.wav"),
    'Sol3': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/G3.wav"),
    'LaMin3': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/Ab3.wav"),
    'La3': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/A3.wav"),
    'SiMin3': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/Bb3.wav"),
    'Si3': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/B3.wav"),
    'Do4': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/C4.wav"),
    'ReMin4': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/Db4.wav"),
    'Re4': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/D4.wav"),
    'MiMin4': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/Eb4.wav"),
    'Mi4': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/E4.wav"),
    'Fa4': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/F4.wav"),
    'SolMin4': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/Gb4.wav"),
    'Sol4': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/G4.wav"),
    'LaMin4': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/Ab4.wav"),
    'La4': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/A4.wav"),
    'SiMin4': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/Bb4.wav"),
    'Si4': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/B4.wav"),
    'Do5': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/C5.wav"),
    'ReMin5': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/Db5.wav"),
    'Re5': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/D5.wav"),
    'MiMin5': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/Eb5.wav"),
    'Mi5': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/E5.wav"),
    'Fa5': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/F5.wav"),
    'SolMin5': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/Gb5.wav"),
    'Sol5': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/G5.wav"),
    'LaMin5': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/Ab5.wav"),
    'La5': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/A5.wav"),
    'SiMin5': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/Bb5.wav"),
    'Si5': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/B5.wav"),
    'Do6': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/C6.wav"),
    'ReMin6': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/Db6.wav"),
    'Re6': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/D6.wav"),
    'MiMin6': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/Eb6.wav"),
    'Mi6': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/E6.wav"),
    'Fa6': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/F6.wav"),
    'SolMin6': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/Gb6.wav"),
    'Sol6': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/G6.wav"),
    'LaMin6': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/Ab6.wav"),
    'La6': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/A6.wav"),
    'SiMin6': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/Bb6.wav"),
    'Si6': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/B6.wav"),
    'Do7': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/C7.wav"),
    'ReMin7': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/Db7.wav"),
    'Re7': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/D7.wav"),
    'MiMin7': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/Eb7.wav"),
    'Mi7': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/E7.wav"),
    'Fa7': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/F7.wav"),
    'SolMin7': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/Gb7.wav"),
    'Sol7': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/G7.wav"),
    'LaMin7': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/Ab7.wav"),
    'La7': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/A7.wav"),
    'SiMin7': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/Bb7.wav"),
    'Si7': sa.WaveObject.from_wave_file("sounds/"+instrumen+"/B7.wav"),

    }

class Ui_MainWindow(QMainWindow):

        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(891, 685)
        MainWindow.setMinimumSize(QtCore.QSize(891, 685))
        MainWindow.setMaximumSize(QtCore.QSize(891, 685))
        MainWindow.setBaseSize(QtCore.QSize(1280, 720))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("zinc.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(54, 57, 63);")
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

               
        self.Sol1 = QtWidgets.QPushButton(self.centralwidget)
        self.Sol1.setGeometry(QtCore.QRect(130, 10, 31, 281))
        self.Sol1.setMinimumSize(QtCore.QSize(0, 281))
        self.Sol1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Sol1.setText("")
        self.Sol1.setAutoRepeat(False)
        self.Sol1.setObjectName("Sol1")
        self.Sol1.clicked.connect(self.SonSol1)
        
        self.La1 = QtWidgets.QPushButton(self.centralwidget)
        self.La1.setGeometry(QtCore.QRect(160, 10, 31, 281))
        self.La1.setMinimumSize(QtCore.QSize(0, 281))
        self.La1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.La1.setText("")
        self.La1.setAutoRepeat(False)
        self.La1.setObjectName("La1")
        self.La1.clicked.connect(self.SonLa1)
        
        self.AA_35 = QtWidgets.QLabel(self.centralwidget)
        self.AA_35.setGeometry(QtCore.QRect(70, 250, 31, 31))
        self.AA_35.setStyleSheet("background: transparent;\n"
"font: 8pt \"Times New Roman\";")
        self.AA_35.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AA_35.setLineWidth(0)
        self.AA_35.setAlignment(QtCore.Qt.AlignCenter)
        self.AA_35.setObjectName("AA_35")
        self.AA_36 = QtWidgets.QLabel(self.centralwidget)
        self.AA_36.setGeometry(QtCore.QRect(100, 250, 31, 31))
        self.AA_36.setStyleSheet("background: transparent;\n"
"font: 8pt \"Times New Roman\";")
        self.AA_36.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AA_36.setLineWidth(0)
        self.AA_36.setAlignment(QtCore.Qt.AlignCenter)
        self.AA_36.setObjectName("AA_36")
        
        self.Do1 = QtWidgets.QPushButton(self.centralwidget)
        self.Do1.setGeometry(QtCore.QRect(10, 10, 31, 281))
        self.Do1.setMinimumSize(QtCore.QSize(0, 281))
        self.Do1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Do1.setText("")
        self.Do1.setAutoRepeat(False)
        self.Do1.setObjectName("Do1")
        self.Do1.clicked.connect(self.SonDo1)

        self.enregistrer = QtWidgets.QPushButton(self.centralwidget)
        self.enregistrer.setGeometry(QtCore.QRect(10, 585, 75, 23))
        self.enregistrer.setStyleSheet("background-color: rgb(0, 185, 0);")
        self.enregistrer.setText("Enregistrer")
        self.enregistrer.clicked.connect(save)          #précise la fonction d'enregistrement à appeler. Peut être remplacé par une autre fonction

        def selection(self):
            global instrument
            instrument=(self.choix.currentText())
            
            
        def selection2(self):
            global midi_port
            midi_port=(self.choix2.currentText())
            midi_port=int(midi_port[1])
            
            
        self.choix = QtWidgets.QComboBox(self.centralwidget)
        self.choix.setGeometry(QtCore.QRect(2, 300, 110, 23))
        self.choix.setStyleSheet("background-color: rgb(255, 127, 0);")
        fic=open("sounds/Instruments.txt","r")
        for ligne in fic:
            a=len(ligne)
            instru=""
            for i in range(0,a-1):
                instru=instru+ligne[i]
            self.choix.addItem(instru)
            
        
           


        def _print_device_info2():
            midi_detect=0
            self.choix2.addItem(" 0-Choix de Clavier MIDI, Cliquer pour développer")
            for i in range( pygame.midi.get_count() ):
                r = pygame.midi.get_device_info(i)
                (interf, name, input, output, opened) = r

                in_out = ""
                if input:
                    in_out = "(input)"
                    self.choix2.addItem("%2i: interface :%s:, name :%s:, opened :%s:  %s" %
                       (i, interf, name, opened, in_out))
                    midi_detect=1
                if output:
                    in_out = "(output)"
            

                
                

        self.choix2 = QtWidgets.QComboBox(self.centralwidget)
        self.choix2.setGeometry(QtCore.QRect(90,610, 791, 20))
        self.choix2.setStyleSheet("background-color: rgb(255, 127, 0);")
        
        
        
        pygame.midi.init()
        _print_device_info2()
        pygame.midi.quit()


        

        


        self.valider = QtWidgets.QPushButton(self.centralwidget)
        self.valider.setGeometry(QtCore.QRect(10, 340, 75, 23))
        self.valider.setStyleSheet("background-color: rgb(0, 185, 0);")
        self.valider.setText("Valider")
        self.valider.clicked.connect(lambda:selection(self))

        self.rec1 = QtWidgets.QPushButton(self.centralwidget)
        self.rec1.setGeometry(QtCore.QRect(10, 400, 75, 23))
        self.rec1.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.rec1.setText("Midi Record")
        self.rec1.clicked.connect(lambda:rec(self))

        
 
        
        self.valider2 = QtWidgets.QPushButton(self.centralwidget)
        self.valider2.setGeometry(QtCore.QRect(10, 610, 75, 23))
        self.valider2.setStyleSheet("background-color: rgb(0, 185, 0);")
        self.valider2.setText("Valider")
        self.valider2.clicked.connect(lambda:selection2(self)) 

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.textChanged.connect(textchanged)
        self.lineEdit.setGeometry(QtCore.QRect(90, 585, 791, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 127, 0);")
        self.lineEdit.setText("Nom de l'enregistrement")

        
        self.AA = QtWidgets.QLabel(self.centralwidget)
        self.AA.setGeometry(QtCore.QRect(160, 250, 31, 31))
        self.AA.setStyleSheet("background: transparent;\n"
"font: 8pt \"Times New Roman\";")
        self.AA.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AA.setLineWidth(0)
        self.AA.setAlignment(QtCore.Qt.AlignCenter)
        self.AA.setObjectName("AA")
        
        self.Si1 = QtWidgets.QPushButton(self.centralwidget)
        self.Si1.setGeometry(QtCore.QRect(190, 10, 31, 281))
        self.Si1.setMinimumSize(QtCore.QSize(0, 281))
        self.Si1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Si1.setText("")
        self.Si1.setAutoRepeat(False)
        self.Si1.setObjectName("Si1")
        self.Si1.clicked.connect(self.SonSi1)
        
        self.Re1 = QtWidgets.QPushButton(self.centralwidget)
        self.Re1.setGeometry(QtCore.QRect(40, 10, 31, 281))
        self.Re1.setMinimumSize(QtCore.QSize(0, 281))
        self.Re1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Re1.setText("")
        self.Re1.setAutoRepeat(False)
        self.Re1.setObjectName("Re1")
        self.Re1.clicked.connect(self.SonRe1)
        
        self.Mi1 = QtWidgets.QPushButton(self.centralwidget)
        self.Mi1.setGeometry(QtCore.QRect(70, 10, 31, 281))
        self.Mi1.setMinimumSize(QtCore.QSize(0, 281))
        self.Mi1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Mi1.setText("")
        self.Mi1.setAutoRepeat(False)
        self.Mi1.setObjectName("Mi1")
        self.Mi1.clicked.connect(self.SonMi1)
        
        self.Fa1 = QtWidgets.QPushButton(self.centralwidget)
        self.Fa1.setGeometry(QtCore.QRect(100, 10, 31, 281))
        self.Fa1.setMinimumSize(QtCore.QSize(0, 281))
        self.Fa1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Fa1.setText("")
        self.Fa1.setAutoRepeat(False)
        self.Fa1.setObjectName("Fa1")
        self.Fa1.clicked.connect(self.SonFa1)

        def piano2():
            pygame.init()
            pygame.midi.init()

            #Ouverture de la fenêtre Pygame
            fenetre = pygame.display.set_mode((640, 480))
            pygame.display.set_caption("ZINC")
            pygame.display.set_icon(pygame.image.load("zinc.png"))

            #Chargement et collage du fond
            fond = pygame.image.load("piano.jpg").convert()
            fenetre.blit(fond, (0,0))

            #Rafraîchissement de l'écran
            pygame.display.flip()
            son_music2(midi_port,instrument)
            pygame.quit()
            return 0

        def piano():
            pygame.init()

            #Ouverture de la fenêtre Pygame
            fenetre = pygame.display.set_mode((640, 480))
            pygame.display.set_caption("ZINC")
            pygame.display.set_icon(pygame.image.load("zinc.png"))

            #Chargement et collage du fond
            fond = pygame.image.load("piano.jpg").convert()
            fenetre.blit(fond, (0,0))

            #Rafraîchissement de l'écran
            pygame.display.flip()
            
            c=time.time()
            son_music(c,2,instrument,name)
            pygame.quit()
            return 0

        def piano3():
            pygame.init()

            #Ouverture de la fenêtre Pygame
            fenetre = pygame.display.set_mode((640, 480))
            pygame.display.set_caption("ZINC")
            pygame.display.set_icon(pygame.image.load("zinc.png"))

            #Chargement et collage du fond
            fond = pygame.image.load("piano.jpg").convert()
            fenetre.blit(fond, (0,0))

            #Rafraîchissement de l'écran
            pygame.display.flip()
            
            son_music3(2,instrument)
            pygame.quit()
            return 0
            
            
   
        def piano6():
            pygame.init()

            #Ouverture de la fenêtre Pygame
            fenetre = pygame.display.set_mode((640, 480))
            pygame.display.set_caption("ZINC")
            pygame.display.set_icon(pygame.image.load("zinc.png"))

            #Chargement et collage du fond
            fond = pygame.image.load("piano.jpg").convert()
            fenetre.blit(fond, (0,0))

            #Rafraîchissement de l'écran
            pygame.display.flip()
            c=time.time()
            son_music6(c,midi_port,instrument,name)
            pygame.quit()
            return 0

        def piano4():
            if midi_port==0:
                piano3()
            
            else:
                piano2()
                
        def piano5():
            if midi_port==0:
                piano()
            else:
                piano6()
                
        def rec_select():
            save()
            if reco==1:
                piano5()
            else:
                piano4()
            

        


        self.Clavier2 = QtWidgets.QPushButton(self.centralwidget)
        self.Clavier2.setGeometry(QtCore.QRect(780, 350, 101, 61))
        self.Clavier2.setMinimumSize(QtCore.QSize(0, 0))
        self.Clavier2.setStyleSheet("background-color: rgb(0, 185, 0);")
        self.Clavier2.setText("Passer en mode \n clavier")
        self.Clavier2.setAutoRepeat(False)
        self.Clavier2.clicked.connect(lambda:rec_select())
    


        

        def partition():
            os.system("taskkill /im MidiSheetMusic-2.6.exe /f")
            os.startfile("partition.mid")
            

        self.partition = QtWidgets.QPushButton(self.centralwidget)
        self.partition.setGeometry(QtCore.QRect(780, 470, 100, 61))
        self.partition.setMinimumSize(QtCore.QSize(0, 0))
        self.partition.setStyleSheet("background-color: rgb(255, 127, 0);")
        self.partition.setText("Voir partition")
        self.partition.setAutoRepeat(False)
        self.partition.clicked.connect(lambda:partition())
        
        self.AA_5 = QtWidgets.QLabel(self.centralwidget)
        self.AA_5.setGeometry(QtCore.QRect(130, 250, 31, 31))
        self.AA_5.setStyleSheet("background: transparent;\n"
"font: 8pt \"Times New Roman\";")
        self.AA_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AA_5.setLineWidth(0)
        self.AA_5.setAlignment(QtCore.Qt.AlignCenter)
        self.AA_5.setObjectName("AA_5")
        self.AA_6 = QtWidgets.QLabel(self.centralwidget)
        self.AA_6.setGeometry(QtCore.QRect(190, 250, 31, 31))
        self.AA_6.setStyleSheet("background: transparent;\n"
"font: 8pt \"Times New Roman\";")
        self.AA_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AA_6.setLineWidth(0)
        self.AA_6.setAlignment(QtCore.Qt.AlignCenter)
        self.AA_6.setObjectName("AA_6")
        self.AA_7 = QtWidgets.QLabel(self.centralwidget)
        self.AA_7.setGeometry(QtCore.QRect(10, 250, 31, 31))
        self.AA_7.setStyleSheet("background: transparent;\n"
"font: 8pt \"Times New Roman\";")
        self.AA_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AA_7.setLineWidth(0)
        self.AA_7.setAlignment(QtCore.Qt.AlignCenter)
        self.AA_7.setObjectName("AA_7")
        self.AA_8 = QtWidgets.QLabel(self.centralwidget)
        self.AA_8.setGeometry(QtCore.QRect(40, 250, 31, 31))
        self.AA_8.setStyleSheet("background: transparent;\n"
"font: 8pt \"Times New Roman\";")
        self.AA_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AA_8.setLineWidth(0)
        self.AA_8.setAlignment(QtCore.Qt.AlignCenter)
        self.AA_8.setObjectName("AA_8")
        self.AA_9 = QtWidgets.QLabel(self.centralwidget)
        self.AA_9.setGeometry(QtCore.QRect(380, 250, 31, 31))
        self.AA_9.setStyleSheet("background: transparent;\n"
"font: 8pt \"Times New Roman\";")
        self.AA_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AA_9.setLineWidth(0)
        self.AA_9.setAlignment(QtCore.Qt.AlignCenter)
        self.AA_9.setObjectName("AA_9")
        self.AA_10 = QtWidgets.QLabel(self.centralwidget)
        self.AA_10.setGeometry(QtCore.QRect(350, 250, 31, 31))
        self.AA_10.setStyleSheet("background: transparent;\n"
"font: 8pt \"Times New Roman\";")
        self.AA_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AA_10.setLineWidth(0)
        self.AA_10.setAlignment(QtCore.Qt.AlignCenter)
        self.AA_10.setObjectName("AA_10")
        
        self.Sol2 = QtWidgets.QPushButton(self.centralwidget)
        self.Sol2.setGeometry(QtCore.QRect(350, 10, 31, 281))
        self.Sol2.setMinimumSize(QtCore.QSize(0, 281))
        self.Sol2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Sol2.setText("")
        self.Sol2.setAutoRepeat(False)
        self.Sol2.setObjectName("Sol2")
        self.Sol2.clicked.connect(self.SonSol2)
        
        self.Re2 = QtWidgets.QPushButton(self.centralwidget)
        self.Re2.setGeometry(QtCore.QRect(260, 10, 31, 281))
        self.Re2.setMinimumSize(QtCore.QSize(0, 281))
        self.Re2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Re2.setText("")
        self.Re2.setAutoRepeat(False)
        self.Re2.setObjectName("Re2")
        self.Re2.clicked.connect(self.SonRe2)
        
        self.Si2 = QtWidgets.QPushButton(self.centralwidget)
        self.Si2.setGeometry(QtCore.QRect(410, 10, 31, 281))
        self.Si2.setMinimumSize(QtCore.QSize(0, 281))
        self.Si2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Si2.setText("")
        self.Si2.setAutoRepeat(False)
        self.Si2.setObjectName("Si2")
        self.Si2.clicked.connect(self.SonSi2)
        
        self.Mi2 = QtWidgets.QPushButton(self.centralwidget)
        self.Mi2.setGeometry(QtCore.QRect(290, 10, 31, 281))
        self.Mi2.setMinimumSize(QtCore.QSize(0, 281))
        self.Mi2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Mi2.setText("")
        self.Mi2.setAutoRepeat(False)
        self.Mi2.setObjectName("Mi2")
        self.Mi2.clicked.connect(self.SonMi2)
        
        self.AA_11 = QtWidgets.QLabel(self.centralwidget)
        self.AA_11.setGeometry(QtCore.QRect(290, 250, 31, 31))
        self.AA_11.setStyleSheet("background: transparent;\n"
"font: 8pt \"Times New Roman\";")
        self.AA_11.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AA_11.setLineWidth(0)
        self.AA_11.setAlignment(QtCore.Qt.AlignCenter)
        self.AA_11.setObjectName("AA_11")
        self.AA_12 = QtWidgets.QLabel(self.centralwidget)
        self.AA_12.setGeometry(QtCore.QRect(410, 250, 31, 31))
        self.AA_12.setStyleSheet("background: transparent;\n"
"font: 8pt \"Times New Roman\";")
        self.AA_12.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AA_12.setLineWidth(0)
        self.AA_12.setAlignment(QtCore.Qt.AlignCenter)
        self.AA_12.setObjectName("AA_12")
        self.AA_13 = QtWidgets.QLabel(self.centralwidget)
        self.AA_13.setGeometry(QtCore.QRect(320, 250, 31, 31))
        self.AA_13.setStyleSheet("background: transparent;\n"
"font: 8pt \"Times New Roman\";")
        self.AA_13.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AA_13.setLineWidth(0)
        self.AA_13.setAlignment(QtCore.Qt.AlignCenter)
        self.AA_13.setObjectName("AA_13")
        
        self.La2 = QtWidgets.QPushButton(self.centralwidget)
        self.La2.setGeometry(QtCore.QRect(380, 10, 31, 281))
        self.La2.setMinimumSize(QtCore.QSize(0, 281))
        self.La2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.La2.setText("")
        self.La2.setAutoRepeat(False)
        self.La2.setObjectName("La2")
        self.La2.clicked.connect(self.SonLa2)
        
        self.Fa2 = QtWidgets.QPushButton(self.centralwidget)
        self.Fa2.setGeometry(QtCore.QRect(320, 10, 31, 281))
        self.Fa2.setMinimumSize(QtCore.QSize(0, 281))
        self.Fa2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Fa2.setText("")
        self.Fa2.setAutoRepeat(False)
        self.Fa2.setObjectName("Fa2")
        self.Fa2.clicked.connect(self.SonFa2)
        
        self.Do2 = QtWidgets.QPushButton(self.centralwidget)
        self.Do2.setGeometry(QtCore.QRect(230, 10, 31, 281))
        self.Do2.setMinimumSize(QtCore.QSize(0, 281))
        self.Do2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Do2.setText("")
        self.Do2.setAutoRepeat(False)
        self.Do2.setObjectName("Do2")
        self.Do2.clicked.connect(self.SonDo2)
        
        self.AA_14 = QtWidgets.QLabel(self.centralwidget)
        self.AA_14.setGeometry(QtCore.QRect(230, 250, 31, 31))
        self.AA_14.setStyleSheet("background: transparent;\n"
"font: 8pt \"Times New Roman\";")
        self.AA_14.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AA_14.setLineWidth(0)
        self.AA_14.setAlignment(QtCore.Qt.AlignCenter)
        self.AA_14.setObjectName("AA_14")
        self.AA_16 = QtWidgets.QLabel(self.centralwidget)
        self.AA_16.setGeometry(QtCore.QRect(260, 250, 31, 31))
        self.AA_16.setStyleSheet("background: transparent;\n"
"font: 8pt \"Times New Roman\";")
        self.AA_16.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AA_16.setLineWidth(0)
        self.AA_16.setAlignment(QtCore.Qt.AlignCenter)
        self.AA_16.setObjectName("AA_16")
        self.AA_17 = QtWidgets.QLabel(self.centralwidget)
        self.AA_17.setGeometry(QtCore.QRect(540, 250, 31, 31))
        self.AA_17.setStyleSheet("background: transparent;\n"
"font: 8pt \"Times New Roman\";")
        self.AA_17.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AA_17.setLineWidth(0)
        self.AA_17.setAlignment(QtCore.Qt.AlignCenter)
        self.AA_17.setObjectName("AA_17")
        
        self.Re3 = QtWidgets.QPushButton(self.centralwidget)
        self.Re3.setGeometry(QtCore.QRect(480, 10, 31, 281))
        self.Re3.setMinimumSize(QtCore.QSize(0, 281))
        self.Re3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Re3.setText("")
        self.Re3.setAutoRepeat(False)
        self.Re3.setObjectName("Re3")
        self.Re3.clicked.connect(self.SonRe3)
        
        self.AA_18 = QtWidgets.QLabel(self.centralwidget)
        self.AA_18.setGeometry(QtCore.QRect(480, 250, 31, 31))
        self.AA_18.setStyleSheet("background: transparent;\n"
"font: 8pt \"Times New Roman\";")
        self.AA_18.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AA_18.setLineWidth(0)
        self.AA_18.setAlignment(QtCore.Qt.AlignCenter)
        self.AA_18.setObjectName("AA_18")
        
        self.Si3 = QtWidgets.QPushButton(self.centralwidget)
        self.Si3.setGeometry(QtCore.QRect(630, 10, 31, 281))
        self.Si3.setMinimumSize(QtCore.QSize(0, 281))
        self.Si3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Si3.setText("")
        self.Si3.setAutoRepeat(False)
        self.Si3.setObjectName("Si3")
        self.Si3.clicked.connect(self.SonSi3)
        
        self.AA_19 = QtWidgets.QLabel(self.centralwidget)
        self.AA_19.setGeometry(QtCore.QRect(510, 250, 31, 31))
        self.AA_19.setStyleSheet("background: transparent;\n"
"font: 8pt \"Times New Roman\";")
        self.AA_19.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AA_19.setLineWidth(0)
        self.AA_19.setAlignment(QtCore.Qt.AlignCenter)
        self.AA_19.setObjectName("AA_19")
        
        self.Fa3 = QtWidgets.QPushButton(self.centralwidget)
        self.Fa3.setGeometry(QtCore.QRect(540, 10, 31, 281))
        self.Fa3.setMinimumSize(QtCore.QSize(0, 281))
        self.Fa3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Fa3.setText("")
        self.Fa3.setAutoRepeat(False)
        self.Fa3.setObjectName("Fa3")
        self.Fa3.clicked.connect(self.SonFa3)
        
        self.La3 = QtWidgets.QPushButton(self.centralwidget)
        self.La3.setGeometry(QtCore.QRect(600, 10, 31, 281))
        self.La3.setMinimumSize(QtCore.QSize(0, 281))
        self.La3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.La3.setText("")
        self.La3.setAutoRepeat(False)
        self.La3.setObjectName("La3")
        self.La3.clicked.connect(self.SonLa3)
        
        self.AA_20 = QtWidgets.QLabel(self.centralwidget)
        self.AA_20.setGeometry(QtCore.QRect(630, 250, 31, 31))
        self.AA_20.setStyleSheet("background: transparent;\n"
"font: 8pt \"Times New Roman\";")
        self.AA_20.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AA_20.setLineWidth(0)
        self.AA_20.setAlignment(QtCore.Qt.AlignCenter)
        self.AA_20.setObjectName("AA_20")
        self.AA_21 = QtWidgets.QLabel(self.centralwidget)
        self.AA_21.setGeometry(QtCore.QRect(600, 250, 31, 31))
        self.AA_21.setStyleSheet("background: transparent;\n"
"font: 8pt \"Times New Roman\";")
        self.AA_21.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AA_21.setLineWidth(0)
        self.AA_21.setAlignment(QtCore.Qt.AlignCenter)
        self.AA_21.setObjectName("AA_21")
        self.AA_22 = QtWidgets.QLabel(self.centralwidget)
        self.AA_22.setGeometry(QtCore.QRect(450, 250, 31, 31))
        self.AA_22.setStyleSheet("background: transparent;\n"
"font: 8pt \"Times New Roman\";")
        self.AA_22.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AA_22.setLineWidth(0)
        self.AA_22.setAlignment(QtCore.Qt.AlignCenter)
        self.AA_22.setObjectName("AA_22")
        
        self.Mi3 = QtWidgets.QPushButton(self.centralwidget)
        self.Mi3.setGeometry(QtCore.QRect(510, 10, 31, 281))
        self.Mi3.setMinimumSize(QtCore.QSize(0, 281))
        self.Mi3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Mi3.setText("")
        self.Mi3.setAutoRepeat(False)
        self.Mi3.setObjectName("Mi3")
        self.Mi3.clicked.connect(self.SonMi3)
        
        self.AA_23 = QtWidgets.QLabel(self.centralwidget)
        self.AA_23.setGeometry(QtCore.QRect(570, 250, 31, 31))
        self.AA_23.setStyleSheet("background: transparent;\n"
"font: 8pt \"Times New Roman\";")
        self.AA_23.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AA_23.setLineWidth(0)
        self.AA_23.setAlignment(QtCore.Qt.AlignCenter)
        self.AA_23.setObjectName("AA_23")
        
        self.Sol3 = QtWidgets.QPushButton(self.centralwidget)
        self.Sol3.setGeometry(QtCore.QRect(570, 10, 31, 281))
        self.Sol3.setMinimumSize(QtCore.QSize(0, 281))
        self.Sol3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Sol3.setText("")
        self.Sol3.setAutoRepeat(False)
        self.Sol3.setObjectName("Sol3")
        self.Sol3.clicked.connect(self.SonSol3)
        
        self.Do3 = QtWidgets.QPushButton(self.centralwidget)
        self.Do3.setGeometry(QtCore.QRect(450, 10, 31, 281))
        self.Do3.setMinimumSize(QtCore.QSize(0, 281))
        self.Do3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Do3.setText("")
        self.Do3.setAutoRepeat(False)
        self.Do3.setObjectName("Do3")
        self.Do3.clicked.connect(self.SonDo3)
        
        self.AA_24 = QtWidgets.QLabel(self.centralwidget)
        self.AA_24.setGeometry(QtCore.QRect(730, 250, 31, 31))
        self.AA_24.setStyleSheet("background: transparent;\n"
"font: 8pt \"Times New Roman\";")
        self.AA_24.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AA_24.setLineWidth(0)
        self.AA_24.setAlignment(QtCore.Qt.AlignCenter)
        self.AA_24.setObjectName("AA_24")
        self.AA_26 = QtWidgets.QLabel(self.centralwidget)
        self.AA_26.setGeometry(QtCore.QRect(700, 250, 31, 31))
        self.AA_26.setStyleSheet("background: transparent;\n"
"font: 8pt \"Times New Roman\";")
        self.AA_26.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AA_26.setLineWidth(0)
        self.AA_26.setAlignment(QtCore.Qt.AlignCenter)
        self.AA_26.setObjectName("AA_26")
        self.AA_27 = QtWidgets.QLabel(self.centralwidget)
        self.AA_27.setGeometry(QtCore.QRect(790, 250, 31, 31))
        self.AA_27.setStyleSheet("background: transparent;\n"
"font: 8pt \"Times New Roman\";")
        self.AA_27.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AA_27.setLineWidth(0)
        self.AA_27.setAlignment(QtCore.Qt.AlignCenter)
        self.AA_27.setObjectName("AA_27")
        
        self.Re4 = QtWidgets.QPushButton(self.centralwidget)
        self.Re4.setGeometry(QtCore.QRect(700, 10, 31, 281))
        self.Re4.setMinimumSize(QtCore.QSize(0, 281))
        self.Re4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Re4.setText("")
        self.Re4.setAutoRepeat(False)
        self.Re4.setObjectName("Re4")
        self.Re4.clicked.connect(self.SonRe4)
        
        self.Fa4 = QtWidgets.QPushButton(self.centralwidget)
        self.Fa4.setGeometry(QtCore.QRect(760, 10, 31, 281))
        self.Fa4.setMinimumSize(QtCore.QSize(0, 281))
        self.Fa4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Fa4.setText("")
        self.Fa4.setAutoRepeat(False)
        self.Fa4.setObjectName("Fa4")
        self.Fa4.clicked.connect(self.SonFa4)
        
        self.AA_28 = QtWidgets.QLabel(self.centralwidget)
        self.AA_28.setGeometry(QtCore.QRect(670, 250, 31, 31))
        self.AA_28.setStyleSheet("background: transparent;\n"
"font: 8pt \"Times New Roman\";")
        self.AA_28.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AA_28.setLineWidth(0)
        self.AA_28.setAlignment(QtCore.Qt.AlignCenter)
        self.AA_28.setObjectName("AA_28")
        self.AA_29 = QtWidgets.QLabel(self.centralwidget)
        self.AA_29.setGeometry(QtCore.QRect(820, 250, 31, 31))
        self.AA_29.setStyleSheet("background: transparent;\n"
"font: 8pt \"Times New Roman\";")
        self.AA_29.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AA_29.setLineWidth(0)
        self.AA_29.setAlignment(QtCore.Qt.AlignCenter)
        self.AA_29.setObjectName("AA_29")
        
        self.Si4 = QtWidgets.QPushButton(self.centralwidget)
        self.Si4.setGeometry(QtCore.QRect(850, 10, 31, 281))
        self.Si4.setMinimumSize(QtCore.QSize(0, 281))
        self.Si4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Si4.setText("")
        self.Si4.setAutoRepeat(False)
        self.Si4.setObjectName("Si4")
        self.Si4.clicked.connect(self.SonSi4)
        
        self.Do4 = QtWidgets.QPushButton(self.centralwidget)
        self.Do4.setGeometry(QtCore.QRect(670, 10, 31, 281))
        self.Do4.setMinimumSize(QtCore.QSize(0, 281))
        self.Do4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Do4.setText("")
        self.Do4.setAutoRepeat(False)
        self.Do4.setObjectName("Do4")
        self.Do4.clicked.connect(self.SonDo4)
        
        self.AA_30 = QtWidgets.QLabel(self.centralwidget)
        self.AA_30.setGeometry(QtCore.QRect(850, 250, 31, 31))
        self.AA_30.setStyleSheet("background: transparent;\n"
"font: 8pt \"Times New Roman\";")
        self.AA_30.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AA_30.setLineWidth(0)
        self.AA_30.setAlignment(QtCore.Qt.AlignCenter)
        self.AA_30.setObjectName("AA_30")
        self.AA_33 = QtWidgets.QLabel(self.centralwidget)
        self.AA_33.setGeometry(QtCore.QRect(760, 250, 31, 31))
        self.AA_33.setStyleSheet("background: transparent;\n"
"font: 8pt \"Times New Roman\";")
        self.AA_33.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AA_33.setLineWidth(0)
        self.AA_33.setAlignment(QtCore.Qt.AlignCenter)
        self.AA_33.setObjectName("AA_33")
        
        self.La4 = QtWidgets.QPushButton(self.centralwidget)
        self.La4.setGeometry(QtCore.QRect(820, 10, 31, 281))
        self.La4.setMinimumSize(QtCore.QSize(0, 281))
        self.La4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.La4.setText("")
        self.La4.setAutoRepeat(False)
        self.La4.setObjectName("La4")
        self.La4.clicked.connect(self.SonLa4)
        
        self.Sol4 = QtWidgets.QPushButton(self.centralwidget)
        self.Sol4.setGeometry(QtCore.QRect(790, 10, 31, 281))
        self.Sol4.setMinimumSize(QtCore.QSize(0, 281))
        self.Sol4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Sol4.setText("")
        self.Sol4.setAutoRepeat(False)
        self.Sol4.setObjectName("Sol4")
        self.Sol4.clicked.connect(self.SonSol4)
        
        self.Mi4 = QtWidgets.QPushButton(self.centralwidget)
        self.Mi4.setGeometry(QtCore.QRect(730, 10, 31, 281))
        self.Mi4.setMinimumSize(QtCore.QSize(0, 281))
        self.Mi4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Mi4.setText("")
        self.Mi4.setAutoRepeat(False)
        self.Mi4.setObjectName("Mi4")
        self.Mi4.clicked.connect(self.SonMi4)
        
        self.Re1Min = QtWidgets.QPushButton(self.centralwidget)
        self.Re1Min.setGeometry(QtCore.QRect(30, 10, 21, 141))
        self.Re1Min.setMinimumSize(QtCore.QSize(0, 141))
        self.Re1Min.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.Re1Min.setText("")
        self.Re1Min.setAutoRepeat(False)
        self.Re1Min.setObjectName("Re1Min")
        self.Re1Min.clicked.connect(self.SonRe1Min)
        
        self.La1Min = QtWidgets.QPushButton(self.centralwidget)
        self.La1Min.setGeometry(QtCore.QRect(150, 10, 21, 141))
        self.La1Min.setMinimumSize(QtCore.QSize(0, 141))
        self.La1Min.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.La1Min.setText("")
        self.La1Min.setAutoRepeat(False)
        self.La1Min.setObjectName("La1Min")
        self.La1Min.clicked.connect(self.SonLa1Min)
        
        self.Mi1Min = QtWidgets.QPushButton(self.centralwidget)
        self.Mi1Min.setGeometry(QtCore.QRect(60, 10, 21, 141))
        self.Mi1Min.setMinimumSize(QtCore.QSize(0, 141))
        self.Mi1Min.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.Mi1Min.setText("")
        self.Mi1Min.setAutoRepeat(False)
        self.Mi1Min.setObjectName("Mi1Min")
        self.Mi1Min.clicked.connect(self.SonMi1Min)
        
        self.Si1Min = QtWidgets.QPushButton(self.centralwidget)
        self.Si1Min.setGeometry(QtCore.QRect(180, 10, 21, 141))
        self.Si1Min.setMinimumSize(QtCore.QSize(0, 141))
        self.Si1Min.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.Si1Min.setText("")
        self.Si1Min.setAutoRepeat(False)
        self.Si1Min.setObjectName("Si1Min")
        self.Si1Min.clicked.connect(self.SonSi1Min)
        
        self.Sol1Min = QtWidgets.QPushButton(self.centralwidget)
        self.Sol1Min.setGeometry(QtCore.QRect(120, 10, 21, 141))
        self.Sol1Min.setMinimumSize(QtCore.QSize(0, 141))
        self.Sol1Min.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.Sol1Min.setText("")
        self.Sol1Min.setAutoRepeat(False)
        self.Sol1Min.setObjectName("Sol1Min")
        self.Sol1Min.clicked.connect(self.SonSol1Min)
        
        self.Mi2Min = QtWidgets.QPushButton(self.centralwidget)
        self.Mi2Min.setGeometry(QtCore.QRect(280, 10, 21, 141))
        self.Mi2Min.setMinimumSize(QtCore.QSize(0, 141))
        self.Mi2Min.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.Mi2Min.setText("")
        self.Mi2Min.setAutoRepeat(False)
        self.Mi2Min.setObjectName("Mi2Min")
        self.Mi2Min.clicked.connect(self.SonMi2Min)
        
        self.Re2Min = QtWidgets.QPushButton(self.centralwidget)
        self.Re2Min.setGeometry(QtCore.QRect(250, 10, 21, 141))
        self.Re2Min.setMinimumSize(QtCore.QSize(0, 141))
        self.Re2Min.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.Re2Min.setText("")
        self.Re2Min.setAutoRepeat(False)
        self.Re2Min.setObjectName("Re2Min")
        self.Re2Min.clicked.connect(self.SonRe2Min)
        
        self.Sol2Min = QtWidgets.QPushButton(self.centralwidget)
        self.Sol2Min.setGeometry(QtCore.QRect(340, 10, 21, 141))
        self.Sol2Min.setMinimumSize(QtCore.QSize(0, 141))
        self.Sol2Min.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.Sol2Min.setText("")
        self.Sol2Min.setAutoRepeat(False)
        self.Sol2Min.setObjectName("Sol2Min")
        self.Sol2Min.clicked.connect(self.SonSol2Min)
        
        self.Si2Min = QtWidgets.QPushButton(self.centralwidget)
        self.Si2Min.setGeometry(QtCore.QRect(400, 10, 21, 141))
        self.Si2Min.setMinimumSize(QtCore.QSize(0, 141))
        self.Si2Min.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.Si2Min.setText("")
        self.Si2Min.setAutoRepeat(False)
        self.Si2Min.setObjectName("Si2Min")
        self.Si2Min.clicked.connect(self.SonSi2Min)
        
        self.La2Min = QtWidgets.QPushButton(self.centralwidget)
        self.La2Min.setGeometry(QtCore.QRect(370, 10, 21, 141))
        self.La2Min.setMinimumSize(QtCore.QSize(0, 141))
        self.La2Min.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.La2Min.setText("")
        self.La2Min.setAutoRepeat(False)
        self.La2Min.setObjectName("La2Min")
        self.La2Min.clicked.connect(self.SonLa2Min)
        
        self.Mi3Min = QtWidgets.QPushButton(self.centralwidget)
        self.Mi3Min.setGeometry(QtCore.QRect(500, 10, 21, 141))
        self.Mi3Min.setMinimumSize(QtCore.QSize(0, 141))
        self.Mi3Min.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.Mi3Min.setText("")
        self.Mi3Min.setAutoRepeat(False)
        self.Mi3Min.setObjectName("Mi3Min")
        self.Mi3Min.clicked.connect(self.SonMi3Min)
        
        self.La3Min = QtWidgets.QPushButton(self.centralwidget)
        self.La3Min.setGeometry(QtCore.QRect(590, 10, 21, 141))
        self.La3Min.setMinimumSize(QtCore.QSize(0, 141))
        self.La3Min.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.La3Min.setText("")
        self.La3Min.setAutoRepeat(False)
        self.La3Min.setObjectName("La3Min")
        self.La3Min.clicked.connect(self.SonLa3Min)
        
        self.Re3Min = QtWidgets.QPushButton(self.centralwidget)
        self.Re3Min.setGeometry(QtCore.QRect(470, 10, 21, 141))
        self.Re3Min.setMinimumSize(QtCore.QSize(0, 141))
        self.Re3Min.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.Re3Min.setText("")
        self.Re3Min.setAutoRepeat(False)
        self.Re3Min.setObjectName("Re3Min")
        self.Re3Min.clicked.connect(self.SonRe3Min)
        
        self.Sol3Min = QtWidgets.QPushButton(self.centralwidget)
        self.Sol3Min.setGeometry(QtCore.QRect(560, 10, 21, 141))
        self.Sol3Min.setMinimumSize(QtCore.QSize(0, 141))
        self.Sol3Min.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.Sol3Min.setText("")
        self.Sol3Min.setAutoRepeat(False)
        self.Sol3Min.setObjectName("Sol3Min")
        self.Sol3Min.clicked.connect(self.SonSol3Min)
        
        self.Si3Min = QtWidgets.QPushButton(self.centralwidget)
        self.Si3Min.setGeometry(QtCore.QRect(620, 10, 21, 141))
        self.Si3Min.setMinimumSize(QtCore.QSize(0, 141))
        self.Si3Min.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.Si3Min.setText("")
        self.Si3Min.setAutoRepeat(False)
        self.Si3Min.setObjectName("Si3Min")
        self.Si3Min.clicked.connect(self.SonSi3Min)
        
        self.Si4Min = QtWidgets.QPushButton(self.centralwidget)
        self.Si4Min.setGeometry(QtCore.QRect(840, 10, 21, 141))
        self.Si4Min.setMinimumSize(QtCore.QSize(0, 141))
        self.Si4Min.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.Si4Min.setText("")
        self.Si4Min.setAutoRepeat(False)
        self.Si4Min.setObjectName("Si4Min")
        self.Si4Min.clicked.connect(self.SonSi4Min)
        
        self.La4Min = QtWidgets.QPushButton(self.centralwidget)
        self.La4Min.setGeometry(QtCore.QRect(810, 10, 21, 141))
        self.La4Min.setMinimumSize(QtCore.QSize(0, 141))
        self.La4Min.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.La4Min.setText("")
        self.La4Min.setAutoRepeat(False)
        self.La4Min.setObjectName("La4Min")
        self.La4Min.clicked.connect(self.SonLa4Min)
        
        self.Sol4Min = QtWidgets.QPushButton(self.centralwidget)
        self.Sol4Min.setGeometry(QtCore.QRect(780, 10, 21, 141))
        self.Sol4Min.setMinimumSize(QtCore.QSize(0, 141))
        self.Sol4Min.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.Sol4Min.setText("")
        self.Sol4Min.setAutoRepeat(False)
        self.Sol4Min.setObjectName("Sol4Min")
        self.Sol4Min.clicked.connect(self.SonSol4Min)
        
        self.Re4Min = QtWidgets.QPushButton(self.centralwidget)
        self.Re4Min.setGeometry(QtCore.QRect(690, 10, 21, 141))
        self.Re4Min.setMinimumSize(QtCore.QSize(0, 141))
        self.Re4Min.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.Re4Min.setText("")
        self.Re4Min.setAutoRepeat(False)
        self.Re4Min.setObjectName("Re4Min")
        self.Re4Min.clicked.connect(self.SonRe4Min)
        
        self.Mi4Min = QtWidgets.QPushButton(self.centralwidget)
        self.Mi4Min.setGeometry(QtCore.QRect(720, 10, 21, 141))
        self.Mi4Min.setMinimumSize(QtCore.QSize(0, 141))
        self.Mi4Min.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.Mi4Min.setText("")
        self.Mi4Min.setAutoRepeat(False)
        self.Mi4Min.setObjectName("Mi4Min")
        self.Mi4Min.clicked.connect(self.SonMi4Min)
        
        self.Do5 = QtWidgets.QPushButton(self.centralwidget)
        self.Do5.setGeometry(QtCore.QRect(120, 300, 31, 281))
        self.Do5.setMinimumSize(QtCore.QSize(0, 281))
        self.Do5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Do5.setText("")
        self.Do5.setAutoRepeat(False)
        self.Do5.setObjectName("Do5")
        self.Do5.clicked.connect(self.SonDo5)
        
        self.Re5 = QtWidgets.QPushButton(self.centralwidget)
        self.Re5.setGeometry(QtCore.QRect(150, 300, 31, 281))
        self.Re5.setMinimumSize(QtCore.QSize(0, 281))
        self.Re5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Re5.setText("")
        self.Re5.setAutoRepeat(False)
        self.Re5.setObjectName("Re5")
        self.Re5.clicked.connect(self.SonRe5)
        
        self.La5 = QtWidgets.QPushButton(self.centralwidget)
        self.La5.setGeometry(QtCore.QRect(270, 300, 31, 281))
        self.La5.setMinimumSize(QtCore.QSize(0, 281))
        self.La5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.La5.setText("")
        self.La5.setAutoRepeat(False)
        self.La5.setObjectName("La5")
        self.La5.clicked.connect(self.SonLa5)
        
        self.Sol5Min = QtWidgets.QPushButton(self.centralwidget)
        self.Sol5Min.setGeometry(QtCore.QRect(230, 300, 21, 141))
        self.Sol5Min.setMinimumSize(QtCore.QSize(0, 141))
        self.Sol5Min.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.Sol5Min.setText("")
        self.Sol5Min.setAutoRepeat(False)
        self.Sol5Min.setObjectName("Sol5Min")
        self.Sol5Min.clicked.connect(self.SonSol5Min)
        
        self.Mi5 = QtWidgets.QPushButton(self.centralwidget)
        self.Mi5.setGeometry(QtCore.QRect(180, 300, 31, 281))
        self.Mi5.setMinimumSize(QtCore.QSize(0, 281))
        self.Mi5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Mi5.setText("")
        self.Mi5.setAutoRepeat(False)
        self.Mi5.setObjectName("Mi5")
        self.Mi5.clicked.connect(self.SonMi5)
        
        self.Re5Min = QtWidgets.QPushButton(self.centralwidget)
        self.Re5Min.setGeometry(QtCore.QRect(140, 300, 21, 141))
        self.Re5Min.setMinimumSize(QtCore.QSize(0, 141))
        self.Re5Min.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.Re5Min.setText("")
        self.Re5Min.setAutoRepeat(False)
        self.Re5Min.setObjectName("Re5Min")
        self.Re5Min.clicked.connect(self.SonRe5Min)
        
        self.AA_38 = QtWidgets.QLabel(self.centralwidget)
        self.AA_38.setGeometry(QtCore.QRect(120, 540, 31, 31))
        self.AA_38.setStyleSheet("background: transparent;\n"
"font: 8pt \"Times New Roman\";")
        self.AA_38.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AA_38.setLineWidth(0)
        self.AA_38.setAlignment(QtCore.Qt.AlignCenter)
        self.AA_38.setObjectName("AA_38")
        self.AA_39 = QtWidgets.QLabel(self.centralwidget)
        self.AA_39.setGeometry(QtCore.QRect(180, 540, 31, 31))
        self.AA_39.setStyleSheet("background: transparent;\n"
"font: 8pt \"Times New Roman\";")
        self.AA_39.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AA_39.setLineWidth(0)
        self.AA_39.setAlignment(QtCore.Qt.AlignCenter)
        self.AA_39.setObjectName("AA_39")
        
        self.Si5 = QtWidgets.QPushButton(self.centralwidget)
        self.Si5.setGeometry(QtCore.QRect(300, 300, 31, 281))
        self.Si5.setMinimumSize(QtCore.QSize(0, 281))
        self.Si5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Si5.setText("")
        self.Si5.setAutoRepeat(False)
        self.Si5.setObjectName("Si5")
        self.Si5.clicked.connect(self.SonSi5)
        
        self.Sol5 = QtWidgets.QPushButton(self.centralwidget)
        self.Sol5.setGeometry(QtCore.QRect(240, 300, 31, 281))
        self.Sol5.setMinimumSize(QtCore.QSize(0, 281))
        self.Sol5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Sol5.setText("")
        self.Sol5.setAutoRepeat(False)
        self.Sol5.setObjectName("Sol5")
        self.Sol5.clicked.connect(self.SonSol5)
        
        self.AA_40 = QtWidgets.QLabel(self.centralwidget)
        self.AA_40.setGeometry(QtCore.QRect(150, 540, 31, 31))
        self.AA_40.setStyleSheet("background: transparent;\n"
"font: 8pt \"Times New Roman\";")
        self.AA_40.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AA_40.setLineWidth(0)
        self.AA_40.setAlignment(QtCore.Qt.AlignCenter)
        self.AA_40.setObjectName("AA_40")
        self.AA_41 = QtWidgets.QLabel(self.centralwidget)
        self.AA_41.setGeometry(QtCore.QRect(240, 540, 31, 31))
        self.AA_41.setStyleSheet("background: transparent;\n"
"font: 8pt \"Times New Roman\";")
        self.AA_41.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AA_41.setLineWidth(0)
        self.AA_41.setAlignment(QtCore.Qt.AlignCenter)
        self.AA_41.setObjectName("AA_41")
        
        self.Fa5 = QtWidgets.QPushButton(self.centralwidget)
        self.Fa5.setGeometry(QtCore.QRect(210, 300, 31, 281))
        self.Fa5.setMinimumSize(QtCore.QSize(0, 281))
        self.Fa5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Fa5.setText("")
        self.Fa5.setAutoRepeat(False)
        self.Fa5.setObjectName("Fa5")
        self.Fa5.clicked.connect(self.SonFa5)
        
        self.La5Min = QtWidgets.QPushButton(self.centralwidget)
        self.La5Min.setGeometry(QtCore.QRect(260, 300, 21, 141))
        self.La5Min.setMinimumSize(QtCore.QSize(0, 141))
        self.La5Min.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.La5Min.setText("")
        self.La5Min.setAutoRepeat(False)
        self.La5Min.setObjectName("La5Min")
        self.La5Min.clicked.connect(self.SonLa5Min)
        
        self.AA_42 = QtWidgets.QLabel(self.centralwidget)
        self.AA_42.setGeometry(QtCore.QRect(270, 540, 31, 31))
        self.AA_42.setStyleSheet("background: transparent;\n"
"font: 8pt \"Times New Roman\";")
        self.AA_42.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AA_42.setLineWidth(0)
        self.AA_42.setAlignment(QtCore.Qt.AlignCenter)
        self.AA_42.setObjectName("AA_42")
        
        self.Si5Min = QtWidgets.QPushButton(self.centralwidget)
        self.Si5Min.setGeometry(QtCore.QRect(290, 300, 21, 141))
        self.Si5Min.setMinimumSize(QtCore.QSize(0, 141))
        self.Si5Min.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.Si5Min.setText("")
        self.Si5Min.setAutoRepeat(False)
        self.Si5Min.setObjectName("Si5Min")
        self.Si5Min.clicked.connect(self.SonSi5Min)
        
        self.AA_43 = QtWidgets.QLabel(self.centralwidget)
        self.AA_43.setGeometry(QtCore.QRect(300, 540, 31, 31))
        self.AA_43.setStyleSheet("background: transparent;\n"
"font: 8pt \"Times New Roman\";")
        self.AA_43.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AA_43.setLineWidth(0)
        self.AA_43.setAlignment(QtCore.Qt.AlignCenter)
        self.AA_43.setObjectName("AA_43")
        self.AA_44 = QtWidgets.QLabel(self.centralwidget)
        self.AA_44.setGeometry(QtCore.QRect(210, 540, 31, 31))
        self.AA_44.setStyleSheet("background: transparent;\n"
"font: 8pt \"Times New Roman\";")
        self.AA_44.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AA_44.setLineWidth(0)
        self.AA_44.setAlignment(QtCore.Qt.AlignCenter)
        self.AA_44.setObjectName("AA_44")
        
        self.Mi5Min = QtWidgets.QPushButton(self.centralwidget)
        self.Mi5Min.setGeometry(QtCore.QRect(170, 300, 21, 141))
        self.Mi5Min.setMinimumSize(QtCore.QSize(0, 141))
        self.Mi5Min.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.Mi5Min.setText("")
        self.Mi5Min.setAutoRepeat(False)
        self.Mi5Min.setObjectName("Mi5Min")
        self.Mi5Min.clicked.connect(self.SonMi5Min)
        
        self.Do6 = QtWidgets.QPushButton(self.centralwidget)
        self.Do6.setGeometry(QtCore.QRect(340, 300, 31, 281))
        self.Do6.setMinimumSize(QtCore.QSize(0, 281))
        self.Do6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Do6.setText("")
        self.Do6.setAutoRepeat(False)
        self.Do6.setObjectName("Do6")
        self.Do6.clicked.connect(self.SonDo6)
        
        self.Re6 = QtWidgets.QPushButton(self.centralwidget)
        self.Re6.setGeometry(QtCore.QRect(370, 300, 31, 281))
        self.Re6.setMinimumSize(QtCore.QSize(0, 281))
        self.Re6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Re6.setText("")
        self.Re6.setAutoRepeat(False)
        self.Re6.setObjectName("Re6")
        self.Re6.clicked.connect(self.SonRe6)
        
        self.La6 = QtWidgets.QPushButton(self.centralwidget)
        self.La6.setGeometry(QtCore.QRect(490, 300, 31, 281))
        self.La6.setMinimumSize(QtCore.QSize(0, 281))
        self.La6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.La6.setText("")
        self.La6.setAutoRepeat(False)
        self.La6.setObjectName("La6")
        self.La6.clicked.connect(self.SonLa6)
        
        self.Sol6Min = QtWidgets.QPushButton(self.centralwidget)
        self.Sol6Min.setGeometry(QtCore.QRect(450, 300, 21, 141))
        self.Sol6Min.setMinimumSize(QtCore.QSize(0, 141))
        self.Sol6Min.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.Sol6Min.setText("")
        self.Sol6Min.setAutoRepeat(False)
        self.Sol6Min.setObjectName("Sol6Min")
        self.Sol6Min.clicked.connect(self.SonSol6Min)
        
        self.Mi6 = QtWidgets.QPushButton(self.centralwidget)
        self.Mi6.setGeometry(QtCore.QRect(400, 300, 31, 281))
        self.Mi6.setMinimumSize(QtCore.QSize(0, 281))
        self.Mi6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Mi6.setText("")
        self.Mi6.setAutoRepeat(False)
        self.Mi6.setObjectName("Mi6")
        self.Mi6.clicked.connect(self.SonMi6)
        
        self.Re6Min = QtWidgets.QPushButton(self.centralwidget)
        self.Re6Min.setGeometry(QtCore.QRect(360, 300, 21, 141))
        self.Re6Min.setMinimumSize(QtCore.QSize(0, 141))
        self.Re6Min.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.Re6Min.setText("")
        self.Re6Min.setAutoRepeat(False)
        self.Re6Min.setObjectName("Re6Min")
        self.Re6Min.clicked.connect(self.SonRe6Min)
        
        self.AA_45 = QtWidgets.QLabel(self.centralwidget)
        self.AA_45.setGeometry(QtCore.QRect(340, 540, 31, 31))
        self.AA_45.setStyleSheet("background: transparent;\n"
"font: 8pt \"Times New Roman\";")
        self.AA_45.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AA_45.setLineWidth(0)
        self.AA_45.setAlignment(QtCore.Qt.AlignCenter)
        self.AA_45.setObjectName("AA_45")
        self.AA_46 = QtWidgets.QLabel(self.centralwidget)
        self.AA_46.setGeometry(QtCore.QRect(400, 540, 31, 31))
        self.AA_46.setStyleSheet("background: transparent;\n"
"font: 8pt \"Times New Roman\";")
        self.AA_46.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AA_46.setLineWidth(0)
        self.AA_46.setAlignment(QtCore.Qt.AlignCenter)
        self.AA_46.setObjectName("AA_46")
        
        self.Si6 = QtWidgets.QPushButton(self.centralwidget)
        self.Si6.setGeometry(QtCore.QRect(520, 300, 31, 281))
        self.Si6.setMinimumSize(QtCore.QSize(0, 281))
        self.Si6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Si6.setText("")
        self.Si6.setAutoRepeat(False)
        self.Si6.setObjectName("Si6")
        self.Si6.clicked.connect(self.SonSi6)
        
        self.Sol6 = QtWidgets.QPushButton(self.centralwidget)
        self.Sol6.setGeometry(QtCore.QRect(460, 300, 31, 281))
        self.Sol6.setMinimumSize(QtCore.QSize(0, 281))
        self.Sol6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Sol6.setText("")
        self.Sol6.setAutoRepeat(False)
        self.Sol6.setObjectName("Sol6")
        self.Sol6.clicked.connect(self.SonSol6)
        
        self.AA_47 = QtWidgets.QLabel(self.centralwidget)
        self.AA_47.setGeometry(QtCore.QRect(370, 540, 31, 31))
        self.AA_47.setStyleSheet("background: transparent;\n"
"font: 8pt \"Times New Roman\";")
        self.AA_47.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AA_47.setLineWidth(0)
        self.AA_47.setAlignment(QtCore.Qt.AlignCenter)
        self.AA_47.setObjectName("AA_47")
        self.AA_48 = QtWidgets.QLabel(self.centralwidget)
        self.AA_48.setGeometry(QtCore.QRect(460, 540, 31, 31))
        self.AA_48.setStyleSheet("background: transparent;\n"
"font: 8pt \"Times New Roman\";")
        self.AA_48.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AA_48.setLineWidth(0)
        self.AA_48.setAlignment(QtCore.Qt.AlignCenter)
        self.AA_48.setObjectName("AA_48")
        
        self.Fa6 = QtWidgets.QPushButton(self.centralwidget)
        self.Fa6.setGeometry(QtCore.QRect(430, 300, 31, 281))
        self.Fa6.setMinimumSize(QtCore.QSize(0, 281))
        self.Fa6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Fa6.setText("")
        self.Fa6.setAutoRepeat(False)
        self.Fa6.setObjectName("Fa6")
        self.Fa6.clicked.connect(self.SonFa6)
        
        self.La6Min = QtWidgets.QPushButton(self.centralwidget)
        self.La6Min.setGeometry(QtCore.QRect(480, 300, 21, 141))
        self.La6Min.setMinimumSize(QtCore.QSize(0, 141))
        self.La6Min.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.La6Min.setText("")
        self.La6Min.setAutoRepeat(False)
        self.La6Min.setObjectName("La6Min")
        self.La6Min.clicked.connect(self.SonLa6Min)
        
        self.AA_49 = QtWidgets.QLabel(self.centralwidget)
        self.AA_49.setGeometry(QtCore.QRect(490, 540, 31, 31))
        self.AA_49.setStyleSheet("background: transparent;\n"
"font: 8pt \"Times New Roman\";")
        self.AA_49.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AA_49.setLineWidth(0)
        self.AA_49.setAlignment(QtCore.Qt.AlignCenter)
        self.AA_49.setObjectName("AA_49")
        
        self.Si6Min = QtWidgets.QPushButton(self.centralwidget)
        self.Si6Min.setGeometry(QtCore.QRect(510, 300, 21, 141))
        self.Si6Min.setMinimumSize(QtCore.QSize(0, 141))
        self.Si6Min.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.Si6Min.setText("")
        self.Si6Min.setAutoRepeat(False)
        self.Si6Min.setObjectName("Si6Min")
        self.Si6Min.clicked.connect(self.SonSi6Min)
        
        self.AA_50 = QtWidgets.QLabel(self.centralwidget)
        self.AA_50.setGeometry(QtCore.QRect(520, 540, 31, 31))
        self.AA_50.setStyleSheet("background: transparent;\n"
"font: 8pt \"Times New Roman\";")
        self.AA_50.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AA_50.setLineWidth(0)
        self.AA_50.setAlignment(QtCore.Qt.AlignCenter)
        self.AA_50.setObjectName("AA_50")
        self.AA_51 = QtWidgets.QLabel(self.centralwidget)
        self.AA_51.setGeometry(QtCore.QRect(430, 540, 31, 31))
        self.AA_51.setStyleSheet("background: transparent;\n"
"font: 8pt \"Times New Roman\";")
        self.AA_51.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AA_51.setLineWidth(0)
        self.AA_51.setAlignment(QtCore.Qt.AlignCenter)
        self.AA_51.setObjectName("AA_51")
        
        self.Mi6Min = QtWidgets.QPushButton(self.centralwidget)
        self.Mi6Min.setGeometry(QtCore.QRect(390, 300, 21, 141))
        self.Mi6Min.setMinimumSize(QtCore.QSize(0, 141))
        self.Mi6Min.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.Mi6Min.setText("")
        self.Mi6Min.setAutoRepeat(False)
        self.Mi6Min.setObjectName("Mi6Min")
        self.Mi6Min.clicked.connect(self.SonMi6Min)
        
        self.Si7Min = QtWidgets.QPushButton(self.centralwidget)
        self.Si7Min.setGeometry(QtCore.QRect(730, 300, 21, 141))
        self.Si7Min.setMinimumSize(QtCore.QSize(0, 141))
        self.Si7Min.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.Si7Min.setText("")
        self.Si7Min.setAutoRepeat(False)
        self.Si7Min.setObjectName("Si7Min")
        self.Si7Min.clicked.connect(self.SonSi7Min)
        
        self.Re7Min = QtWidgets.QPushButton(self.centralwidget)
        self.Re7Min.setGeometry(QtCore.QRect(580, 300, 21, 141))
        self.Re7Min.setMinimumSize(QtCore.QSize(0, 141))
        self.Re7Min.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.Re7Min.setText("")
        self.Re7Min.setAutoRepeat(False)
        self.Re7Min.setObjectName("Re7Min")
        self.Re7Min.clicked.connect(self.SonRe7Min)
        
        self.Fa7 = QtWidgets.QPushButton(self.centralwidget)
        self.Fa7.setGeometry(QtCore.QRect(650, 300, 31, 281))
        self.Fa7.setMinimumSize(QtCore.QSize(0, 281))
        self.Fa7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Fa7.setText("")
        self.Fa7.setAutoRepeat(False)
        self.Fa7.setObjectName("Fa7")
        self.Fa7.clicked.connect(self.SonFa7)
        
        self.Re7 = QtWidgets.QPushButton(self.centralwidget)
        self.Re7.setGeometry(QtCore.QRect(590, 300, 31, 281))
        self.Re7.setMinimumSize(QtCore.QSize(0, 281))
        self.Re7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Re7.setText("")
        self.Re7.setAutoRepeat(False)
        self.Re7.setObjectName("Re7")
        self.Re7.clicked.connect(self.SonRe7)
        
        self.Sol7Min = QtWidgets.QPushButton(self.centralwidget)
        self.Sol7Min.setGeometry(QtCore.QRect(670, 300, 21, 141))
        self.Sol7Min.setMinimumSize(QtCore.QSize(0, 141))
        self.Sol7Min.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.Sol7Min.setText("")
        self.Sol7Min.setAutoRepeat(False)
        self.Sol7Min.setObjectName("Sol7Min")
        self.Sol7Min.clicked.connect(self.SonSol7Min)
        
        self.AA_52 = QtWidgets.QLabel(self.centralwidget)
        self.AA_52.setGeometry(QtCore.QRect(560, 540, 31, 31))
        self.AA_52.setStyleSheet("background: transparent;\n"
"font: 8pt \"Times New Roman\";")
        self.AA_52.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AA_52.setLineWidth(0)
        self.AA_52.setAlignment(QtCore.Qt.AlignCenter)
        self.AA_52.setObjectName("AA_52")
        
        self.La7 = QtWidgets.QPushButton(self.centralwidget)
        self.La7.setGeometry(QtCore.QRect(710, 300, 31, 281))
        self.La7.setMinimumSize(QtCore.QSize(0, 281))
        self.La7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.La7.setText("")
        self.La7.setAutoRepeat(False)
        self.La7.setObjectName("La7")
        self.La7.clicked.connect(self.SonLa7)
        
        self.AA_53 = QtWidgets.QLabel(self.centralwidget)
        self.AA_53.setGeometry(QtCore.QRect(710, 540, 31, 31))
        self.AA_53.setStyleSheet("background: transparent;\n"
"font: 8pt \"Times New Roman\";")
        self.AA_53.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AA_53.setLineWidth(0)
        self.AA_53.setAlignment(QtCore.Qt.AlignCenter)
        self.AA_53.setObjectName("AA_53")
        self.AA_54 = QtWidgets.QLabel(self.centralwidget)
        self.AA_54.setGeometry(QtCore.QRect(680, 540, 31, 31))
        self.AA_54.setStyleSheet("background: transparent;\n"
"font: 8pt \"Times New Roman\";")
        self.AA_54.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AA_54.setLineWidth(0)
        self.AA_54.setAlignment(QtCore.Qt.AlignCenter)
        self.AA_54.setObjectName("AA_54")
        
        self.Mi7 = QtWidgets.QPushButton(self.centralwidget)
        self.Mi7.setGeometry(QtCore.QRect(620, 300, 31, 281))
        self.Mi7.setMinimumSize(QtCore.QSize(0, 281))
        self.Mi7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Mi7.setText("")
        self.Mi7.setAutoRepeat(False)
        self.Mi7.setObjectName("Mi7")
        self.Mi7.clicked.connect(self.SonMi7)
        
        self.Sol7 = QtWidgets.QPushButton(self.centralwidget)
        self.Sol7.setGeometry(QtCore.QRect(680, 300, 31, 281))
        self.Sol7.setMinimumSize(QtCore.QSize(0, 281))
        self.Sol7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Sol7.setText("")
        self.Sol7.setAutoRepeat(False)
        self.Sol7.setObjectName("Sol7")
        self.Sol7.clicked.connect(self.SonSol7)
        
        self.AA_55 = QtWidgets.QLabel(self.centralwidget)
        self.AA_55.setGeometry(QtCore.QRect(620, 540, 31, 31))
        self.AA_55.setStyleSheet("background: transparent;\n"
"font: 8pt \"Times New Roman\";")
        self.AA_55.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AA_55.setLineWidth(0)
        self.AA_55.setAlignment(QtCore.Qt.AlignCenter)
        self.AA_55.setObjectName("AA_55")
        
        self.Mi7Min = QtWidgets.QPushButton(self.centralwidget)
        self.Mi7Min.setGeometry(QtCore.QRect(610, 300, 21, 141))
        self.Mi7Min.setMinimumSize(QtCore.QSize(0, 141))
        self.Mi7Min.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.Mi7Min.setText("")
        self.Mi7Min.setAutoRepeat(False)
        self.Mi7Min.setObjectName("Mi7Min")
        self.Mi7Min.clicked.connect(self.SonMi7Min)
        
        self.AA_56 = QtWidgets.QLabel(self.centralwidget)
        self.AA_56.setGeometry(QtCore.QRect(590, 540, 31, 31))
        self.AA_56.setStyleSheet("background: transparent;\n"
"font: 8pt \"Times New Roman\";")
        self.AA_56.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AA_56.setLineWidth(0)
        self.AA_56.setAlignment(QtCore.Qt.AlignCenter)
        self.AA_56.setObjectName("AA_56")
        
        self.Do7 = QtWidgets.QPushButton(self.centralwidget)
        self.Do7.setGeometry(QtCore.QRect(560, 300, 31, 281))
        self.Do7.setMinimumSize(QtCore.QSize(0, 281))
        self.Do7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Do7.setText("")
        self.Do7.setAutoRepeat(False)
        self.Do7.setObjectName("Do7")
        self.Do7.clicked.connect(self.SonDo7)
        
        self.Si7 = QtWidgets.QPushButton(self.centralwidget)
        self.Si7.setGeometry(QtCore.QRect(740, 300, 31, 281))
        self.Si7.setMinimumSize(QtCore.QSize(0, 281))
        self.Si7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Si7.setText("")
        self.Si7.setAutoRepeat(False)
        self.Si7.setObjectName("Si7")
        self.Si7.clicked.connect(self.SonSi7)
        
        self.La7Min = QtWidgets.QPushButton(self.centralwidget)
        self.La7Min.setGeometry(QtCore.QRect(700, 300, 21, 141))
        self.La7Min.setMinimumSize(QtCore.QSize(0, 141))
        self.La7Min.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.La7Min.setText("")
        self.La7Min.setAutoRepeat(False)
        self.La7Min.setObjectName("La7Min")
        self.La7Min.clicked.connect(self.SonLa7Min)
        
        self.AA_57 = QtWidgets.QLabel(self.centralwidget)
        self.AA_57.setGeometry(QtCore.QRect(740, 540, 31, 31))
        self.AA_57.setStyleSheet("background: transparent;\n"
"font: 8pt \"Times New Roman\";")
        self.AA_57.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AA_57.setLineWidth(0)
        self.AA_57.setAlignment(QtCore.Qt.AlignCenter)
        self.AA_57.setObjectName("AA_57")
        self.AA_58 = QtWidgets.QLabel(self.centralwidget)
        self.AA_58.setGeometry(QtCore.QRect(650, 540, 31, 31))
        self.AA_58.setStyleSheet("background: transparent;\n"
"font: 8pt \"Times New Roman\";")
        self.AA_58.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AA_58.setLineWidth(0)
        self.AA_58.setAlignment(QtCore.Qt.AlignCenter)
        self.AA_58.setObjectName("AA_58")
        
        self.Si7.raise_()
        self.La7.raise_()
        self.Sol7.raise_()
        self.Fa7.raise_()
        self.Mi7.raise_()
        self.Re7.raise_()
        self.Do7.raise_()
        self.Si6.raise_()
        self.La6.raise_()
        self.Sol6.raise_()
        self.Fa6.raise_()
        self.Mi6.raise_()
        self.Re6.raise_()
        self.Do6.raise_()
        self.Si5.raise_()
        self.La5.raise_()
        self.Sol5.raise_()
        self.Fa5.raise_()
        self.Mi5.raise_()
        self.Re5.raise_()
        self.Do5.raise_()
        self.Si4.raise_()
        self.La4.raise_()
        self.Sol4.raise_()
        self.Fa4.raise_()
        self.Mi4.raise_()
        self.Re4.raise_()
        self.Do4.raise_()
        self.Si3.raise_()
        self.La3.raise_()
        self.Sol3.raise_()
        self.Fa3.raise_()
        self.Mi3.raise_()
        self.Re3.raise_()
        self.Do3.raise_()
        self.Si2.raise_()
        self.La2.raise_()
        self.Sol2.raise_()
        self.Fa2.raise_()
        self.Mi2.raise_()
        self.Re2.raise_()
        self.Do2.raise_()
        self.Si1.raise_()
        self.La1.raise_()
        self.Sol1.raise_()
        self.Fa1.raise_()
        self.Mi1.raise_()
        self.Re1.raise_()
        self.Do1.raise_()
        self.AA_35.raise_()
        self.AA_36.raise_()
        self.AA.raise_()
        self.AA_5.raise_()
        self.AA_6.raise_()
        self.AA_7.raise_()
        self.AA_8.raise_()
        self.AA_9.raise_()
        self.AA_10.raise_()
        self.AA_11.raise_()
        self.AA_12.raise_()
        self.AA_13.raise_()
        self.AA_14.raise_()
        self.AA_16.raise_()
        self.AA_17.raise_()
        self.AA_18.raise_()
        self.AA_19.raise_()
        self.AA_20.raise_()
        self.AA_21.raise_()
        self.AA_22.raise_()
        self.AA_23.raise_()
        self.AA_24.raise_()
        self.AA_26.raise_()
        self.AA_27.raise_()
        self.AA_28.raise_()
        self.AA_29.raise_()
        self.AA_30.raise_()
        self.AA_33.raise_()
        self.Re1Min.raise_()
        self.La1Min.raise_()
        self.Mi1Min.raise_()
        self.Si1Min.raise_()
        self.Sol1Min.raise_()
        self.Mi2Min.raise_()
        self.Re2Min.raise_()
        self.Sol2Min.raise_()
        self.Si2Min.raise_()
        self.La2Min.raise_()
        self.Mi3Min.raise_()
        self.La3Min.raise_()
        self.Re3Min.raise_()
        self.Sol3Min.raise_()
        self.Si3Min.raise_()
        self.Si4Min.raise_()
        self.La4Min.raise_()
        self.Sol4Min.raise_()
        self.Re4Min.raise_()
        self.Mi4Min.raise_()
        self.Sol5Min.raise_()
        self.Re5Min.raise_()
        self.AA_38.raise_()
        self.AA_39.raise_()
        self.AA_40.raise_()
        self.AA_41.raise_()
        self.La5Min.raise_()
        self.AA_42.raise_()
        self.Si5Min.raise_()
        self.AA_43.raise_()
        self.AA_44.raise_()
        self.Mi5Min.raise_()
        self.Sol6Min.raise_()
        self.Re6Min.raise_()
        self.AA_45.raise_()
        self.AA_46.raise_()
        self.AA_47.raise_()
        self.AA_48.raise_()
        self.La6Min.raise_()
        self.AA_49.raise_()
        self.Si6Min.raise_()
        self.AA_50.raise_()
        self.AA_51.raise_()
        self.Mi6Min.raise_()
        self.Si7Min.raise_()
        self.Re7Min.raise_()
        self.Sol7Min.raise_()
        self.AA_52.raise_()
        self.AA_53.raise_()
        self.AA_54.raise_()
        self.AA_55.raise_()
        self.Mi7Min.raise_()
        self.AA_56.raise_()
        self.La7Min.raise_()
        self.AA_57.raise_()
        self.AA_58.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 891, 21))
        self.menubar.setObjectName("menubar")

        
        

        
        
        

        
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setIconSize(QtCore.QSize(18, 18))
        self.toolBar.setObjectName("toolBar")
        
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionNew_Nouveau = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icones/049-notes.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew_Nouveau.setIcon(icon1)
        self.actionNew_Nouveau.setObjectName("actionNew_Nouveau")
        
        
        
        self.actionOpen_Ouvvrir = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Icones/042-folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen_Ouvvrir.setIcon(icon2)
        self.actionOpen_Ouvvrir.setObjectName("actionOpen_Ouvvrir")
        self.actionOpen_Ouvvrir.triggered.connect(lambda:partition())
        
        
        self.actionSave_Enregistrer = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Icones/035-save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_Enregistrer.setIcon(icon3)
        self.actionSave_Enregistrer.setObjectName("actionSave_Enregistrer")
        self.actionSave_Enregistrer.triggered.connect(lambda:save())
        
        self.actionQuit_Quitter = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Icones/018-power.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit_Quitter.setIcon(icon4)
        self.actionQuit_Quitter.setObjectName("actionQuit_Quitter")
        self.actionQuit_Quitter.triggered.connect(self.exit)
        
        self.actionSettings_Param_tres = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Icones/043-settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettings_Param_tres.setIcon(icon5)
        
        self.actionSettings_Param_tres.setObjectName("actionSettings_Parametres")

        
            

        
        


        
        

                    


        
        
        
        self.toolBar.addAction(self.actionOpen_Ouvvrir)
        self.toolBar.addAction(self.actionSave_Enregistrer)
        self.toolBar.addAction(self.actionQuit_Quitter)
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ZINC"))
        self.AA_35.setText(_translate("MainWindow", "Mi"))
        self.AA_36.setText(_translate("MainWindow", "Fa"))
        self.AA.setText(_translate("MainWindow", "La"))
        self.AA_5.setText(_translate("MainWindow", "Sol"))
        self.AA_6.setText(_translate("MainWindow", "Si"))
        self.AA_7.setText(_translate("MainWindow", "Do"))
        self.AA_8.setText(_translate("MainWindow", "Ré"))
        self.AA_9.setText(_translate("MainWindow", "La"))
        self.AA_10.setText(_translate("MainWindow", "Sol"))
        self.AA_11.setText(_translate("MainWindow", "Mi"))
        self.AA_12.setText(_translate("MainWindow", "Si"))
        self.AA_13.setText(_translate("MainWindow", "Fa"))
        self.AA_14.setText(_translate("MainWindow", "Do"))
        self.AA_16.setText(_translate("MainWindow", "Ré"))
        self.AA_17.setText(_translate("MainWindow", "Fa"))
        self.AA_18.setText(_translate("MainWindow", "Ré"))
        self.AA_19.setText(_translate("MainWindow", "Mi"))
        self.AA_20.setText(_translate("MainWindow", "Si"))
        self.AA_21.setText(_translate("MainWindow", "La"))
        self.AA_22.setText(_translate("MainWindow", "Do"))
        self.AA_23.setText(_translate("MainWindow", "Sol"))
        self.AA_24.setText(_translate("MainWindow", "Mi"))
        self.AA_26.setText(_translate("MainWindow", "Ré"))
        self.AA_27.setText(_translate("MainWindow", "Sol"))
        self.AA_28.setText(_translate("MainWindow", "Do"))
        self.AA_29.setText(_translate("MainWindow", "La"))
        self.AA_30.setText(_translate("MainWindow", "Si"))
        self.AA_33.setText(_translate("MainWindow", "Fa"))
        self.AA_38.setText(_translate("MainWindow", "Do"))
        self.AA_39.setText(_translate("MainWindow", "Mi"))
        self.AA_40.setText(_translate("MainWindow", "Ré"))
        self.AA_41.setText(_translate("MainWindow", "Sol"))
        self.AA_42.setText(_translate("MainWindow", "La"))
        self.AA_43.setText(_translate("MainWindow", "Si"))
        self.AA_44.setText(_translate("MainWindow", "Fa"))
        self.AA_45.setText(_translate("MainWindow", "Do"))
        self.AA_46.setText(_translate("MainWindow", "Mi"))
        self.AA_47.setText(_translate("MainWindow", "Ré"))
        self.AA_48.setText(_translate("MainWindow", "Sol"))
        self.AA_49.setText(_translate("MainWindow", "La"))
        self.AA_50.setText(_translate("MainWindow", "Si"))
        self.AA_51.setText(_translate("MainWindow", "Fa"))
        self.AA_52.setText(_translate("MainWindow", "Do"))
        self.AA_53.setText(_translate("MainWindow", "La"))
        self.AA_54.setText(_translate("MainWindow", "Sol"))
        self.AA_55.setText(_translate("MainWindow", "Mi"))
        self.AA_56.setText(_translate("MainWindow", "Ré"))
        self.AA_57.setText(_translate("MainWindow", "Si"))
        self.AA_58.setText(_translate("MainWindow", "Fa"))

        #################################################################################################
        
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        

    def clavier (self, event):
        pass
    def exit(self, event):
        print("Extinction")
        sys.exit()
        os.exit()
        QApplication.quit()
        
    def SonDo1 (self, event):
        jouerNote('Do1')
    def SonRe1Min (self, event):
        jouerNote('ReMin1')
    def SonRe1(self, event):
        jouerNote('Re1')
    def SonMi1Min(self, event):
        jouerNote('MiMin1')
    def SonMi1(self, event):
        jouerNote('Mi1')
    def SonFa1(self, event):
        jouerNote('Fa1')
    def SonSol1Min(self, event):
        jouerNote('SolMin1')
    def SonSol1(self, event):
        jouerNote('Sol1')
    def SonLa1Min(self, event):
        jouerNote('LaMin1')
    def SonLa1(self, event):
        jouerNote('La1')
    def SonSi1Min(self, event):
        jouerNote('SiMin1')
    def SonSi1(self, event):
        jouerNote('Si1')

    def SonDo2 (self, event):
        jouerNote('Do2')
    def SonRe2Min (self, event):
        jouerNote('ReMin2')
    def SonRe2(self, event):
        jouerNote('Re2')
    def SonMi2Min(self, event):
        jouerNote('MiMin2')
    def SonMi2(self, event):
        jouerNote('Mi2')
    def SonFa2(self, event):
        jouerNote('Fa2')
    def SonSol2Min(self, event):
        jouerNote('SolMin2')
    def SonSol2(self, event):
        jouerNote('Sol2')
    def SonLa2Min(self, event):
        jouerNote('LaMin2')
    def SonLa2(self, event):
        jouerNote('La2')
    def SonSi2Min(self, event):
        jouerNote('SiMin2')
    def SonSi2(self, event):
        jouerNote('Si2')

    def SonDo3 (self, event):
        jouerNote('Do3')
    def SonRe3Min (self, event):
        jouerNote('ReMin3')
    def SonRe3(self, event):
        jouerNote('Re3')
    def SonMi3Min(self, event):
        jouerNote('MiMin3')
    def SonMi3(self, event):
        jouerNote('Mi3')
    def SonFa3(self, event):
        jouerNote('Fa3')
    def SonSol3Min(self, event):
        jouerNote('SolMin3')
    def SonSol3(self, event):
        jouerNote('Sol3')
    def SonLa3Min(self, event):
        jouerNote('LaMin3')
    def SonLa3(self, event):
        jouerNote('La3')
    def SonSi3Min(self, event):
        jouerNote('SiMin3')
    def SonSi3(self, event):
        jouerNote('Si3')

    def SonDo4 (self, event):
        jouerNote('Do4')
    def SonRe4Min (self, event):
        jouerNote('ReMin4')
    def SonRe4(self, event):
        jouerNote('Re4')
    def SonMi4Min(self, event):
        jouerNote('MiMin4')
    def SonMi4(self, event):
        jouerNote('Mi4')
    def SonFa4(self, event):
        jouerNote('Fa4')
    def SonSol4Min(self, event):
        jouerNote('SolMin4')
    def SonSol4(self, event):
        jouerNote('Sol4')
    def SonLa4Min(self, event):
        jouerNote('LaMin4')
    def SonLa4(self, event):
        jouerNote('La4')
    def SonSi4Min(self, event):
        jouerNote('SiMin4')
    def SonSi4(self, event):
        jouerNote('Si4')

    def SonDo5 (self, event):
        jouerNote('Do5')
    def SonRe5Min (self, event):
        jouerNote('ReMin5')
    def SonRe5(self, event):
        jouerNote('Re5')
    def SonMi5Min(self, event):
        jouerNote('MiMin5')
    def SonMi5(self, event):
        jouerNote('Mi5')
    def SonFa5(self, event):
        jouerNote('Fa5')
    def SonSol5Min(self, event):
        jouerNote('SolMin5')
    def SonSol5(self, event):
        jouerNote('Sol5')
    def SonLa5Min(self, event):
        jouerNote('LaMin5')
    def SonLa5(self, event):
        jouerNote('La5')
    def SonSi5Min(self, event):
        jouerNote('SiMin5')
    def SonSi5(self, event):
        jouerNote('Si5')

    def SonDo6 (self, event):
        jouerNote('Do6')
    def SonRe6Min (self, event):
        jouerNote('ReMin6')
    def SonRe6(self, event):
        jouerNote('Re6')
    def SonMi6Min(self, event):
        jouerNote('MiMin6')
    def SonMi6(self, event):
        jouerNote('Mi6')
    def SonFa6(self, event):
        jouerNote('Fa6')
    def SonSol6Min(self, event):
        jouerNote('SolMin6')
    def SonSol6(self, event):
        jouerNote('Sol6')
    def SonLa6Min(self, event):
        jouerNote('LaMin6')
    def SonLa6(self, event):
        jouerNote('La6')
    def SonSi6Min(self, event):
        jouerNote('SiMin6')
    def SonSi6(self, event):
        jouerNote('Si6')

    def SonDo7 (self, event):
        jouerNote('Do7')
    def SonRe7Min (self, event):
        jouerNote('ReMin7')
    def SonRe7(self, event):
        jouerNote('Re7')
    def SonMi7Min(self, event):
        jouerNote('MiMin7')
    def SonMi7(self, event):
        jouerNote('Mi7')
    def SonFa7(self, event):
        jouerNote('Fa7')
    def SonSol7Min(self, event):
        jouerNote('SolMin7')
    def SonSol7(self, event):
        jouerNote('Sol7')
    def SonLa7Min(self, event):
        jouerNote('LaMin7')
    def SonLa7(self, event):
        jouerNote('La7')
    def SonSi7Min(self, event):
        jouerNote('SiMin7')
    def SonSi7(self, event):
        jouerNote('Si7')
import icons




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


