

import pygame
from pygame.locals import *
from pygame import*
import simpleaudio as sa
from midiutil import*
import pygame.midi
from time import*
import time

    ################### Musique #######################
 
def debut():
    print("salut")
    #debut=time.time()
def fin():
    fin=time.time()
    duration=fin-debut
def son_music2(a,instrument):
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


    device_id=a
    pygame.init()
    pygame.fastevent.init()
    event_get = pygame.fastevent.get
    event_post = pygame.fastevent.post

    

    


    if device_id is None:
        input_id = pygame.midi.get_default_input_id()
    else:
        input_id = device_id

    
    i = pygame.midi.Input( input_id )

    



    going = True
    x=0
    

    
    while going:
        sleep(0.03)
        
        
        for e in event_get():
            

            
                    
            event=e
            
            #Octave
            if e.type == KEYDOWN and e.key == K_KP_PLUS and octave!=6:
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


                
                 
            if e.type == KEYUP and e.key == K_KP_MINUS and octave!=1:
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
            if e.type == QUIT:
                going=0
                pygame.quit()
            

            if e.type == KEYDOWN and e.key == 256:
                a0.play()
            if e.type == KEYDOWN and e.key == 257:
                a1.play()
            if e.type == KEYDOWN and e.key == 258:
                a2.play()
            if e.type == KEYDOWN and e.key == 259:
                a3.play()
            if e.type == KEYDOWN and e.key == 260:
                a4.play()
            if e.type == KEYDOWN and e.key == 261:
                a5.play()
            if e.type == KEYDOWN and e.key == 262:
                a6.play()
            if e.type == KEYDOWN and e.key == 263:
                a7.play()
            if e.type == KEYDOWN and e.key == 264:
                a8.play()
            if e.type == KEYDOWN and e.key == 265:
                a9.play()
            
            #Do
            if e.type == KEYDOWN and e.key == K_a:
                Dox=Do.play()
                
                      
                

            if e.type == KEYUP and e.key == K_a:
                Dox.stop()
                
                
           
                

            #ReMin
            if e.type == KEYDOWN and e.key == K_w:
                ReMinx=ReMin.play()
                
            if e.type == KEYUP and e.key == K_w:
                ReMinx.stop()
                

            #Re
            if e.type == KEYDOWN and e.key == K_s:
                Rex=Re.play()
                
            if e.type == KEYUP and e.key == K_s:
                Rex.stop()
                

            #MiMin
            if e.type == KEYDOWN and e.key == K_e:
                MiMinx=MiMin.play()
                
            if e.type == KEYUP and e.key == K_e:
                MiMinx.stop()
                

            #Mi
            if e.type == KEYDOWN and e.key == K_d:
                Mix=Mi.play()
                
            if e.type == KEYUP and e.key == K_d:
                Mix.stop()
                

            #Fa
            if e.type == KEYDOWN and e.key == K_f:
                Fax=Fa.play()
                
            if e.type == KEYUP and e.key == K_f:
                Fax.stop()
                

            #SolMin         
            if e.type == KEYDOWN and e.key == K_t:
                SolMinx=SolMin.play()
                
            if e.type == KEYUP and e.key == K_t:
                SolMinx.stop()
               

            #Sol
            if e.type == KEYDOWN and e.key == K_g:
                Solx=Sol.play()
                
            if e.type == KEYUP and e.key == K_g:
                Solx.stop()
                

            #LaMin
            if e.type == KEYDOWN and e.key == K_y:
                LaMinx=LaMin.play()
                
            if e.type == KEYUP and e.key == K_y:
                LaMinx.stop()
               

            #La
            if e.type == KEYDOWN and e.key == K_h:
                Lax=La.play()
                
            if e.type == KEYUP and e.key == K_h:
                Lax.stop()
                

            #SiMin
            if e.type == KEYDOWN and e.key == K_u:
                SiMinx=SiMin.play()
                
            if e.type == KEYUP and e.key == K_u:
                SiMinx.stop()
                

            #Si
            if e.type == KEYDOWN and e.key == K_j:
                Six=Si.play()
                
            if e.type == KEYUP and e.key == K_j:
                Six.stop()
                

            #Do2
            if e.type == KEYDOWN and e.key == K_k:
                Do2x=Do2.play()
                
            if e.type == KEYUP and e.key == K_k:
                Do2x.stop()
                

            #ReMin2
            if e.type == KEYDOWN and e.key == K_o:
                ReMin2x=ReMin2.play()
                
            if e.type == KEYUP and e.key == K_o:
                ReMin2x.stop()
                

            #Re2
            if e.type == KEYDOWN and e.key == K_l:
                Re2x=Re2.play()
                
            if e.type == KEYUP and e.key == K_l:
                Re2x.stop()
                

            #MiMin2
            if e.type == KEYDOWN and e.key == K_p:
                MiMin2x=MiMin2.play()
               
            if e.type == KEYUP and e.key == K_p:
                MiMin2x.stop()
                

            #Mi2
            if e.type == KEYDOWN and e.key == K_SEMICOLON:
                Mi2x=Mi2.play()
                
            if e.type == KEYUP and e.key == K_SEMICOLON:
                Mi2x.stop()
                

            if e.type == KEYDOWN and e.key == K_QUOTE:
                Fa2x=Fa2.play()
                
            if e.type == KEYUP and e.key == K_QUOTE:
                Fa2x.stop()
                
        

            if e.type == KEYDOWN and e.key == K_RIGHTBRACKET:
                SolMin2x=SolMin2.play()
                
            if e.type == KEYUP and e.key == K_RIGHTBRACKET:
                SolMin2x.stop()
                

            if e.type == KEYDOWN and e.key == K_BACKSLASH:
                Sol2x=Sol2.play()
                
            if e.type == KEYUP and e.key == K_BACKSLASH:
                Sol2x.stop()
     
            if e.type in [pygame.midi.MIDIIN]:
                               

                if e.data1==12:
                    if e.data2 !=0:
                        C1x=C1.play()
                    elif e.data2==0:
                        C1x.stop()
                if e.data1==13:
                    if e.data2 !=0:
                        Db1x=Db1.play()
                    elif e.data2==0:
                        Db1x.stop()
                if e.data1==14:
                    if e.data2 !=0:
                        D1x=D1.play()
                    elif e.data2==0:
                        D1x.stop()
                if e.data1==15:
                    if e.data2 !=0:
                        Eb1x=Eb1.play()
                    elif e.data2==0:
                        Eb1x.stop()
                if e.data1==16:
                    if e.data2 !=0:
                        E1x=E1.play()
                    elif e.data2==0:
                        E1x.stop()
                if e.data1==17:
                    if e.data2 !=0:
                        F1x=F1.play()
                    elif e.data2==0:
                        F1x.stop()
                if e.data1==18:
                    if e.data2 !=0:
                        Gb1x=Gb1.play()
                    elif e.data2==0:
                        Gb1x.stop()
                if e.data1==19:
                    if e.data2 !=0:
                        G1x=G1.play()
                    elif e.data2==0:
                        G1x.stop()
                if e.data1==20:
                    if e.data2 !=0:
                        Ab1x=Ab1.play()
                    elif e.data2==0:
                        Ab1x.stop()
                if e.data1==21:
                    if e.data2 !=0:
                        A1x=A1.play()
                    elif e.data2==0:
                        A1x.stop()
                if e.data1==22:
                    if e.data2 !=0:
                        Bb1x=Bb1.play()
                    elif e.data2==0:
                        Bb1x.stop()
                if e.data1==23:
                    if e.data2 !=0:
                        B1x=B1.play()
                    elif e.data2==0:
                        B1x.stop()
                if e.data1==24:
                    if e.data2 !=0:
                        C2x=C2.play()
                    elif e.data2==0:
                        C2x.stop()
                if e.data1==25:
                    if e.data2 !=0:
                        Db2x=Db2.play()
                    elif e.data2==0:
                        Db2x.stop()
                if e.data1==26:
                    if e.data2 !=0:
                        D2x=D2.play()
                    elif e.data2==0:
                        D2x.stop()
                if e.data1==27:
                    if e.data2 !=0:
                        Eb2x=Eb2.play()
                    elif e.data2==0:
                        Eb2x.stop()
                if e.data1==28:
                    if e.data2 !=0:
                        E2x=E2.play()
                    elif e.data2==0:
                        E2x.stop()
                if e.data1==29:
                    if e.data2 !=0:
                        F2x=F2.play()
                    elif e.data2==0:
                        F2x.stop()
                if e.data1==30:
                    if e.data2 !=0:
                        Gb2x=Gb2.play()
                    elif e.data2==0:
                        Gb2x.stop()
                if e.data1==31:
                    if e.data2 !=0:
                        G2x=G2.play()
                    elif e.data2==0:
                        G2x.stop()
                if e.data1==32:
                    if e.data2 !=0:
                        Ab2x=Ab2.play()
                    elif e.data2==0:
                        Ab2x.stop()
                if e.data1==33:
                    if e.data2 !=0:
                        A2x=A2.play()
                    elif e.data2==0:
                        A2x.stop()
                if e.data1==34:
                    if e.data2 !=0:
                        Bb2x=Bb2.play()
                    elif e.data2==0:
                        Bb2x.stop()
                if e.data1==35:
                    if e.data2 !=0:
                        B2x=B2.play()
                    elif e.data2==0:
                        B2x.stop()
                if e.data1==36:
                    if e.data2 !=0:
                        C3x=C3.play()
                    elif e.data2==0:
                        C3x.stop()
                if e.data1==37:
                    if e.data2 !=0:
                        Db3x=Db3.play()
                    elif e.data2==0:
                        Db3x.stop()
                if e.data1==38:
                    if e.data2 !=0:
                        D3x=D3.play()
                    elif e.data2==0:
                        D3x.stop()
                if e.data1==39:
                    if e.data2 !=0:
                        Eb3x=Eb3.play()
                    elif e.data2==0:
                        Eb3x.stop()
                if e.data1==40:
                    if e.data2 !=0:
                        E3x=E3.play()
                    elif e.data2==0:
                        E3x.stop()
                if e.data1==41:
                    if e.data2 !=0:
                        F3x=F3.play()
                    elif e.data2==0:
                        F3x.stop()
                if e.data1==42:
                    if e.data2 !=0:
                        Gb3x=Gb3.play()
                    elif e.data2==0:
                        Gb3x.stop()
                if e.data1==43:
                    if e.data2 !=0:
                        G3x=G3.play()
                    elif e.data2==0:
                        G3x.stop()
                if e.data1==44:
                    if e.data2 !=0:
                        Ab3x=Ab3.play()
                    elif e.data2==0:
                        Ab3x.stop()
                if e.data1==45:
                    if e.data2 !=0:
                        A3x=A3.play()
                    elif e.data2==0:
                        A3x.stop()
                if e.data1==46:
                    if e.data2 !=0:
                        Bb3x=Bb3.play()
                    elif e.data2==0:
                        Bb3x.stop()
                if e.data1==47:
                    if e.data2 !=0:
                        B3x=B3.play()
                    elif e.data2==0:
                        B3x.stop()
                if e.data1==48:
                    if e.data2 !=0:
                        C4x=C4.play()
                    elif e.data2==0:
                        C4x.stop()
                if e.data1==49:
                    if e.data2 !=0:
                        Db4x=Db4.play()
                    elif e.data2==0:
                        Db4x.stop()
                if e.data1==50:
                    if e.data2 !=0:
                        D4x=D4.play()
                    elif e.data2==0:
                        D4x.stop()
                if e.data1==51:
                    if e.data2 !=0:
                        Eb4x=Eb4.play()
                    elif e.data2==0:
                        Eb4x.stop()
                if e.data1==52:
                    if e.data2 !=0:
                        E4x=E4.play()
                    elif e.data2==0:
                        E4x.stop()
                if e.data1==53:
                    if e.data2 !=0:
                        F4x=F4.play()
                    elif e.data2==0:
                        F4x.stop()
                if e.data1==54:
                    if e.data2 !=0:
                        Gb4x=Gb4.play()
                    elif e.data2==0:
                        Gb4x.stop()
                if e.data1==55:
                    if e.data2 !=0:
                        G4x=G4.play()
                    elif e.data2==0:
                        G4x.stop()
                if e.data1==56:
                    if e.data2 !=0:
                        Ab4x=Ab4.play()
                    elif e.data2==0:
                        Ab4x.stop()
                if e.data1==57:
                    if e.data2 !=0:
                        A4x=A4.play()
                    elif e.data2==0:
                        A4x.stop()
                if e.data1==58:
                    if e.data2 !=0:
                        Bb4x=Bb4.play()
                    elif e.data2==0:
                        Bb4x.stop()
                if e.data1==59:
                    if e.data2 !=0:
                        B4x=B4.play()
                    elif e.data2==0:
                        B4x.stop()
                if e.data1==60:
                    if e.data2 !=0:
                        C5x=C5.play()
                    elif e.data2==0:
                        C5x.stop()
                if e.data1==61:
                    if e.data2 !=0:
                        Db5x=Db5.play()
                    elif e.data2==0:
                        Db5x.stop()
                if e.data1==62:
                    if e.data2 !=0:
                        D5x=D5.play()
                    elif e.data2==0:
                        D5x.stop()
                if e.data1==63:
                    if e.data2 !=0:
                        Eb5x=Eb5.play()
                    elif e.data2==0:
                        Eb5x.stop()
                if e.data1==64:
                    if e.data2 !=0:
                        E5x=E5.play()
                    elif e.data2==0:
                        E5x.stop()
                if e.data1==65:
                    if e.data2 !=0:
                        F5x=F5.play()
                    elif e.data2==0:
                        F5x.stop()
                if e.data1==66:
                    if e.data2 !=0:
                        Gb5x=Gb5.play()
                    elif e.data2==0:
                        Gb5x.stop()
                if e.data1==67:
                    if e.data2 !=0:
                        G5x=G5.play()
                    elif e.data2==0:
                        G5x.stop()
                if e.data1==68:
                    if e.data2 !=0:
                        Ab5x=Ab5.play()
                    elif e.data2==0:
                        Ab5x.stop()
                if e.data1==69:
                    if e.data2 !=0:
                        A5x=A5.play()
                    elif e.data2==0:
                        A5x.stop()
                if e.data1==70:
                    if e.data2 !=0:
                        Bb5x=Bb5.play()
                    elif e.data2==0:
                        Bb5x.stop()
                if e.data1==71:
                    if e.data2 !=0:
                        B5x=B5.play()
                    elif e.data2==0:
                        B5x.stop()
                if e.data1==72:
                    if e.data2 !=0:
                        C6x=C6.play()
                    elif e.data2==0:
                        C6x.stop()
                if e.data1==73:
                    if e.data2 !=0:
                        Db6x=Db6.play()
                    elif e.data2==0:
                        Db6x.stop()
                if e.data1==74:
                    if e.data2 !=0:
                        D6x=D6.play()
                    elif e.data2==0:
                        D6x.stop()
                if e.data1==75:
                    if e.data2 !=0:
                        Eb6x=Eb6.play()
                    elif e.data2==0:
                        Eb6x.stop()
                if e.data1==76:
                    if e.data2 !=0:
                        E6x=E6.play()
                    elif e.data2==0:
                        E6x.stop()
                if e.data1==77:
                    if e.data2 !=0:
                        F6x=F6.play()
                    elif e.data2==0:
                        F6x.stop()
                if e.data1==78:
                    if e.data2 !=0:
                        Gb6x=Gb6.play()
                    elif e.data2==0:
                        Gb6x.stop()
                if e.data1==79:
                    if e.data2 !=0:
                        G6x=G6.play()
                    elif e.data2==0:
                        G6x.stop()
                if e.data1==80:
                    if e.data2 !=0:
                        Ab6x=Ab6.play()
                    elif e.data2==0:
                        Ab6x.stop()
                if e.data1==81:
                    if e.data2 !=0:
                        A6x=A6.play()
                    elif e.data2==0:
                        A6x.stop()
                if e.data1==82:
                    if e.data2 !=0:
                        Bb6x=Bb6.play()
                    elif e.data2==0:
                        Bb6x.stop()
                if e.data1==83:
                    if e.data2 !=0:
                        B6x=B6.play()
                    elif e.data2==0:
                        B6x.stop()
                if e.data1==84:
                    if e.data2 !=0:
                        C7x=C7.play()
                    elif e.data2==0:
                        C7x.stop()
                if e.data1==85:
                    if e.data2 !=0:
                        Db7x=Db7.play()
                    elif e.data2==0:
                        Db7x.stop()
                if e.data1==86:
                    if e.data2 !=0:
                        D7x=D7.play()
                    elif e.data2==0:
                        D7x.stop()
                if e.data1==87:
                    if e.data2 !=0:
                        Eb7x=Eb7.play()
                    elif e.data2==0:
                        Eb7x.stop()
                if e.data1==88:
                    if e.data2 !=0:
                        E7x=E7.play()
                    elif e.data2==0:
                        E7x.stop()
                if e.data1==89:
                    if e.data2 !=0:
                        F7x=F7.play()
                    elif e.data2==0:
                        F7x.stop()
                if e.data1==90:
                    if e.data2 !=0:
                        Gb7x=Gb7.play()
                    elif e.data2==0:
                        Gb7x.stop()
                if e.data1==91:
                    if e.data2 !=0:
                        G7x=G7.play()
                    elif e.data2==0:
                        G7x.stop()
                if e.data1==92:
                    if e.data2 !=0:
                        Ab7x=Ab7.play()
                    elif e.data2==0:
                        Ab7x.stop()
                if e.data1==93:
                    if e.data2 !=0:
                        A7x=A7.play()
                    elif e.data2==0:
                        A7x.stop()
                if e.data1==94:
                    if e.data2 !=0:
                        Bb7x=Bb7.play()
                    elif e.data2==0:
                        Bb7x.stop()

            

                                
                

                    
               
        if i.poll():
            midi_events = i.read(10)
            # convert them into pygame events.
            midi_evs = pygame.midi.midis2events(midi_events, i.device_id)

            for m_e in midi_evs:
                event_post( m_e )


    
    


                
                    






                
                

                

                

                
                








    




        











