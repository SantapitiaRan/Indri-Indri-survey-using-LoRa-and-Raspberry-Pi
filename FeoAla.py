import pickle
dict_FeoAla_conter={"FeoAla_conter":1}
with open('/opt/audio-compare-master/Dictionnaire/dict_FeoAla_conter.pkl', 'wb') as fp:
    pickle.dump(dict_FeoAla_conter, fp)