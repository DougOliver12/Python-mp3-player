# -*- coding: utf-8 -*-
"""
Mp3 Player por Douglas Magalhães de Oliveira
"""

"""Importar módulos"""
import pygame
import tkinter as tkr
import os

"""Criar a janela"""
player = tkr.Tk()

"""Editar a janela"""
player.title("Audio Player")
player.geometry("205x340")

"""Registro da Playlist"""
os.chdir("/home/doug/PycharmProjects")
print(os.getcwd)
songlist = os.listdir()

"""Controle de volume"""
VolumeLevel = tkr.Scale(player, from_=0.0, to_=1.0, orient=tkr.HORIZONTAL, resolution=0.1)

"""Entradas da Playlist"""
playlist = tkr.Listbox(player, highlightcolor="blue", selectmode=tkr.SINGLE)
print(songlist)
for item in songlist:
    pos = 0
    playlist.insert(pos, item)
    pos = pos + 1

"""Pygame init"""
pygame.init()
pygame.mixer.init()

"""Funções"""
def Play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(VolumeLevel.get())
    print(pygame.mixer.music.get_volume())
    print(VolumeLevel.get())
def ExitPlayer():
    pygame.mixer.music.stop()

def Pause():
    pygame.mixer.music.pause()

def UnPause():
    pygame.mixer.music.unpause()

"""Registro os botões"""
button1 = tkr.Button(player, width=5, height=3, text="Tocar", command=Play)
button2 = tkr.Button(player, width=5, height=3, text="Parar", command=ExitPlayer)
button3 = tkr.Button(player, width=5, height=3, text="Pausar", command=Pause)
button4 = tkr.Button(player, width=5, height=3, text="Continuar", command=UnPause)

"""Nome da música"""
var = tkr.StringVar()
soungtitle1 = tkr.Label(player, textvariable=var)

"""Local das widgets"""
button1.pack(fill="x")
button2.pack(fill="x")
button3.pack(fill="x")
button4.pack(fill="x")
VolumeLevel.pack(fill="x")
soungtitle1.pack()
playlist.pack(fill="both", expand="yes")

"""Ativar"""
player.mainloop()
""""""
