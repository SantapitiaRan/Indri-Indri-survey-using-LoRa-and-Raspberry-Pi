#!/usr/bin/python3

# correlation.py
import subprocess
import numpy
import pickle
import os
from RecolteDonne import Recolte 
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
# seconds to sample audio file for
sample_time = 30
# number of points to scan cross correlation over
span = 200
# step size (in points) of cross correlation
step = 1
# minimum number of points that must overlap in cross correlation
# exception is raised if this cannot be met
min_overlap = 20
# report match when cross correlation has a peak exceeding threshold
threshold = 0.5

# calculate fingerprint
# Generate file.mp3.fpcalc by "fpcalc -raw -length 500 file.mp3"
def calculate_fingerprints(filename):
    if os.path.exists(filename + '.fpcalc'):
        print("Found precalculated fingerprint for %s" % (filename))
        f = open(filename + '.fpcalc', "r")
        fpcalc_out = ''.join(f.readlines())
        f.close()
    else:
        print("Calculating fingerprint by fpcalc for %s" % (filename))
        fpcalc_out = str(subprocess.check_output(['fpcalc', '-raw', '-length', str(sample_time), filename])).strip().replace('\\n', '').replace("'", "")

    fingerprint_index = fpcalc_out.find('FINGERPRINT=') + 12
    # convert fingerprint to list of integers
    fingerprints = list(map(int, fpcalc_out[fingerprint_index:].split(',')))
    
    return fingerprints
  
# returns correlation between lists
def correlation(listx, listy):
    if len(listx) == 0 or len(listy) == 0:
        # Error checking in main program should prevent us from ever being
        # able to get here.
        raise Exception('Empty lists cannot be correlated.')
    if len(listx) > len(listy):
        listx = listx[:len(listy)]
    elif len(listx) < len(listy):
        listy = listy[:len(listx)]
    
    covariance = 0
    for i in range(len(listx)):
        covariance += 32 - bin(listx[i] ^ listy[i]).count("1")
    covariance = covariance / float(len(listx))
    
    return covariance/32
  
# return cross correlation, with listy offset from listx
def cross_correlation(listx, listy, offset):
    if offset > 0:
        listx = listx[offset:]
        listy = listy[:len(listx)]
    elif offset < 0:
        offset = -offset
        listy = listy[offset:]
        listx = listx[:len(listy)]
    if min(len(listx), len(listy)) < min_overlap:
        # Error checking in main program should prevent us from ever being
        # able to get here.
        return 
    #raise Exception('Overlap too small: %i' % min(len(listx), len(listy)))
    return correlation(listx, listy)
  
# cross correlate listx and listy with offsets from -span to span
def compare(listx, listy, span, step):
    if span > min(len(listx), len(listy)):
        # Error checking in main program should prevent us from ever being
        # able to get here.
        raise Exception('span >= sample size: %i >= %i\n'
                        % (span, min(len(listx), len(listy)))
                        + 'Reduce span, reduce crop or increase sample_time.')
    corr_xy = []
    for offset in numpy.arange(-span, span + 1, step):
        corr_xy.append(cross_correlation(listx, listy, offset))
    return corr_xy
  
# return index of maximum value in list
def max_index(listx):
    max_index = 0
    max_value = listx[0]
    for i, value in enumerate(listx):
        if value > max_value:
            max_value = value
            max_index = i
    return max_index
  
def get_max_corr(corr, source, target, Son, nametarget):
    max_corr_index = max_index(corr)
    max_corr_offset = -span + max_corr_index * step
    #print("max_corr_index = ", max_corr_index, "max_corr_offset = ", max_corr_offset)
    # report matches
    if corr[max_corr_index] > threshold:
        print("File A: %s" % (source))
        print("File B: %s" % (target))
        print('Match with correlation of %.2f%% at offset %i'
             % (corr[max_corr_index] * 100.0, max_corr_offset))
    ResultCompare = (corr[max_corr_index] * 100.0)


#Cree un dictionnaire pour mettre les resultat du comparaison
    dict_Comparaison=dict()
    with open('/opt/audio-compare-master/Dictionnaire/dict_Comparaison.pkl', 'rb') as fp:
        dict_Comparaison = pickle.load(fp)
    if Son == a:
        dict_Comparaison[a] = ResultCompare
    elif Son == b:
        dict_Comparaison[b] = ResultCompare
    elif Son == c:
        dict_Comparaison[c] = ResultCompare
    elif Son == d:
        dict_Comparaison[d] = ResultCompare
    elif Son == e:
        dict_Comparaison[e] = ResultCompare
    elif Son == f:
        dict_Comparaison[f] = ResultCompare
    elif Son == g:
        dict_Comparaison[g] = ResultCompare
    elif Son == h:
        dict_Comparaison[h] = ResultCompare
    elif Son == i:
        dict_Comparaison[i] = ResultCompare
    elif Son == j:
        dict_Comparaison[j] = ResultCompare
    elif Son == k:
        dict_Comparaison[k] = ResultCompare
        x=0
        dict_FeoMitovy=dict()
        for key, value in dict_Comparaison.items():
            if value >=65:
                print("Misy Feo manakaiky sady ananatsika ilay izy:")
                print(f"Ilay feo: {key}, Fitovizany: {value}%")
                dict_FeoMitovy[key]=value
                x=1
        if x==1:
            inverse = [(value, key) for key, value in dict_FeoMitovy.items()]
            FeoTenaMitovy=str(max(inverse)[1])
            PercentResult=str(dict_FeoMitovy.get(FeoTenaMitovy))
            print("Ity ny feo manakaiky indrindra ilay izy: "+FeoTenaMitovy)
            Recolte(FeoTenaMitovy, nametarget, PercentResult)      
            print(dict_Comparaison)
        else:
            print("Tsy misy donnée manakaiky indrindra")


    with open('/opt/audio-compare-master/Dictionnaire/dict_Comparaison.pkl', 'wb') as fp:
        pickle.dump(dict_Comparaison, fp)
        

def correlate(source, target, Son, nametarget):
    fingerprint_source = calculate_fingerprints(source)
    fingerprint_target = calculate_fingerprints(target)

    corr = compare(fingerprint_source, fingerprint_target, span, step)
    max_corr_offset = get_max_corr(corr, source, target, Son, nametarget)
