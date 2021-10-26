

import pygame
from pygame.locals import *
from pygame import*
import simpleaudio as sa
from midiutil import*
import time

    ################### Musique #######################
 
def debut():
    print("salut")
    #debut=time.time()
def fin():
    fin=time.time()
    duration=fin-debut
def son_music3(octave,instrument):
    
    


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
    a0=sa.WaveObject.from_wave_file("drum_rack/0.wav")
    a1=sa.WaveObject.from_wave_file("drum_rack/1.wav")
    a2=sa.WaveObject.from_wave_file("drum_rack/2.wav")
    a3=sa.WaveObject.from_wave_file("drum_rack/3.wav")
    a4=sa.WaveObject.from_wave_file("drum_rack/4.wav")
    a5=sa.WaveObject.from_wave_file("drum_rack/5.wav")
    a6=sa.WaveObject.from_wave_file("drum_rack/6.wav")
    a7=sa.WaveObject.from_wave_file("drum_rack/7.wav")
    a8=sa.WaveObject.from_wave_file("drum_rack/8.wav")
    a9=sa.WaveObject.from_wave_file("drum_rack/9.wav")



    while continuer==1:
        time.sleep(0.003)
        for e in pygame.event.get():
            event=e
               
            


            
            #Octave
            if event.type == KEYDOWN and event.key == K_KP_PLUS and octave!=6:
                octave=octave+1
                
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
                continuer=0
                pygame.quit()
            

            if event.type == KEYDOWN and event.key == 256:
                a0.play()
            if event.type == KEYDOWN and event.key == 257:
                a1.play()
            if event.type == KEYDOWN and event.key == 258:
                a2.play()
            if event.type == KEYDOWN and event.key == 259:
                a3.play()
            if event.type == KEYDOWN and event.key == 260:
                a4.play()
            if event.type == KEYDOWN and event.key == 261:
                a5.play()
            if event.type == KEYDOWN and event.key == 262:
                a6.play()
            if event.type == KEYDOWN and event.key == 263:
                a7.play()
            if event.type == KEYDOWN and event.key == 264:
                a8.play()
            if event.type == KEYDOWN and event.key == 265:
                a9.play()

            #Do
            if event.type == KEYDOWN and event.key == K_a:
                Dox=Do.play()
                
                      
                

            if event.type == KEYUP and event.key == K_a:
                Dox.stop()
                
                
           
                

            #ReMin
            if event.type == KEYDOWN and event.key == K_w:
                ReMinx=ReMin.play()
                
            if event.type == KEYUP and event.key == K_w:
                ReMinx.stop()
                

            #Re
            if event.type == KEYDOWN and event.key == K_s:
                Rex=Re.play()
                
            if event.type == KEYUP and event.key == K_s:
                Rex.stop()
                

            #MiMin
            if event.type == KEYDOWN and event.key == K_e:
                MiMinx=MiMin.play()
                
            if event.type == KEYUP and event.key == K_e:
                MiMinx.stop()
                

            #Mi
            if event.type == KEYDOWN and event.key == K_d:
                Mix=Mi.play()
                
            if event.type == KEYUP and event.key == K_d:
                Mix.stop()
                

            #Fa
            if event.type == KEYDOWN and event.key == K_f:
                Fax=Fa.play()
                
            if event.type == KEYUP and event.key == K_f:
                Fax.stop()
                

            #SolMin         
            if event.type == KEYDOWN and event.key == K_t:
                SolMinx=SolMin.play()
                
            if event.type == KEYUP and event.key == K_t:
                SolMinx.stop()
               

            #Sol
            if event.type == KEYDOWN and event.key == K_g:
                Solx=Sol.play()
                
            if event.type == KEYUP and event.key == K_g:
                Solx.stop()
                

            #LaMin
            if event.type == KEYDOWN and event.key == K_y:
                LaMinx=LaMin.play()
                
            if event.type == KEYUP and event.key == K_y:
                LaMinx.stop()
               

            #La
            if event.type == KEYDOWN and event.key == K_h:
                Lax=La.play()
                
            if event.type == KEYUP and event.key == K_h:
                Lax.stop()
                

            #SiMin
            if event.type == KEYDOWN and event.key == K_u:
                SiMinx=SiMin.play()
                
            if event.type == KEYUP and event.key == K_u:
                SiMinx.stop()
                

            #Si
            if event.type == KEYDOWN and event.key == K_j:
                Six=Si.play()
                
            if event.type == KEYUP and event.key == K_j:
                Six.stop()
                

            #Do2
            if event.type == KEYDOWN and event.key == K_k:
                Do2x=Do2.play()
                
            if event.type == KEYUP and event.key == K_k:
                Do2x.stop()
                

            #ReMin2
            if event.type == KEYDOWN and event.key == K_o:
                ReMin2x=ReMin2.play()
                
            if event.type == KEYUP and event.key == K_o:
                ReMin2x.stop()
                

            #Re2
            if event.type == KEYDOWN and event.key == K_l:
                Re2x=Re2.play()
                
            if event.type == KEYUP and event.key == K_l:
                Re2x.stop()
                

            #MiMin2
            if event.type == KEYDOWN and event.key == K_p:
                MiMin2x=MiMin2.play()
               
            if event.type == KEYUP and event.key == K_p:
                MiMin2x.stop()
                

            #Mi2
            if event.type == KEYDOWN and event.key == K_SEMICOLON:
                Mi2x=Mi2.play()
                
            if event.type == KEYUP and event.key == K_SEMICOLON:
                Mi2x.stop()
                

            if event.type == KEYDOWN and event.key == K_QUOTE:
                Fa2x=Fa2.play()
                
            if event.type == KEYUP and event.key == K_QUOTE:
                Fa2x.stop()
                
        

            if event.type == KEYDOWN and event.key == K_RIGHTBRACKET:
                SolMin2x=SolMin2.play()
                
            if event.type == KEYUP and event.key == K_RIGHTBRACKET:
                SolMin2x.stop()
                

            if event.type == KEYDOWN and event.key == K_BACKSLASH:
                Sol2x=Sol2.play()
                
            if event.type == KEYUP and event.key == K_BACKSLASH:
                Sol2x.stop()
                
            if event.type == KEYDOWN and event.key == K_v:
                continuer=0











            
                

                

                

                





    




        











