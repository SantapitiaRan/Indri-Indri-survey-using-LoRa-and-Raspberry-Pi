#!/usr/bin/python3
# compare.py
import os
from correlation import correlate
import pickle
dict_recording_conter=dict()
dict_FeoAla_conter=dict()
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

with open('/opt/audio-compare-master/Dictionnaire/dict_recording_conter.pkl', 'rb') as fp:
    dict_recording_conter = pickle.load(fp)
recording_conter = dict_recording_conter.get("recording_conter")

with open('/opt/audio-compare-master/Dictionnaire/dict_FeoAla_conter.pkl', 'rb') as fp:
    dict_FeoAla_conter = pickle.load(fp)
FeoAla_conter = dict_FeoAla_conter.get("FeoAla_conter")
if FeoAla_conter <= recording_conter:
    nametarget = 'IndriIndri'+str(FeoAla_conter)
    Target_file= '/opt/audio-compare-master/FeoAla/%s.wav'%(nametarget)
    for key in List_Indri: 
    #SOURCE_FILE ="Audio/"+son(i)+".mp3"
        SOURCE_FILE = "VocalDataBaseIndriIndri/%s.wav"%(key)
        TARGET_FILE = Target_file
        SON= key
        NAME_TARGET = nametarget
        correlate(SOURCE_FILE, TARGET_FILE, SON, NAME_TARGET)
    FeoAla_conter += 1
    dict_FeoAla_conter["FeoAla_conter"] = FeoAla_conter 
    with open('/opt/audio-compare-master/Dictionnaire/dict_FeoAla_conter.pkl', 'wb') as fp:
        pickle.dump(dict_FeoAla_conter, fp)
else:
    print("Miandry Donnée vaovao")

