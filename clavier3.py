from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import*
import sys
from datetime import *
import os
from random import *
import simpleaudio as sa

import pygame
from pygame.locals import *
from pygame import*
from midiutil import*
import pygame.midi


from time import*
import time

def son_music(c,octave,instrument,name):
    
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
    Do=sa.WaveObject.from_wave_file("sounds/"+instrument+"/C"+str(octave)+".wav")
    ReMin=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Db"+str(octave)+".wav")
    Re=sa.WaveObject.from_wave_file("sounds/"+instrument+"/D"+str(octave)+".wav")
    MiMin=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Eb"+str(octave)+".wav")
    Mi=sa.WaveObject.from_wave_file("sounds/"+instrument+"/E"+str(octave)+".wav")
    Fa=sa.WaveObject.from_wave_file("sounds/"+instrument+"/F"+str(octave)+".wav")
    SolMin=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Gb"+str(octave)+".wav")
    Sol=sa.WaveObject.from_wave_file("sounds/"+instrument+"/G"+str(octave)+".wav")
    LaMin=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Ab"+str(octave)+".wav")
    La=sa.WaveObject.from_wave_file("sounds/"+instrument+"/A"+str(octave)+".wav")
    SiMin=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Bb"+str(octave)+".wav")
    Si=sa.WaveObject.from_wave_file("sounds/"+instrument+"/B"+str(octave)+".wav")

    Do2=sa.WaveObject.from_wave_file("sounds/"+instrument+"/C"+str(octave+1)+".wav")
    ReMin2=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Db"+str(octave+1)+".wav")
    Re2=sa.WaveObject.from_wave_file("sounds/"+instrument+"/D"+str(octave+1)+".wav")
    MiMin2=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Eb"+str(octave+1)+".wav")
    Mi2=sa.WaveObject.from_wave_file("sounds/"+instrument+"/E"+str(octave+1)+".wav")
    Fa2=sa.WaveObject.from_wave_file("sounds/"+instrument+"/F"+str(octave+1)+".wav")
    SolMin2=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Gb"+str(octave+1)+".wav")
    Sol2=sa.WaveObject.from_wave_file("sounds/"+instrument+"/G"+str(octave+1)+".wav")

    while continuer==1:
        time.sleep(0.003)
        for event in pygame.event.get():
               
            


                
                #Octave
                if event.type == KEYDOWN and event.key == K_KP_PLUS and octave!=6:
                    octave=octave+1
                    octavem=octavem+12
                    Do=sa.WaveObject.from_wave_file("sounds/"+instrument+"/C"+str(octave)+".wav")
                    ReMin=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Db"+str(octave)+".wav")
                    Re=sa.WaveObject.from_wave_file("sounds/"+instrument+"/D"+str(octave)+".wav")
                    MiMin=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Eb"+str(octave)+".wav")
                    Mi=sa.WaveObject.from_wave_file("sounds/"+instrument+"/E"+str(octave)+".wav")
                    Fa=sa.WaveObject.from_wave_file("sounds/"+instrument+"/F"+str(octave)+".wav")
                    SolMin=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Gb"+str(octave)+".wav")
                    Sol=sa.WaveObject.from_wave_file("sounds/"+instrument+"/G"+str(octave)+".wav")
                    LaMin=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Ab"+str(octave)+".wav")
                    La=sa.WaveObject.from_wave_file("sounds/"+instrument+"/A"+str(octave)+".wav")
                    SiMin=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Bb"+str(octave)+".wav")
                    Si=sa.WaveObject.from_wave_file("sounds/"+instrument+"/B"+str(octave)+".wav")

                    Do2=sa.WaveObject.from_wave_file("sounds/"+instrument+"/C"+str(octave+1)+".wav")
                    ReMin2=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Db"+str(octave+1)+".wav")
                    Re2=sa.WaveObject.from_wave_file("sounds/"+instrument+"/D"+str(octave+1)+".wav")
                    MiMin2=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Eb"+str(octave+1)+".wav")
                    Mi2=sa.WaveObject.from_wave_file("sounds/"+instrument+"/E"+str(octave+1)+".wav")
                    Fa2=sa.WaveObject.from_wave_file("sounds/"+instrument+"/F"+str(octave+1)+".wav")
                    SolMin2=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Gb"+str(octave+1)+".wav")
                    Sol2=sa.WaveObject.from_wave_file("sounds/"+instrument+"/G"+str(octave+1)+".wav")


                    
                     
                if event.type == KEYUP and event.key == K_KP_MINUS and octave!=1:
                    octave=octave-1
                    octavem=octavem-12
                    Do=sa.WaveObject.from_wave_file("sounds/"+instrument+"/C"+str(octave)+".wav")
                    ReMin=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Db"+str(octave)+".wav")
                    Re=sa.WaveObject.from_wave_file("sounds/"+instrument+"/D"+str(octave)+".wav")
                    MiMin=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Eb"+str(octave)+".wav")
                    Mi=sa.WaveObject.from_wave_file("sounds/"+instrument+"/E"+str(octave)+".wav")
                    Fa=sa.WaveObject.from_wave_file("sounds/"+instrument+"/F"+str(octave)+".wav")
                    SolMin=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Gb"+str(octave)+".wav")
                    Sol=sa.WaveObject.from_wave_file("sounds/"+instrument+"/G"+str(octave)+".wav")
                    LaMin=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Ab"+str(octave)+".wav")
                    La=sa.WaveObject.from_wave_file("sounds/"+instrument+"/A"+str(octave)+".wav")
                    SiMin=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Bb"+str(octave)+".wav")
                    Si=sa.WaveObject.from_wave_file("sounds/"+instrument+"/B"+str(octave)+".wav")

                    Do2=sa.WaveObject.from_wave_file("sounds/"+instrument+"/C"+str(octave+1)+".wav")
                    ReMin2=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Db"+str(octave+1)+".wav")
                    Re2=sa.WaveObject.from_wave_file("sounds/"+instrument+"/D"+str(octave+1)+".wav")
                    MiMin2=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Eb"+str(octave+1)+".wav")
                    Mi2=sa.WaveObject.from_wave_file("sounds/"+instrument+"/E"+str(octave+1)+".wav")
                    Fa2=sa.WaveObject.from_wave_file("sounds/"+instrument+"/F"+str(octave+1)+".wav")
                    SolMin2=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Gb"+str(octave+1)+".wav")
                    Sol2=sa.WaveObject.from_wave_file("sounds/"+instrument+"/G"+str(octave+1)+".wav")

                #Escape
                if event.type == QUIT:
                    with open("midi/"+name+".mid", "wb") as output_file:
                        MyMIDI.writeFile(output_file)#!/usr/bin/env python
                    with open("partition.mid", "wb") as output_file:
                        MyMIDI.writeFile(output_file)#!/usr/bin/env python
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


