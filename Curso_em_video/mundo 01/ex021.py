# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame

pygame.mixer.init() 
pygame.mixer.music.load('python/Curso_em_video/audios/If I Could Fly.mp3') 
pygame.mixer.music.play()  # Toca a música

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

