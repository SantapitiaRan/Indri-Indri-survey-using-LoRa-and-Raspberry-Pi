import pickle
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
dict_Comparaison=dict()
dict_Comparaison={str(a):0,str(b):0,str(c):0,str(d):0,str(e):0,str(f):0,str(g):0,str(h):0,str(i):0,str(j):0,str(k):0}
with open('/home/santapitia/Desktop/audio-compare-master/Dictionnaire/dict_Comparaison.pkl', 'wb') as fp:
        pickle.dump(dict_Comparaison, fp)
        print(dict_Comparaison)
