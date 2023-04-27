# Developed using GitHub Co-pilot services

import gradio as gr # pip install gradio
import openai # pip install openai
from gtts import gTTS # pip install gTTS
import os # pip install os
import playsound # pip install playsound
from config import config # pip install config

openai.api_key = config['OPENAI_API_KEY'] # set the OpenAI API key

messages = [  # add messages to the chat
        {"role": "system", "content": "You are a helpful assistant."}, # add a system message, change to change personality of chatbot
    ]

def transcribe(audio): # audio is a filepath
    global messages # use the global messages variable

    #Transcribing audio recevied from the microphone
    audio_file= open(audio, "rb") # open the audio file
    transcript = openai.Audio.transcribe("whisper-1", audio_file) # transcribe the audio file
    
    #getting the response from chatGPT-3 model for current query
    messages.append({"role": "user", "content": transcript["text"]}) # add the user message to the messages list
    response = openai.ChatCompletion.create( # create a chat completion
    model="gpt-3.5-turbo",   # use the gpt-3.5-turbo model
    messages = messages
    )
    system_message = response["choices"][0]["message"]["content"] # get the system message

    #playing the curent query response from the chatGPT-3 model
    tts = gTTS(text=system_message, lang='en-us') # create a gTTS object
    tts.save("./file2.mp3") #
    playsound.playsound("./file2.mp3") # play the audio file
    os.remove("./file2.mp3") # remove the audio file
    messages.append({"role": "assistant", "content": system_message}) # add the system message to the messages list
    
    # aggreated transcript to keep the context of the conversations
    chat_transcript = "" # create a variable to store the chat transcript
    for message in messages:
        if message['role'] != 'system':
            chat_transcript += message['role'] + ": " + message['content'] + "\n\n"

    return chat_transcript # return the transcript

# launch the main interface
ui = gr.Interface(fn=transcribe, inputs=gr.Audio(source="microphone", type="filepath"), outputs="text")
ui.launch() # launch the interface


