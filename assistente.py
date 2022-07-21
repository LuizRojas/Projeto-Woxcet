# Arquivo principal

import speech_recognition as sr

# criando reconhecedor
r = sr.Recognizer()

# abrindo microfone para captura
with sr.Microphone() as source:
    rodando = True
    while rodando:
        audio = r.listen(source)  # define microfone como fonte de audio

        print(r.recognize_google(audio, language='pt'))
