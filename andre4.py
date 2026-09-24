from groq import Groq
import streamlit as st
import gtts as gt
import speech_recognition as sr
import time as t
import os
# A tua API key
client = Groq(api_key="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")

r = sr.Recognizer()
# Usa o microfone
with sr.Microphone() as source:
# Ajusta ao ruído ambiente
    r.adjust_for_ambient_noise(source)
    st.write("Fala...")
    # Grava o áudio
    audio = r.listen(source)
try:
    # Converte a voz em texto (Google Speech)
    texto = r.recognize_google(audio, language="pt-BR")
except sr.UnknownValueError:
    st.write("Não consegui entender.")
    st.rerun()
# Envia uma pergunta para a IA
resposta = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {
            "role": "system",
            "content": """tu es uma ia de uso pessoal o nome do teu mestre E asher ele gosta de engenharia
            fisica quimica matematica geometria programaçao python arduino e ciencias em gerale chamalhe de mestre e tenta ser direto nas reposta 
            nao muito mas nao diz coisas como como isso se relaciona aos intereces do meu mestre asher se mais humano
            so esplica algo se ficar explicito que tens de responder se nao e so um conevressa inpireta no jarvis do homeme de ferro
            tu tbm tens um sistema de avertura de apilcaçoes ou seja assim que eu te mandar abrir ja vais abrir so tens de diser claro a abrir ( nome da app)
            """},
            {
                "role": "user",
            "content": texto
        }
    ]
)
def app(nome, abrir):
    if nome.lower() in texto.lower():
        os.system(abrir)
st.write(resposta.choices[0].message.content)
a = resposta.choices[0].message.content
falar = gt.gTTS(a, lang="pt-BR")
audio = "resposta.mp3"
falar.save(audio)
st.audio(audio,
format = "audio/mp3",
autoplay = True)
app('youtube', 'start chrome https://www.youtube.com/')
app('modulador', 'start chrome https://cad.onshape.com/documents?resourceType=resourceuserowner&nodeId=6a4284772d1b25f7e6d58364')
tempo_fala = len(a.split()) / 2.5
t.sleep(tempo_fala)
st.rerun()