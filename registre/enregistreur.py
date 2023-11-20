import os
import pyaudio
import wave
import RPi.GPIO as GPIO

#Déclaration des boutons :
#	Raccrocher & décrocher = pin 29
#   Bouton centrale        =
#   Bouton1     		   = pin 31
#	Bouton2		           = pin 33
#	Bouton3 		       = pin 35
#	Bouton4		           = pin 37
#   Bouton5                = 
bt1 =29
bt2 =31
bt3 =33
bt4 =35
bt5 =37

#Declaration de l'entrer vers le rasp
GPIO.setmode(GPIO.BOARD)
GPIO.setup(bt1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(bt2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(bt3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(bt4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(bt5, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Parametre d'enregistrement
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024

audio = pyaudio.PyAudio()

def start_recording():
    global is_recording,recording_file
    if not is_recording:
        is_recording = True
        file_name = f"/opt/registre/Rec{recording_conter}.wav"
        recording_file = wav.open(file_name, "wb")
        recording_file.setnchannels(CHANNELS)
        recording_file.setsampwidth(audio.get_sample_size(Format))
        recording_file.setframerate(RATE)
        recording_conter += 1
        print("Enregistrement demare")

def stop_recording():
    global is_recording,recording_file
    if not is_recording:
        is_recording = False
        recording_file.close()
        print("Fin d'enregistrement")

def play_last_recording():
    recordings_dir = "/opt/registre"
    recordings = sorted(os.listdir(recordings_dir), key=lambda x : os.path.getmtime(os.path.join(recordings_dir,x)),reverse=True)
    if recordings:
            last_recording = os.path.join(recordings_dir,recordings[0])
            chunk = 1024
            wf = wave.open(last_recording,'rb')
            audio = pyaudio.PyAudio()
            stream = audio.open(format=audio.get_format_from_width(wf.getsampwidth()),channels=wf.getnchannels(),rate=wf.getframerate(),output=True)
            data = wf.readframes(chunk)
            while data:
                stream.write(data)
                data=wf.readframes(chunk)
            stream.stop_stream()
            stream.close()
            audio.terminate()
            
def replace_last_recording():
    global is_recording,recording_file
    if not is_recording:
        is_recording = True
        file_name = directory_path = '/opt/registre'.wav
        files = os.listdir(directory_path)
        files = [f for f in files if os.path.isfile(os.path.join(directory_path, f))]
        files.sort(key=lambda x: os.path.getmtime(os.path.join(directory_path, x)), reverse=True)
        if files:
            most_recent_file = files[0]
        recording_file = wav.open(file_name, "wb")
        recording_file.setnchannels(CHANNELS)
        recording_file.setsampwidth(audio.get_sample_size(Format))
        recording_file.setframerate(RATE)
        recording_conter += 1
        print("Enregistrement demare")

def delet_last_recording():
    recordings_dir="/opt/registre".wav
    recording=sorted(os.listdir(recordings_dir), key=lambda x : os.path.getmtime(os.path.join(recordings_dir,x)),reverse=True)
    if recordings:
        last_recording = os.path.join(recordings_dir,recordings[0])
        chunk = 1024
        wf = wave.open(last_recording,'rb')
        audio = pyaudio.PyAudio()
        stream = audio.open(format=audio.get_format_from_width(wf.getsampwidth()),channels=wf.getnchannels(),rate=wf.getframerate(),output=True)
    if recordings:
        last_recording = os.path.join(recordings_dir,recordings[0])
        os.remove(last_recording)

#def play_first_recording():


#def play_second_recording():

#Bouton raccrocher et décrocher :
#Si LOW :
if bt1 == GPIO.LOW:
#1.	Envoi du message d’accueil   => message déjà enregistré dès le début
    play_first_recording()
#2.	Début d’enregistrement  => activation de l’enregistreur
    start_recording()
#Si HIGH :
if bt1 == GPIO.HIGH:
#1.	Fin d’enregistrement  => désactivation de l’enregistreur 
    stop_recording()
 
#Bouton1 :
#Si HIGH :
if bt2 == GPIO.HIGH:
#Renvoyer la dernière prise  => ouverture du dossier et lecture de la dernière prise
    stop_recording()
    play_last_recording()
#Si LOW :
#     None
 
#Bouton2 :
#Si HIGH :
if bt3 == GPIO.HIGH:
#1.	Envoie du message d’accueil => lecture du premier message
    play_first_recording()
#2.	Début d’enregistrement  => activation de l’enregistrement
    stop_recording()
    replace_last_recording()
#Si LOW :
#     None 

#Bouton3 :
#Si HIGH :
if bt4 == GPIO.HIGH:
#1.	Envoie d’un message  => lecture de la deuxième message
    play_second_recording()
#2.	Suppression de la dernière message  => ouverture du dossier et suppression de la dernière prise
    stop_recording()
    if bt5 == GPIO.HIGH:
        delet_last_recording()
#Si LOW :
#	  None