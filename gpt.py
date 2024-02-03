import openai
import speech_recognition as sr
import asr1 as sp
import historytxt as st

def onlylisten():
    error="None"
    gr = sr.Recognizer()
    with sr.Microphone() as gsource:
        print("listening...")
        gr.energy_threshold = 800
        gr.pause_threshold = 1
        gaudio = gr.listen(gsource)
    try:
        print("recognizing...")
        query = gr.recognize_google(gaudio, language="en-IN")
        return query
    except Exception as e:
        return error
openai.api_key = "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"

def thinking(a):
    print("thinking...")
    output=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[

        {"role": "assistant", "content": a},
        
    ])
    return output
while True:
    input=onlylisten()
    print(input)
    if input=="stop listening":
        break    
    x=thinking(input)
    st.store(input)
    print(x["choices"][0]["message"]["content"])
    sp.speak(x["choices"][0]["message"]["content"])
sp.speak("thank you for using assistant")
