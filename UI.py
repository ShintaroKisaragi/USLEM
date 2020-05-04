# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!




from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import qApp
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
import time

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
    



def son_music(octave):
    
            ########################### MIDI ###################
    track    = 0
    channel  = 0
    temps    = 0    # In beats
    #duration = 1.2    # In beats
    tempo    = 60   # In BPM
    volume   = 100  # 0-127, as per the MIDI standard
    i=0
    octave=1
    octavem=(-12)*2
    
    
    

    MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
                      # automatically)
    MyMIDI.addTempo(track, temps, tempo)


    continuer = 1 #Variable de boucle
    Do=sa.WaveObject.from_wave_file("sounds/Do"+str(octave)+".wav")
    ReMin=sa.WaveObject.from_wave_file("sounds/"+"ReMin"+str(octave)+".wav")
    Re=sa.WaveObject.from_wave_file("sounds/"+"Re"+str(octave)+".wav")
    MiMin=sa.WaveObject.from_wave_file("sounds/"+"MiMin"+str(octave)+".wav")
    Mi=sa.WaveObject.from_wave_file("sounds/"+"Mi"+str(octave)+".wav")
    Fa=sa.WaveObject.from_wave_file("sounds/"+"Fa"+str(octave)+".wav")
    SolMin=sa.WaveObject.from_wave_file("sounds/"+"SolMin"+str(octave)+".wav")
    Sol=sa.WaveObject.from_wave_file("sounds/"+"Sol"+str(octave)+".wav")
    LaMin=sa.WaveObject.from_wave_file("sounds/"+"LaMin"+str(octave)+".wav")
    La=sa.WaveObject.from_wave_file("sounds/"+"La"+str(octave)+".wav")
    SiMin=sa.WaveObject.from_wave_file("sounds/"+"SiMin"+str(octave)+".wav")
    Si=sa.WaveObject.from_wave_file("sounds/"+"Si"+str(octave)+".wav")
    Do2=sa.WaveObject.from_wave_file("sounds/"+"Do"+str(octave+1)+".wav")
    ReMin2=sa.WaveObject.from_wave_file("sounds/"+"ReMin"+str(octave+1)+".wav")
    Re2=sa.WaveObject.from_wave_file("sounds/"+"Re"+str(octave+1)+".wav")
    MiMin2=sa.WaveObject.from_wave_file("sounds/"+"MiMin"+str(octave+1)+".wav")
    Mi2=sa.WaveObject.from_wave_file("sounds/"+"Mi"+str(octave+1)+".wav")
    Fa2=sa.WaveObject.from_wave_file("sounds/"+"Fa"+str(octave+1)+".wav")
    SolMin2=sa.WaveObject.from_wave_file("sounds/"+"SolMin"+str(octave+1)+".wav")
    Sol2=sa.WaveObject.from_wave_file("sounds/"+"Sol"+str(octave+1)+".wav")

    while continuer==1:
        time.sleep(0.003)
        for event in pygame.event.get():
               
            


                
                #Octave
                if event.type == KEYDOWN and event.key == K_KP_PLUS and octave!=6:
                    octave=octave+1
                    octavem=octavem+12
                    Do=sa.WaveObject.from_wave_file("sounds/Do"+str(octave)+".wav")
                    ReMin=sa.WaveObject.from_wave_file("sounds/"+"ReMin"+str(octave)+".wav")
                    Re=sa.WaveObject.from_wave_file("sounds/"+"Re"+str(octave)+".wav")
                    MiMin=sa.WaveObject.from_wave_file("sounds/"+"MiMin"+str(octave)+".wav")
                    Mi=sa.WaveObject.from_wave_file("sounds/"+"Mi"+str(octave)+".wav")
                    Fa=sa.WaveObject.from_wave_file("sounds/"+"Fa"+str(octave)+".wav")
                    SolMin=sa.WaveObject.from_wave_file("sounds/"+"SolMin"+str(octave)+".wav")
                    Sol=sa.WaveObject.from_wave_file("sounds/"+"Sol"+str(octave)+".wav")
                    LaMin=sa.WaveObject.from_wave_file("sounds/"+"LaMin"+str(octave)+".wav")
                    La=sa.WaveObject.from_wave_file("sounds/"+"La"+str(octave)+".wav")
                    SiMin=sa.WaveObject.from_wave_file("sounds/"+"SiMin"+str(octave)+".wav")
                    Si=sa.WaveObject.from_wave_file("sounds/"+"Si"+str(octave)+".wav")
                    Do2=sa.WaveObject.from_wave_file("sounds/"+"Do"+str(octave+1)+".wav")
                    ReMin2=sa.WaveObject.from_wave_file("sounds/"+"ReMin"+str(octave+1)+".wav")
                    Re2=sa.WaveObject.from_wave_file("sounds/"+"Re"+str(octave+1)+".wav")
                    MiMin2=sa.WaveObject.from_wave_file("sounds/"+"MiMin"+str(octave+1)+".wav")
                    Mi2=sa.WaveObject.from_wave_file("sounds/"+"Mi"+str(octave+1)+".wav")
                    Fa2=sa.WaveObject.from_wave_file("sounds/"+"Fa"+str(octave+1)+".wav")
                    SolMin2=sa.WaveObject.from_wave_file("sounds/"+"SolMin"+str(octave+1)+".wav")
                    Sol2=sa.WaveObject.from_wave_file("sounds/"+"Sol"+str(octave+1)+".wav")


                    
                     
                if event.type == KEYUP and event.key == K_KP_MINUS and octave!=1:
                    octave=octave-1
                    octavem=octavem-12
                    Do=sa.WaveObject.from_wave_file("sounds/Do"+str(octave)+".wav")
                    ReMin=sa.WaveObject.from_wave_file("sounds/"+"ReMin"+str(octave)+".wav")
                    Re=sa.WaveObject.from_wave_file("sounds/"+"Re"+str(octave)+".wav")
                    MiMin=sa.WaveObject.from_wave_file("sounds/"+"MiMin"+str(octave)+".wav")
                    Mi=sa.WaveObject.from_wave_file("sounds/"+"Mi"+str(octave)+".wav")
                    Fa=sa.WaveObject.from_wave_file("sounds/"+"Fa"+str(octave)+".wav")
                    SolMin=sa.WaveObject.from_wave_file("sounds/"+"SolMin"+str(octave)+".wav")
                    Sol=sa.WaveObject.from_wave_file("sounds/"+"Sol"+str(octave)+".wav")
                    LaMin=sa.WaveObject.from_wave_file("sounds/"+"LaMin"+str(octave)+".wav")
                    La=sa.WaveObject.from_wave_file("sounds/"+"La"+str(octave)+".wav")
                    SiMin=sa.WaveObject.from_wave_file("sounds/"+"SiMin"+str(octave)+".wav")
                    Si=sa.WaveObject.from_wave_file("sounds/"+"Si"+str(octave)+".wav")
                    Do2=sa.WaveObject.from_wave_file("sounds/"+"Do"+str(octave+1)+".wav")
                    ReMin2=sa.WaveObject.from_wave_file("sounds/"+"ReMin"+str(octave+1)+".wav")
                    Re2=sa.WaveObject.from_wave_file("sounds/"+"Re"+str(octave+1)+".wav")
                    MiMin2=sa.WaveObject.from_wave_file("sounds/"+"MiMin"+str(octave+1)+".wav")
                    Mi2=sa.WaveObject.from_wave_file("sounds/"+"Mi"+str(octave+1)+".wav")
                    Fa2=sa.WaveObject.from_wave_file("sounds/"+"Fa"+str(octave+1)+".wav")
                    SolMin2=sa.WaveObject.from_wave_file("sounds/"+"SolMin"+str(octave+1)+".wav")
                    Sol2=sa.WaveObject.from_wave_file("sounds/"+"Sol"+str(octave+1)+".wav")

                #Escape
                if event.type == QUIT:
                    continuer=0
                    pygame.quit()

                #Do
                if event.type == KEYDOWN and event.key == K_a:
                    Dox=Do.play()
                    a=time.time()        
                    

                if event.type == KEYUP and event.key == K_a:
                    Dox.stop()
                    b=time.time()
                    t=b-a
                    duration=(t*60)/tempo
                    MyMIDI.addNote(track, channel, 60+octavem, a-c, duration, volume)
                    i=i+duration
                    
               
                    

                #ReMin
                if event.type == KEYDOWN and event.key == K_w:
                    ReMinx=ReMin.play()
                    a=time.time()
                if event.type == KEYUP and event.key == K_w:
                    ReMinx.stop()
                    b=time.time()
                    t=b-a
                    duration=(t*60)/tempo
                    MyMIDI.addNote(track, channel, 61+octavem, a-c, duration, volume)
                    i=i+duration

                #Re
                if event.type == KEYDOWN and event.key == K_s:
                    Rex=Re.play()
                    a=time.time()
                if event.type == KEYUP and event.key == K_s:
                    Rex.stop()
                    b=time.time()
                    t=b-a
                    duration=(t*60)/tempo
                    MyMIDI.addNote(track, channel, 62+octavem, a-c, duration, volume)
                    i=i+duration

                #MiMin
                if event.type == KEYDOWN and event.key == K_e:
                    MiMinx=MiMin.play()
                    a=time.time()
                if event.type == KEYUP and event.key == K_e:
                    MiMinx.stop()
                    b=time.time()
                    t=b-a
                    duration=(t*60)/tempo
                    MyMIDI.addNote(track, channel, 63+octavem, a-c, duration, volume)
                    i=i+duration

                #Mi
                if event.type == KEYDOWN and event.key == K_d:
                    Mix=Mi.play()
                    a=time.time()
                if event.type == KEYUP and event.key == K_d:
                    Mix.stop()
                    b=time.time()
                    t=b-a
                    duration=(t*60)/tempo
                    MyMIDI.addNote(track, channel, 64+octavem,a-c, duration, volume)
                    i=i+duration

                #Fa
                if event.type == KEYDOWN and event.key == K_f:
                    Fax=Fa.play()
                    a=time.time()
                if event.type == KEYUP and event.key == K_f:
                    Fax.stop()
                    b=time.time()
                    t=b-a
                    duration=(t*60)/tempo
                    MyMIDI.addNote(track, channel, 65+octavem, a-c, duration, volume)
                    i=i+duration

                #SolMin         
                if event.type == KEYDOWN and event.key == K_t:
                    SolMinx=SolMin.play()
                    a=time.time()
                if event.type == KEYUP and event.key == K_t:
                    SolMinx.stop()
                    b=time.time()
                    t=b-a
                    duration=(t*60)/tempo
                    MyMIDI.addNote(track, channel, 66+octavem, a-c, duration, volume)
                    i=i+duration

                #Sol
                if event.type == KEYDOWN and event.key == K_g:
                    Solx=Sol.play()
                    a=time.time()
                if event.type == KEYUP and event.key == K_g:
                    Solx.stop()
                    b=time.time()
                    t=b-a
                    duration=(t*60)/tempo
                    MyMIDI.addNote(track, channel, 67+octavem, a-c, duration, volume)
                    i=i+duration

                #LaMin
                if event.type == KEYDOWN and event.key == K_y:
                    LaMinx=LaMin.play()
                    a=time.time()
                if event.type == KEYUP and event.key == K_y:
                    LaMinx.stop()
                    b=time.time()
                    t=b-a
                    duration=(t*60)/tempo
                    MyMIDI.addNote(track, channel, 68+octavem, a-c, duration, volume)
                    i=i+duration

                #La
                if event.type == KEYDOWN and event.key == K_h:
                    Lax=La.play()
                    a=time.time()
                if event.type == KEYUP and event.key == K_h:
                    Lax.stop()
                    b=time.time()
                    t=b-a
                    duration=(t*60)/tempo
                    duration=b-a
                    MyMIDI.addNote(track, channel, 69+octavem, a-c, duration, volume)
                    i=i+duration

                #SiMin
                if event.type == KEYDOWN and event.key == K_u:
                    SiMinx=SiMin.play()
                    a=time.time()
                if event.type == KEYUP and event.key == K_u:
                    SiMinx.stop()
                    t=b-a
                    duration=(t*60)/tempo
                    duration=b-a
                    MyMIDI.addNote(track, channel, 70+octavem, a-c, duration, volume)
                    i=i+duration

                #Si
                if event.type == KEYDOWN and event.key == K_j:
                    Six=Si.play()
                    a=time.time()
                if event.type == KEYUP and event.key == K_j:
                    Six.stop()
                    b=time.time()
                    t=b-a
                    duration=(t*60)/tempo
                    MyMIDI.addNote(track, channel, 71+octavem, a-c, duration, volume)
                    i=i+duration

                #Do2
                if event.type == KEYDOWN and event.key == K_k:
                    Do2x=Do2.play()
                    a=time.time()
                if event.type == KEYUP and event.key == K_k:
                    Do2x.stop()
                    b=time.time()
                    t=b-a
                    duration=(t*60)/tempo
                    MyMIDI.addNote(track, channel, 72+octavem, a-c, duration, volume)
                    i=i+duration

                #ReMin2
                if event.type == KEYDOWN and event.key == K_o:
                    ReMin2x=ReMin2.play()
                    a=time.time()
                if event.type == KEYUP and event.key == K_o:
                    ReMin2x.stop()
                    b=time.time()
                    t=b-a
                    duration=(t*60)/tempo
                    MyMIDI.addNote(track, channel, 73+octavem, a-c, duration, volume)
                    i=i+duration

                #Re2
                if event.type == KEYDOWN and event.key == K_l:
                    Re2x=Re2.play()
                    a=time.time()
                if event.type == KEYUP and event.key == K_l:
                    Re2x.stop()
                    b=time.time()
                    t=b-a
                    duration=(t*60)/tempo
                    MyMIDI.addNote(track, channel, 74+octavem, a-c, duration, volume)
                    i=i+duration

                #MiMin2
                if event.type == KEYDOWN and event.key == K_p:
                    MiMin2x=MiMin2.play()
                    a=time.time()
                if event.type == KEYUP and event.key == K_p:
                    MiMin2x.stop()
                    b=time.time()
                    t=b-a
                    duration=(t*60)/tempo
                    MyMIDI.addNote(track, channel, 75+octavem, a-c, duration, volume)
                    i=i+duration

                #Mi2
                if event.type == KEYDOWN and event.key == K_SEMICOLON:
                    Mi2x=Mi2.play()
                    a=time.time()
                if event.type == KEYUP and event.key == K_SEMICOLON:
                    Mi2x.stop()
                    b=time.time()
                    t=b-a
                    duration=(t*60)/tempo
                    MyMIDI.addNote(track, channel, 76+octavem, a-c, duration, volume)
                    i=i+duration

                if event.type == KEYDOWN and event.key == K_QUOTE:
                    Fa2x=Fa2.play()
                    a=time.time()
                if event.type == KEYUP and event.key == K_QUOTE:
                    Fa2x.stop()
                    b=time.time()
                    t=b-a
                    duration=(t*60)/tempo
                    MyMIDI.addNote(track, channel, 77+octavem, a-c, duration, volume)
                    i=i+duration

                if event.type == KEYDOWN and event.key == K_RIGHTBRACKET:
                    SolMin2x=SolMin2.play()
                    a=time.time()
                if event.type == KEYUP and event.key == K_RIGHTBRACKET:
                    SolMin2x.stop()
                    b=time.time()
                    t=b-a
                    duration=(t*60)/tempo
                    MyMIDI.addNote(track, channel, 78+octavem, a-c, duration, volume)
                    i=i+duration

                if event.type == KEYDOWN and event.key == K_BACKSLASH:
                    Sol2x=Sol2.play()
                    a=time.time()
                if event.type == KEYUP and event.key == K_BACKSLASH:
                    Sol2x.stop()
                    b=time.time()
                    t=b-a
                    duration=(t*60)/tempo
                    MyMIDI.addNote(track, channel, 79+octavem, a-c, duration, volume)
                    i=i+duration
                if event.type == KEYDOWN and event.key == K_SPACE:
                    with open("midi/"+name+".mid", "wb") as output_file:
                        MyMIDI.writeFile(output_file)#!/usr/bin/env python
                    with open("partition.mid", "wb") as output_file:
                        MyMIDI.writeFile(output_file)#!/usr/bin/env python

                if event.type == KEYDOWN and event.key == K_v:
                    c=time.time()


############################################################# Main #################################################################################
"""----------------------------------------------------------------------------------------------------------------------------------------------"""
####################################################################################################################################################

def textchanged(text):
    global filename
    filename = text
    
    

def save():
    global name
    name=filename       #fonction d'enregistrement du fichier. Le nom du fichier est dans la variable "filename" définie avec la fonction juste au dessus

def jouerNote(note):
    wave_obj = notes[note]
    play_obj = wave_obj.play()

notes = {
    'La1': sa.WaveObject.from_wave_file('sounds/La1.wav'),
    'La2': sa.WaveObject.from_wave_file('sounds/La2.wav'),
    'La3': sa.WaveObject.from_wave_file('sounds/La3.wav'),
    'La4': sa.WaveObject.from_wave_file('sounds/La4.wav'),
    'La5': sa.WaveObject.from_wave_file('sounds/La5.wav'),
    'La6': sa.WaveObject.from_wave_file('sounds/La6.wav'),
    'La7': sa.WaveObject.from_wave_file('sounds/La7.wav'),
    'LaMin1': sa.WaveObject.from_wave_file('sounds/LaMin1.wav'),
    'LaMin2': sa.WaveObject.from_wave_file('sounds/LaMin2.wav'),
    'LaMin3': sa.WaveObject.from_wave_file('sounds/LaMin3.wav'),
    'LaMin4': sa.WaveObject.from_wave_file('sounds/LaMin4.wav'),
    'LaMin5': sa.WaveObject.from_wave_file('sounds/LaMin5.wav'),
    'LaMin6': sa.WaveObject.from_wave_file('sounds/LaMin6.wav'),
    'LaMin7': sa.WaveObject.from_wave_file('sounds/LaMin7.wav'),
    'Si1': sa.WaveObject.from_wave_file('sounds/Si1.wav'),
    'Si2': sa.WaveObject.from_wave_file('sounds/Si2.wav'),
    'Si3': sa.WaveObject.from_wave_file('sounds/Si3.wav'),
    'Si4': sa.WaveObject.from_wave_file('sounds/Si4.wav'),
    'Si5': sa.WaveObject.from_wave_file('sounds/Si5.wav'),
    'Si6': sa.WaveObject.from_wave_file('sounds/Si6.wav'),
    'Si7': sa.WaveObject.from_wave_file('sounds/Si7.wav'),
    'SiMin1': sa.WaveObject.from_wave_file('sounds/SiMin1.wav'),
    'SiMin2': sa.WaveObject.from_wave_file('sounds/SiMin2.wav'),
    'SiMin3': sa.WaveObject.from_wave_file('sounds/SiMin3.wav'),
    'SiMin4': sa.WaveObject.from_wave_file('sounds/SiMin4.wav'),
    'SiMin5': sa.WaveObject.from_wave_file('sounds/SiMin5.wav'),
    'SiMin6': sa.WaveObject.from_wave_file('sounds/SiMin6.wav'),
    'SiMin7': sa.WaveObject.from_wave_file('sounds/SiMin7.wav'),
    'Do1': sa.WaveObject.from_wave_file('sounds/Do1.wav'),
    'Do2': sa.WaveObject.from_wave_file('sounds/Do2.wav'),
    'Do3': sa.WaveObject.from_wave_file('sounds/Do3.wav'),
    'Do4': sa.WaveObject.from_wave_file('sounds/Do4.wav'),
    'Do5': sa.WaveObject.from_wave_file('sounds/Do5.wav'),
    'Do6': sa.WaveObject.from_wave_file('sounds/Do6.wav'),
    'Do7': sa.WaveObject.from_wave_file('sounds/Do7.wav'),
    'Re1': sa.WaveObject.from_wave_file('sounds/Re1.wav'),
    'Re2': sa.WaveObject.from_wave_file('sounds/Re2.wav'),
    'Re3': sa.WaveObject.from_wave_file('sounds/Re3.wav'),
    'Re4': sa.WaveObject.from_wave_file('sounds/Re4.wav'),
    'Re5': sa.WaveObject.from_wave_file('sounds/Re5.wav'),
    'Re6': sa.WaveObject.from_wave_file('sounds/Re6.wav'),
    'Re7': sa.WaveObject.from_wave_file('sounds/Re7.wav'),
    'ReMin1': sa.WaveObject.from_wave_file('sounds/ReMin1.wav'),
    'ReMin2': sa.WaveObject.from_wave_file('sounds/ReMin2.wav'),
    'ReMin3': sa.WaveObject.from_wave_file('sounds/ReMin3.wav'),
    'ReMin4': sa.WaveObject.from_wave_file('sounds/ReMin4.wav'),
    'ReMin5': sa.WaveObject.from_wave_file('sounds/ReMin5.wav'),
    'ReMin6': sa.WaveObject.from_wave_file('sounds/ReMin6.wav'),
    'ReMin7': sa.WaveObject.from_wave_file('sounds/ReMin7.wav'),
    'Mi1': sa.WaveObject.from_wave_file('sounds/Mi1.wav'),
    'Mi2': sa.WaveObject.from_wave_file('sounds/Mi2.wav'),
    'Mi3': sa.WaveObject.from_wave_file('sounds/Mi3.wav'),
    'Mi4': sa.WaveObject.from_wave_file('sounds/Mi4.wav'),
    'Mi5': sa.WaveObject.from_wave_file('sounds/Mi5.wav'),
    'Mi6': sa.WaveObject.from_wave_file('sounds/Mi6.wav'),
    'Mi7': sa.WaveObject.from_wave_file('sounds/Mi7.wav'),
    'MiMin1': sa.WaveObject.from_wave_file('sounds/MiMin1.wav'),
    'MiMin2': sa.WaveObject.from_wave_file('sounds/MiMin2.wav'),
    'MiMin3': sa.WaveObject.from_wave_file('sounds/MiMin3.wav'),
    'MiMin4': sa.WaveObject.from_wave_file('sounds/MiMin4.wav'),
    'MiMin5': sa.WaveObject.from_wave_file('sounds/MiMin5.wav'),
    'MiMin6': sa.WaveObject.from_wave_file('sounds/MiMin6.wav'),
    'MiMin7': sa.WaveObject.from_wave_file('sounds/MiMin7.wav'),
    'Fa1': sa.WaveObject.from_wave_file('sounds/Fa1.wav'),
    'Fa2': sa.WaveObject.from_wave_file('sounds/Fa2.wav'),
    'Fa3': sa.WaveObject.from_wave_file('sounds/Fa3.wav'),
    'Fa4': sa.WaveObject.from_wave_file('sounds/Fa4.wav'),
    'Fa5': sa.WaveObject.from_wave_file('sounds/Fa5.wav'),
    'Fa6': sa.WaveObject.from_wave_file('sounds/Fa6.wav'),
    'Fa7': sa.WaveObject.from_wave_file('sounds/Fa7.wav'),
    'SolMin1': sa.WaveObject.from_wave_file('sounds/SolMin1.wav'),
    'SolMin2': sa.WaveObject.from_wave_file('sounds/SolMin2.wav'),
    'SolMin3': sa.WaveObject.from_wave_file('sounds/SolMin3.wav'),
    'SolMin4': sa.WaveObject.from_wave_file('sounds/SolMin4.wav'),
    'SolMin5': sa.WaveObject.from_wave_file('sounds/SolMin5.wav'),
    'SolMin6': sa.WaveObject.from_wave_file('sounds/SolMin6.wav'),
    'SolMin7': sa.WaveObject.from_wave_file('sounds/SolMin7.wav'),
    'Sol1': sa.WaveObject.from_wave_file('sounds/Sol1.wav'),
    'Sol2': sa.WaveObject.from_wave_file('sounds/Sol2.wav'),
    'Sol3': sa.WaveObject.from_wave_file('sounds/Sol3.wav'),
    'Sol4': sa.WaveObject.from_wave_file('sounds/Sol4.wav'),
    'Sol5': sa.WaveObject.from_wave_file('sounds/Sol5.wav'),
    'Sol6': sa.WaveObject.from_wave_file('sounds/Sol6.wav'),
    'Sol7': sa.WaveObject.from_wave_file('sounds/Sol7.wav')
    }

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(891, 685)
        MainWindow.setMinimumSize(QtCore.QSize(891, 685))
        MainWindow.setMaximumSize(QtCore.QSize(891, 685))
        MainWindow.setBaseSize(QtCore.QSize(1280, 720))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icones/022-sound.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.enregistrer.setGeometry(QtCore.QRect(10, 590, 75, 23))
        self.enregistrer.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.enregistrer.setText("Enregistrer")
        self.enregistrer.clicked.connect(save)          #précise la fonction d'enregistrement à appeler. Peut être remplacé par une autre fonction

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.textChanged.connect(textchanged)
        self.lineEdit.setGeometry(QtCore.QRect(90, 590, 791, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
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

            #Ouverture de la fenêtre Pygame
            fenetre = pygame.display.set_mode((640, 480))
            pygame.display.set_caption("USLEM")
            pygame.display.set_icon(pygame.image.load("sound.png"))

            #Chargement et collage du fond
            fond = pygame.image.load("piano.jpg").convert()
            fenetre.blit(fond, (0,0))

            #Rafraîchissement de l'écran
            pygame.display.flip()
            son_music2(2)
            pygame.quit()
            return 0

        def piano():
            pygame.init()

            #Ouverture de la fenêtre Pygame
            fenetre = pygame.display.set_mode((640, 480))
            pygame.display.set_caption("USLEM")
            pygame.display.set_icon(pygame.image.load("sound.png"))

            #Chargement et collage du fond
            fond = pygame.image.load("piano.jpg").convert()
            fenetre.blit(fond, (0,0))

            #Rafraîchissement de l'écran
            pygame.display.flip()
            son_music(2)
            pygame.quit()
            return 0

        


        self.Clavier2 = QtWidgets.QPushButton(self.centralwidget)
        self.Clavier2.setGeometry(QtCore.QRect(780, 330, 101, 61))
        self.Clavier2.setMinimumSize(QtCore.QSize(0, 0))
        self.Clavier2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Clavier2.setText("Passer en mode \n clavier sans \n enregistrement")
        self.Clavier2.setAutoRepeat(False)
        self.Clavier2.clicked.connect(lambda:piano2())
        

        self.Clavier = QtWidgets.QPushButton(self.centralwidget)
        self.Clavier.setGeometry(QtCore.QRect(780, 400, 101, 61))
        self.Clavier.setMinimumSize(QtCore.QSize(0, 0))
        self.Clavier.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Clavier.setText("Passer en mode \n clavier avec \n enregistrement")
        self.Clavier.setAutoRepeat(False)
        self.Clavier.clicked.connect(lambda:piano())


        

        def partition():
            os.system("taskkill /im MidiSheetMusic-2.6.exe /f")
            os.startfile("partition.mid")
            

        self.partition = QtWidgets.QPushButton(self.centralwidget)
        self.partition.setGeometry(QtCore.QRect(780, 470, 100, 61))
        self.partition.setMinimumSize(QtCore.QSize(0, 0))
        self.partition.setStyleSheet("background-color: rgb(255, 255, 255);")
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
        
        self.menuFile_Fichier = QtWidgets.QMenu(self.menubar)
        self.menuFile_Fichier.setObjectName("menuFile_Fichier")
        
        self.menuIntrument = QtWidgets.QMenu(self.menubar)
        self.menuIntrument.setObjectName("menuIntrument")
        
        self.menuPiano = QtWidgets.QMenu(self.menuIntrument)
        self.menuPiano.setObjectName("menuPiano")
        
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
        self.actionSave_Enregistrer = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Icones/035-save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_Enregistrer.setIcon(icon3)
        
        self.actionSave_Enregistrer.setObjectName("actionSave_Enregistrer")
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
        self.actionNew_Nouveau_2 = QtWidgets.QAction(MainWindow)
        self.actionNew_Nouveau_2.setObjectName("actionNew_Nouveau_2")
        self.actionOpen_Ovrir = QtWidgets.QAction(MainWindow)
        self.actionOpen_Ovrir.setObjectName("actionOpen_Ovrir")
        self.actionSave_Enregistrer_2 = QtWidgets.QAction(MainWindow)
        self.actionSave_Enregistrer_2.setObjectName("actionSave_Enregistrer_2")
        self.actionSettings_Param_tres_2 = QtWidgets.QAction(MainWindow)
        self.actionSettings_Param_tres_2.setObjectName("actionSettings_Parametres_2")
        self.actionQuit_Quitter_2 = QtWidgets.QAction(MainWindow)
        self.actionQuit_Quitter_2.setObjectName("actionQuit_Quitter_2")
        self.actionPianissimo = QtWidgets.QAction(MainWindow)
        self.actionPianissimo.setCheckable(True)
        self.actionPianissimo.setObjectName("actionPianissimo")
        self.actionMezzo_Forte = QtWidgets.QAction(MainWindow)
        self.actionMezzo_Forte.setCheckable(True)
        self.actionMezzo_Forte.setObjectName("actionMezzo_Forte")
        self.actionFortissimo = QtWidgets.QAction(MainWindow)
        self.actionFortissimo.setCheckable(True)
        self.actionFortissimo.setObjectName("actionFortissimo")
        self.menuFile_Fichier.addAction(self.actionNew_Nouveau_2)
        self.menuFile_Fichier.addAction(self.actionOpen_Ovrir)
        self.menuFile_Fichier.addAction(self.actionSave_Enregistrer_2)
        self.menuFile_Fichier.addSeparator()
        self.menuFile_Fichier.addAction(self.actionSettings_Param_tres_2)
        self.menuFile_Fichier.addSeparator()
        self.menuFile_Fichier.addAction(self.actionQuit_Quitter_2)
        self.menuPiano.addAction(self.actionPianissimo)
        self.menuPiano.addAction(self.actionMezzo_Forte)
        self.menuPiano.addAction(self.actionFortissimo)
        self.menuIntrument.addAction(self.menuPiano.menuAction())
        self.menubar.addAction(self.menuFile_Fichier.menuAction())
        self.menubar.addAction(self.menuIntrument.menuAction())
        
        self.toolBar.addAction(self.actionNew_Nouveau)
        self.toolBar.addAction(self.actionOpen_Ouvvrir)
        self.toolBar.addAction(self.actionSave_Enregistrer)
        self.toolBar.addAction(self.actionSettings_Param_tres)
        self.toolBar.addAction(self.actionQuit_Quitter)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "USLEM"))
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
        self.menuFile_Fichier.setTitle(_translate("MainWindow", "File - Fichier"))
        self.menuIntrument.setTitle(_translate("MainWindow", "Intrument"))
        self.menuPiano.setTitle(_translate("MainWindow", "Piano"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionNew_Nouveau.setText(_translate("MainWindow", "New - Nouveau"))
        self.actionNew_Nouveau.setToolTip(_translate("MainWindow", "Erase all datas and create a new record - Efface toutes les données et crée un nouveau fichier"))
        self.actionOpen_Ouvvrir.setText(_translate("MainWindow", "Open... - Ouvvrir..."))
        self.actionOpen_Ouvvrir.setToolTip(_translate("MainWindow", "Opens a record - Ouvre un enregistrement"))
        self.actionSave_Enregistrer.setText(_translate("MainWindow", "Save - Enregistrer"))
        self.actionSave_Enregistrer.setToolTip(_translate("MainWindow", "Saves all datas - Enregistre toutes les données"))
        self.actionQuit_Quitter.setText(_translate("MainWindow", "Quit - Quitter"))
        self.actionQuit_Quitter.setToolTip(_translate("MainWindow", "Closes application - Ferme l\'application"))
        self.actionSettings_Param_tres.setText(_translate("MainWindow", "Settings - Paramètres"))
        self.actionSettings_Param_tres.setToolTip(_translate("MainWindow", "Opens the settings panel - Ouvre la fenêtre des paramètres"))
        self.actionNew_Nouveau_2.setText(_translate("MainWindow", "New - Nouveau"))
        self.actionOpen_Ovrir.setText(_translate("MainWindow", "Open - Ovrir"))
        self.actionSave_Enregistrer_2.setText(_translate("MainWindow", "Save - Enregistrer"))
        self.actionSettings_Param_tres_2.setText(_translate("MainWindow", "Settings - Paramètres"))
        self.actionQuit_Quitter_2.setText(_translate("MainWindow", "Quit - Quitter"))
        self.actionPianissimo.setText(_translate("MainWindow", "Pianissimo"))
        self.actionMezzo_Forte.setText(_translate("MainWindow", "Mezzo Forte"))
        self.actionFortissimo.setText(_translate("MainWindow", "Fortissimo"))

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


