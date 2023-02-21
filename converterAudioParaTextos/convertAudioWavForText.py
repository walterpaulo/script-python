# pip install SpeechRecognition
import pdb

# importando a biblioteca
import speech_recognition as sr

# instanciando e limitando o threshold
recognizer = sr.Recognizer()
recognizer.energy_threshold = 300

# vamos guardar nosso áudio em uma varíavel com o mesmo nome
audio = sr.AudioFile('portugues.wav')

# pdb.set_trace()

# tipo de audio 
print(type(audio))

# convert de data type para Audio Data
with audio as source:
  audio = recognizer.record(source)

recognizer.recognize_google(audio, language="pt-br")
