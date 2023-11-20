import pyaudio
import wave
import pickle
# Configuration
FORMAT = pyaudio.paInt16  # Audio format (16-bit PCM)
CHANNELS = 1              # Mono audio
RATE = 44100             # Sample rate (samples per second)
RECORD_SECONDS = 35     # Duration of recording
INPUT_DEVICE_INDEX= 2
#NEw Things
CHUNK = 1024


#j = np.complex(0, 1)
# Initialize PyAudio
audio = pyaudio.PyAudio()

# Open a microphone stream
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,input_device_index=INPUT_DEVICE_INDEX,
                    frames_per_buffer=CHUNK)

print("Recording...")

frames = []
# Record audio in chunks and store in frames
for _ in range(0, int(RATE / 1024 * RECORD_SECONDS)):
    data = stream.read(1024)
    frames.append(data)



print("Finished recording.")

# Stop and close the microphone stream
stream.stop_stream()
stream.close()

# Terminate PyAudio
audio.terminate()

# Save the recorded audio to a WAV file
dict_recording_conter=dict()
with open('/opt/audio-compare-master/Dictionnaire/dict_recording_conter.pkl', 'rb') as fp:
    dict_recording_conter = pickle.load(fp)
recording_conter = dict_recording_conter.get("recording_conter")
recording_conter += 1
dict_recording_conter["recording_conter"] = recording_conter 
OUTPUT_FILENAME = '/opt/audio-compare-master/FeoAla/IndriIndri'+str(recording_conter)+'.wav'
with wave.open(OUTPUT_FILENAME, 'wb') as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
with open('/opt/audio-compare-master/Dictionnaire/dict_recording_conter.pkl', 'wb') as fp:
    pickle.dump(dict_recording_conter, fp)
print(f"Audio saved to {OUTPUT_FILENAME}")
