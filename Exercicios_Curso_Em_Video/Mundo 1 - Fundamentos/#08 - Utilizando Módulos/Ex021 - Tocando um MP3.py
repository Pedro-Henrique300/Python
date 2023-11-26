#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame

pygame.init()
pygame.mixer.music.load('Ex021.mp3') # Deixando o arquivo no mesmo local que o código apenas copie examente o nome do arquivo.
pygame.mixer.music.play()
pygame.event.wait()

