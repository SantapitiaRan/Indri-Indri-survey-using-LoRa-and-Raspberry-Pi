#!/usr/bin/python3
# compare.py
import os
from correlation import correlate
a="Territory marking T18_playback of a song_not real one"
b="Territory marking T18 I1_song advertisement 1"
c="Territory marking T15_song advertisement 1"
d="Territory marking T15_song advertisement 2"
e="Indri's territory marking T14_song advertisement 1"
f="Indri's territory marking T14_song advertisement 2"
g="Indri's Territory marking or loss T15 I3_song advertisement 1"
h="Indri's alerting 3rd stage T15 I1, 13_roar alarm+song 1"
i="Indri's alerting 3rd stage T15 I1, 13Indri's alerting 3rd stage T15 I1, 13_roar alarm+song 2"
j="Indri's alerting 2nd stage_honk"
k="Territory marking T18 I1_song advertisement 2"
List_Indri=[a,b,c,d,e,f,g,h,i,j,k]
Target_file= input('Veulliez entrer le nom du fichier audio a comparer dans le dossier AudioTest: ')
Target_file="AudioTest/%s.wav"%(Target_file)
for key in List_Indri: 
  #SOURCE_FILE ="Audio/"+son(i)+".mp3"
  SOURCE_FILE = "VocalDataBaseIndriIndri/%s.wav"%(key)
  TARGET_FILE = Target_file
  SON= key
  nametarget="Test"
  correlate(SOURCE_FILE, TARGET_FILE, SON, nametarget)
