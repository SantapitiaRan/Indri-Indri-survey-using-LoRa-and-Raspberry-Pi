import pickle
dict_recording_conter={"recording_conter":0}
with open('/opt/audio-compare-master/Dictionnaire/dict_recording_conter.pkl', 'wb') as fp:
    pickle.dump(dict_recording_conter, fp)
# with open('/opt/audio-compare-master/dict_recording_conter.pkl', 'rb') as fp:
#     dict_recording_conter = pickle.load(fp)
#     print('dict_recording_conter:')
#     print(dict_recording_conter)   