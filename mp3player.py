# -*- coding: utf-8 -*-
"""
Mp3 Player por Douglas Magalhães de Oliveira

""" 

"""Importar módulos"""
import pygame
import tkinter as tkr

"""Criar a janela"""
player= tkr.Tk()

"""Editar a janela"""
player.title("Audio Player")
player.geometry("205x340")

"""Ir a música"""
file = "03 - Words Of Wisdom.mp3"

"""Evento de ações"""
def Play():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    
def ExitPlayer():
    pygame.mixer.music.stop()

"""Registro os botões"""
button1 = tkr.Button(player,width=5, height=3, text="Tocar",comando=Play) 
button1.pack(fill="x")
button2 = tkr.Button(player,width=5, height=3, text="Parar",comando=ExitPlayer) 
button2.pack(fill="x")

"""Nome da música"""
label1 = tkr.LabelFrame(player, text="Musica")
label1.pack(fill="both", expand="yes")
contents1 = tkr.Label(label1, text = file)
contents1.pack()    

"""Ativar"""
player.mainloop()
""""""
