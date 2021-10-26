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


def son_music6(c,a,instrument,name):
    octave=2
    
            ########################### MIDI ###################
    track    = 0
    channel  = 0
    temps    = 0    # In beats
    #duration = 1.2    # In beats
    tempo    = 60   # In BPM
    volume   = 100  # 0-127, as per the MIDI standard
    i=0
    
    octavem=(-12)*2

    device_id=a
    pygame.init()
    pygame.midi.init()
    pygame.fastevent.init()
    event_get = pygame.fastevent.get
    event_post = pygame.fastevent.post

    

    


    if device_id is None:
        input_id = pygame.midi.get_default_input_id()
    else:
        input_id = device_id

    
    i2 = pygame.midi.Input( input_id )

    



    going = True
    x=0
    
    
    

    MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
                      # automatically)
    MyMIDI.addTempo(track, temps, tempo)


    octave=1
    C1=sa.WaveObject.from_wave_file("sounds/"+instrument+"/C1.wav")
    Db1=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Db1.wav")
    D1=sa.WaveObject.from_wave_file("sounds/"+instrument+"/D1.wav")
    Eb1=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Eb1.wav")
    E1=sa.WaveObject.from_wave_file("sounds/"+instrument+"/E1.wav")
    F1=sa.WaveObject.from_wave_file("sounds/"+instrument+"/F1.wav")
    Gb1=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Gb1.wav")
    G1=sa.WaveObject.from_wave_file("sounds/"+instrument+"/G1.wav")
    Ab1=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Ab1.wav")
    A1=sa.WaveObject.from_wave_file("sounds/"+instrument+"/A1.wav")
    Bb1=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Bb1.wav")
    B1=sa.WaveObject.from_wave_file("sounds/"+instrument+"/B1.wav")
    C2=sa.WaveObject.from_wave_file("sounds/"+instrument+"/C2.wav")
    Db2=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Db2.wav")
    D2=sa.WaveObject.from_wave_file("sounds/"+instrument+"/D2.wav")
    Eb2=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Eb2.wav")
    E2=sa.WaveObject.from_wave_file("sounds/"+instrument+"/E2.wav")
    F2=sa.WaveObject.from_wave_file("sounds/"+instrument+"/F2.wav")
    Gb2=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Gb2.wav")
    G2=sa.WaveObject.from_wave_file("sounds/"+instrument+"/G2.wav")
    Ab2=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Ab2.wav")
    A2=sa.WaveObject.from_wave_file("sounds/"+instrument+"/A2.wav")
    Bb2=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Bb2.wav")
    B2=sa.WaveObject.from_wave_file("sounds/"+instrument+"/B2.wav")
    C3=sa.WaveObject.from_wave_file("sounds/"+instrument+"/C3.wav")
    Db3=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Db3.wav")
    D3=sa.WaveObject.from_wave_file("sounds/"+instrument+"/D3.wav")
    Eb3=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Eb3.wav")
    E3=sa.WaveObject.from_wave_file("sounds/"+instrument+"/E3.wav")
    F3=sa.WaveObject.from_wave_file("sounds/"+instrument+"/F3.wav")
    Gb3=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Gb3.wav")
    G3=sa.WaveObject.from_wave_file("sounds/"+instrument+"/G3.wav")
    Ab3=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Ab3.wav")
    A3=sa.WaveObject.from_wave_file("sounds/"+instrument+"/A3.wav")
    Bb3=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Bb3.wav")
    B3=sa.WaveObject.from_wave_file("sounds/"+instrument+"/B3.wav")
    C4=sa.WaveObject.from_wave_file("sounds/"+instrument+"/C4.wav")
    Db4=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Db4.wav")
    D4=sa.WaveObject.from_wave_file("sounds/"+instrument+"/D4.wav")
    Eb4=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Eb4.wav")
    E4=sa.WaveObject.from_wave_file("sounds/"+instrument+"/E4.wav")
    F4=sa.WaveObject.from_wave_file("sounds/"+instrument+"/F4.wav")
    Gb4=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Gb4.wav")
    G4=sa.WaveObject.from_wave_file("sounds/"+instrument+"/G4.wav")
    Ab4=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Ab4.wav")
    A4=sa.WaveObject.from_wave_file("sounds/"+instrument+"/A4.wav")
    Bb4=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Bb4.wav")
    B4=sa.WaveObject.from_wave_file("sounds/"+instrument+"/B4.wav")
    C5=sa.WaveObject.from_wave_file("sounds/"+instrument+"/C5.wav")
    Db5=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Db5.wav")
    D5=sa.WaveObject.from_wave_file("sounds/"+instrument+"/D5.wav")
    Eb5=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Eb5.wav")
    E5=sa.WaveObject.from_wave_file("sounds/"+instrument+"/E5.wav")
    F5=sa.WaveObject.from_wave_file("sounds/"+instrument+"/F5.wav")
    Gb5=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Gb5.wav")
    G5=sa.WaveObject.from_wave_file("sounds/"+instrument+"/G5.wav")
    Ab5=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Ab5.wav")
    A5=sa.WaveObject.from_wave_file("sounds/"+instrument+"/A5.wav")
    Bb5=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Bb5.wav")
    B5=sa.WaveObject.from_wave_file("sounds/"+instrument+"/B5.wav")
    C6=sa.WaveObject.from_wave_file("sounds/"+instrument+"/C6.wav")
    Db6=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Db6.wav")
    D6=sa.WaveObject.from_wave_file("sounds/"+instrument+"/D6.wav")
    Eb6=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Eb6.wav")
    E6=sa.WaveObject.from_wave_file("sounds/"+instrument+"/E6.wav")
    F6=sa.WaveObject.from_wave_file("sounds/"+instrument+"/F6.wav")
    Gb6=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Gb6.wav")
    G6=sa.WaveObject.from_wave_file("sounds/"+instrument+"/G6.wav")
    Ab6=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Ab6.wav")
    A6=sa.WaveObject.from_wave_file("sounds/"+instrument+"/A6.wav")
    Bb6=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Bb6.wav")
    B6=sa.WaveObject.from_wave_file("sounds/"+instrument+"/B6.wav")
    C7=sa.WaveObject.from_wave_file("sounds/"+instrument+"/C7.wav")
    Db7=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Db7.wav")
    D7=sa.WaveObject.from_wave_file("sounds/"+instrument+"/D7.wav")
    Eb7=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Eb7.wav")
    E7=sa.WaveObject.from_wave_file("sounds/"+instrument+"/E7.wav")
    F7=sa.WaveObject.from_wave_file("sounds/"+instrument+"/F7.wav")
    Gb7=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Gb7.wav")
    G7=sa.WaveObject.from_wave_file("sounds/"+instrument+"/G7.wav")
    Ab7=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Ab7.wav")
    A7=sa.WaveObject.from_wave_file("sounds/"+instrument+"/A7.wav")
    Bb7=sa.WaveObject.from_wave_file("sounds/"+instrument+"/Bb7.wav")
    B7=sa.WaveObject.from_wave_file("sounds/"+instrument+"/B7.wav")
    
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



    while going==1:
        time.sleep(0.003)
        for e in event_get():
            event=e
               
            


            
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
                going=0
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
                print(duration)
                MyMIDI.addNote(track, channel, 60+octavem, a-c, duration, volume)
                a=i+duration
                
                
           
                

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
                    
            if event.type == KEYUP and event.key == K_v:
                c=time.time()

            

            

            if e.type in [pygame.midi.MIDIIN]:          


                if e.data1==12:
                    if e.data2 !=0:
                        C1x=C1.play()
                        a=time.time()
                    elif e.data2==0:
                        C1x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,12,a-c, duration, volume)
                        i=i+duration
                if e.data1==13:
                    if e.data2 !=0:
                        Db1x=Db1.play()
                        a=time.time()
                    elif e.data2==0:
                        Db1x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,13,a-c, duration, volume)
                        i=i+duration
                if e.data1==14:
                    if e.data2 !=0:
                        D1x=D1.play()
                        a=time.time()
                    elif e.data2==0:
                        D1x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,14,a-c, duration, volume)
                        i=i+duration
                if e.data1==15:
                    if e.data2 !=0:
                        Eb1x=Eb1.play()
                        a=time.time()
                    elif e.data2==0:
                        Eb1x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,15,a-c, duration, volume)
                        i=i+duration
                if e.data1==16:
                    if e.data2 !=0:
                        E1x=E1.play()
                        a=time.time()
                    elif e.data2==0:
                        E1x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,16,a-c, duration, volume)
                        i=i+duration
                if e.data1==17:
                    if e.data2 !=0:
                        F1x=F1.play()
                        a=time.time()
                    elif e.data2==0:
                        F1x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,17,a-c, duration, volume)
                        i=i+duration
                if e.data1==18:
                    if e.data2 !=0:
                        Gb1x=Gb1.play()
                        a=time.time()
                    elif e.data2==0:
                        Gb1x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,18,a-c, duration, volume)
                        i=i+duration
                if e.data1==19:
                    if e.data2 !=0:
                        G1x=G1.play()
                        a=time.time()
                    elif e.data2==0:
                        G1x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,19,a-c, duration, volume)
                        i=i+duration
                if e.data1==20:
                    if e.data2 !=0:
                        Ab1x=Ab1.play()
                        a=time.time()
                    elif e.data2==0:
                        Ab1x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,20,a-c, duration, volume)
                        i=i+duration
                if e.data1==21:
                    if e.data2 !=0:
                        A1x=A1.play()
                        a=time.time()
                    elif e.data2==0:
                        A1x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,21,a-c, duration, volume)
                        i=i+duration
                if e.data1==22:
                    if e.data2 !=0:
                        Bb1x=Bb1.play()
                        a=time.time()
                    elif e.data2==0:
                        Bb1x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,22,a-c, duration, volume)
                        i=i+duration
                if e.data1==23:
                    if e.data2 !=0:
                        B1x=B1.play()
                        a=time.time()
                    elif e.data2==0:
                        B1x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,23,a-c, duration, volume)
                        i=i+duration
                if e.data1==24:
                    if e.data2 !=0:
                        C2x=C2.play()
                        a=time.time()
                    elif e.data2==0:
                        C2x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,24,a-c, duration, volume)
                        i=i+duration
                if e.data1==25:
                    if e.data2 !=0:
                        Db2x=Db2.play()
                        a=time.time()
                    elif e.data2==0:
                        Db2x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,25,a-c, duration, volume)
                        i=i+duration
                if e.data1==26:
                    if e.data2 !=0:
                        D2x=D2.play()
                        a=time.time()
                    elif e.data2==0:
                        D2x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,26,a-c, duration, volume)
                        i=i+duration
                if e.data1==27:
                    if e.data2 !=0:
                        Eb2x=Eb2.play()
                        a=time.time()
                    elif e.data2==0:
                        Eb2x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,27,a-c, duration, volume)
                        i=i+duration
                if e.data1==28:
                    if e.data2 !=0:
                        E2x=E2.play()
                        a=time.time()
                    elif e.data2==0:
                        E2x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,28,a-c, duration, volume)
                        i=i+duration
                if e.data1==29:
                    if e.data2 !=0:
                        F2x=F2.play()
                        a=time.time()
                    elif e.data2==0:
                        F2x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,29,a-c, duration, volume)
                        i=i+duration
                if e.data1==30:
                    if e.data2 !=0:
                        Gb2x=Gb2.play()
                        a=time.time()
                    elif e.data2==0:
                        Gb2x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,30,a-c, duration, volume)
                        i=i+duration
                if e.data1==31:
                    if e.data2 !=0:
                        G2x=G2.play()
                        a=time.time()
                    elif e.data2==0:
                        G2x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,31,a-c, duration, volume)
                        i=i+duration
                if e.data1==32:
                    if e.data2 !=0:
                        Ab2x=Ab2.play()
                        a=time.time()
                    elif e.data2==0:
                        Ab2x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,32,a-c, duration, volume)
                        i=i+duration
                if e.data1==33:
                    if e.data2 !=0:
                        A2x=A2.play()
                        a=time.time()
                    elif e.data2==0:
                        A2x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,33,a-c, duration, volume)
                        i=i+duration
                if e.data1==34:
                    if e.data2 !=0:
                        Bb2x=Bb2.play()
                        a=time.time()
                    elif e.data2==0:
                        Bb2x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,34,a-c, duration, volume)
                        i=i+duration
                if e.data1==35:
                    if e.data2 !=0:
                        B2x=B2.play()
                        a=time.time()
                    elif e.data2==0:
                        B2x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,35,a-c, duration, volume)
                        i=i+duration
                if e.data1==36:
                    if e.data2 !=0:
                        C3x=C3.play()
                        a=time.time()
                    elif e.data2==0:
                        C3x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,36,a-c, duration, volume)
                        i=i+duration
                if e.data1==37:
                    if e.data2 !=0:
                        Db3x=Db3.play()
                        a=time.time()
                    elif e.data2==0:
                        Db3x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,37,a-c, duration, volume)
                        i=i+duration
                if e.data1==38:
                    if e.data2 !=0:
                        D3x=D3.play()
                        a=time.time()
                    elif e.data2==0:
                        D3x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,38,a-c, duration, volume)
                        i=i+duration
                if e.data1==39:
                    if e.data2 !=0:
                        Eb3x=Eb3.play()
                        a=time.time()
                    elif e.data2==0:
                        Eb3x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,39,a-c, duration, volume)
                        i=i+duration
                if e.data1==40:
                    if e.data2 !=0:
                        E3x=E3.play()
                        a=time.time()
                    elif e.data2==0:
                        E3x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,40,a-c, duration, volume)
                        i=i+duration
                if e.data1==41:
                    if e.data2 !=0:
                        F3x=F3.play()
                        a=time.time()
                    elif e.data2==0:
                        F3x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,41,a-c, duration, volume)
                        i=i+duration
                if e.data1==42:
                    if e.data2 !=0:
                        Gb3x=Gb3.play()
                        a=time.time()
                    elif e.data2==0:
                        Gb3x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,42,a-c, duration, volume)
                        i=i+duration
                if e.data1==43:
                    if e.data2 !=0:
                        G3x=G3.play()
                        a=time.time()
                    elif e.data2==0:
                        G3x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,43,a-c, duration, volume)
                        i=i+duration
                if e.data1==44:
                    if e.data2 !=0:
                        Ab3x=Ab3.play()
                        a=time.time()
                    elif e.data2==0:
                        Ab3x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,44,a-c, duration, volume)
                        i=i+duration
                if e.data1==45:
                    if e.data2 !=0:
                        A3x=A3.play()
                        a=time.time()
                    elif e.data2==0:
                        A3x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,45,a-c, duration, volume)
                        i=i+duration
                if e.data1==46:
                    if e.data2 !=0:
                        Bb3x=Bb3.play()
                        a=time.time()
                    elif e.data2==0:
                        Bb3x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,46,a-c, duration, volume)
                        i=i+duration
                if e.data1==47:
                    if e.data2 !=0:
                        B3x=B3.play()
                        a=time.time()
                    elif e.data2==0:
                        B3x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,47,a-c, duration, volume)
                        i=i+duration
                if e.data1==48:
                    if e.data2 !=0:
                        C4x=C4.play()
                        a=time.time()
                    elif e.data2==0:
                        C4x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,48,a-c, duration, volume)
                        i=i+duration
                if e.data1==49:
                    if e.data2 !=0:
                        Db4x=Db4.play()
                        a=time.time()
                    elif e.data2==0:
                        Db4x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,49,a-c, duration, volume)
                        i=i+duration
                if e.data1==50:
                    if e.data2 !=0:
                        D4x=D4.play()
                        a=time.time()
                    elif e.data2==0:
                        D4x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,50,a-c, duration, volume)
                        i=i+duration
                if e.data1==51:
                    if e.data2 !=0:
                        Eb4x=Eb4.play()
                        a=time.time()
                    elif e.data2==0:
                        Eb4x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,51,a-c, duration, volume)
                        i=i+duration
                if e.data1==52:
                    if e.data2 !=0:
                        E4x=E4.play()
                        a=time.time()
                    elif e.data2==0:
                        E4x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,52,a-c, duration, volume)
                        i=i+duration
                if e.data1==53:
                    if e.data2 !=0:
                        F4x=F4.play()
                        a=time.time()
                    elif e.data2==0:
                        F4x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,53,a-c, duration, volume)
                        i=i+duration
                if e.data1==54:
                    if e.data2 !=0:
                        Gb4x=Gb4.play()
                        a=time.time()
                    elif e.data2==0:
                        Gb4x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,54,a-c, duration, volume)
                        i=i+duration
                if e.data1==55:
                    if e.data2 !=0:
                        G4x=G4.play()
                        a=time.time()
                    elif e.data2==0:
                        G4x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,55,a-c, duration, volume)
                        i=i+duration
                if e.data1==56:
                    if e.data2 !=0:
                        Ab4x=Ab4.play()
                        a=time.time()
                    elif e.data2==0:
                        Ab4x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,56,a-c, duration, volume)
                        i=i+duration
                if e.data1==57:
                    if e.data2 !=0:
                        A4x=A4.play()
                        a=time.time()
                    elif e.data2==0:
                        A4x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,57,a-c, duration, volume)
                        i=i+duration
                if e.data1==58:
                    if e.data2 !=0:
                        Bb4x=Bb4.play()
                        a=time.time()
                    elif e.data2==0:
                        Bb4x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,58,a-c, duration, volume)
                        i=i+duration
                if e.data1==59:
                    if e.data2 !=0:
                        B4x=B4.play()
                        a=time.time()
                    elif e.data2==0:
                        B4x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,59,a-c, duration, volume)
                        i=i+duration
                if e.data1==60:
                    if e.data2 !=0:
                        C5x=C5.play()
                        a=time.time()
                    elif e.data2==0:
                        C5x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,60,a-c, duration, volume)
                        i=i+duration
                if e.data1==61:
                    if e.data2 !=0:
                        Db5x=Db5.play()
                        a=time.time()
                    elif e.data2==0:
                        Db5x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,61,a-c, duration, volume)
                        i=i+duration
                if e.data1==62:
                    if e.data2 !=0:
                        D5x=D5.play()
                        a=time.time()
                    elif e.data2==0:
                        D5x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,62,a-c, duration, volume)
                        i=i+duration
                if e.data1==63:
                    if e.data2 !=0:
                        Eb5x=Eb5.play()
                        a=time.time()
                    elif e.data2==0:
                        Eb5x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,63,a-c, duration, volume)
                        i=i+duration
                if e.data1==64:
                    if e.data2 !=0:
                        E5x=E5.play()
                        a=time.time()
                    elif e.data2==0:
                        E5x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,64,a-c, duration, volume)
                        i=i+duration
                if e.data1==65:
                    if e.data2 !=0:
                        F5x=F5.play()
                        a=time.time()
                    elif e.data2==0:
                        F5x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,65,a-c, duration, volume)
                        i=i+duration
                if e.data1==66:
                    if e.data2 !=0:
                        Gb5x=Gb5.play()
                        a=time.time()
                    elif e.data2==0:
                        Gb5x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,66,a-c, duration, volume)
                        i=i+duration
                if e.data1==67:
                    if e.data2 !=0:
                        G5x=G5.play()
                        a=time.time()
                    elif e.data2==0:
                        G5x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,67,a-c, duration, volume)
                        i=i+duration
                if e.data1==68:
                    if e.data2 !=0:
                        Ab5x=Ab5.play()
                        a=time.time()
                    elif e.data2==0:
                        Ab5x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,68,a-c, duration, volume)
                        i=i+duration
                if e.data1==69:
                    if e.data2 !=0:
                        A5x=A5.play()
                        a=time.time()
                    elif e.data2==0:
                        A5x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,69,a-c, duration, volume)
                        i=i+duration
                if e.data1==70:
                    if e.data2 !=0:
                        Bb5x=Bb5.play()
                        a=time.time()
                    elif e.data2==0:
                        Bb5x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,70,a-c, duration, volume)
                        i=i+duration
                if e.data1==71:
                    if e.data2 !=0:
                        B5x=B5.play()
                        a=time.time()
                    elif e.data2==0:
                        B5x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,71,a-c, duration, volume)
                        i=i+duration
                if e.data1==72:
                    if e.data2 !=0:
                        C6x=C6.play()
                        a=time.time()
                    elif e.data2==0:
                        C6x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,72,a-c, duration, volume)
                        i=i+duration
                if e.data1==73:
                    if e.data2 !=0:
                        Db6x=Db6.play()
                        a=time.time()
                    elif e.data2==0:
                        Db6x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,73,a-c, duration, volume)
                        i=i+duration
                if e.data1==74:
                    if e.data2 !=0:
                        D6x=D6.play()
                        a=time.time()
                    elif e.data2==0:
                        D6x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,74,a-c, duration, volume)
                        i=i+duration
                if e.data1==75:
                    if e.data2 !=0:
                        Eb6x=Eb6.play()
                        a=time.time()
                    elif e.data2==0:
                        Eb6x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,75,a-c, duration, volume)
                        i=i+duration
                if e.data1==76:
                    if e.data2 !=0:
                        E6x=E6.play()
                        a=time.time()
                    elif e.data2==0:
                        E6x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,76,a-c, duration, volume)
                        i=i+duration
                if e.data1==77:
                    if e.data2 !=0:
                        F6x=F6.play()
                        a=time.time()
                    elif e.data2==0:
                        F6x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,77,a-c, duration, volume)
                        i=i+duration
                if e.data1==78:
                    if e.data2 !=0:
                        Gb6x=Gb6.play()
                        a=time.time()
                    elif e.data2==0:
                        Gb6x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,78,a-c, duration, volume)
                        i=i+duration
                if e.data1==79:
                    if e.data2 !=0:
                        G6x=G6.play()
                        a=time.time()
                    elif e.data2==0:
                        G6x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,79,a-c, duration, volume)
                        i=i+duration
                if e.data1==80:
                    if e.data2 !=0:
                        Ab6x=Ab6.play()
                        a=time.time()
                    elif e.data2==0:
                        Ab6x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,80,a-c, duration, volume)
                        i=i+duration
                if e.data1==81:
                    if e.data2 !=0:
                        A6x=A6.play()
                        a=time.time()
                    elif e.data2==0:
                        A6x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,81,a-c, duration, volume)
                        i=i+duration
                if e.data1==82:
                    if e.data2 !=0:
                        Bb6x=Bb6.play()
                        a=time.time()
                    elif e.data2==0:
                        Bb6x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,82,a-c, duration, volume)
                        i=i+duration
                if e.data1==83:
                    if e.data2 !=0:
                        B6x=B6.play()
                        a=time.time()
                    elif e.data2==0:
                        B6x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,83,a-c, duration, volume)
                        i=i+duration
                if e.data1==84:
                    if e.data2 !=0:
                        C7x=C7.play()
                        a=time.time()
                    elif e.data2==0:
                        C7x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,84,a-c, duration, volume)
                        i=i+duration
                if e.data1==85:
                    if e.data2 !=0:
                        Db7x=Db7.play()
                        a=time.time()
                    elif e.data2==0:
                        Db7x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,85,a-c, duration, volume)
                        i=i+duration
                if e.data1==86:
                    if e.data2 !=0:
                        D7x=D7.play()
                        a=time.time()
                    elif e.data2==0:
                        D7x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,86,a-c, duration, volume)
                        i=i+duration
                if e.data1==87:
                    if e.data2 !=0:
                        Eb7x=Eb7.play()
                        a=time.time()
                    elif e.data2==0:
                        Eb7x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,87,a-c, duration, volume)
                        i=i+duration
                if e.data1==88:
                    if e.data2 !=0:
                        E7x=E7.play()
                        a=time.time()
                    elif e.data2==0:
                        E7x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,88,a-c, duration, volume)
                        i=i+duration
                if e.data1==89:
                    if e.data2 !=0:
                        F7x=F7.play()
                        a=time.time()
                    elif e.data2==0:
                        F7x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,89,a-c, duration, volume)
                        i=i+duration
                if e.data1==90:
                    if e.data2 !=0:
                        Gb7x=Gb7.play()
                        a=time.time()
                    elif e.data2==0:
                        Gb7x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,90,a-c, duration, volume)
                        i=i+duration
                if e.data1==91:
                    if e.data2 !=0:
                        G7x=G7.play()
                        a=time.time()
                    elif e.data2==0:
                        G7x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,91,a-c, duration, volume)
                        i=i+duration
                if e.data1==92:
                    if e.data2 !=0:
                        Ab7x=Ab7.play()
                        a=time.time()
                    elif e.data2==0:
                        Ab7x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,92,a-c, duration, volume)
                        i=i+duration
                if e.data1==93:
                    if e.data2 !=0:
                        A7x=A7.play()
                        a=time.time()
                    elif e.data2==0:
                        A7x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,93,a-c, duration, volume)
                        i=i+duration
                if e.data1==94:
                    if e.data2 !=0:
                        Bb7x=Bb7.play()
                        a=time.time()
                    elif e.data2==0:
                        Bb7x.stop()
                        b=time.time()
                        t=b-a
                        duration=(t*60)/tempo
                        MyMIDI.addNote(track,channel,94,a-c, duration, volume)
                        i=i+duration

        if i2.poll():
            midi_events = i2.read(10)
            # convert them into pygame events.
            midi_evs = pygame.midi.midis2events(midi_events, i2.device_id)

            for m_e in midi_evs:
                event_post( m_e )




