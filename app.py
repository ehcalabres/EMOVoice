import os
import streamlit as st

EXAMPLE_PATH = []
for f in os.listdir('data/'):
    EXAMPLE_PATH.append(f)

st.sidebar.image('img/love_emoji_128.png')
st.sidebar.title('EMOVoice')
st.sidebar.write('Welcome to EMOVoice, a tool for Speech Emotion Recognition based on the Wav2Vec2 model.')

st.title('EMOVoice')
st.write("This is a work in progress, stay tuned!")

st.sidebar.subheader('Model input')
input_mode = st.sidebar.radio('Select your input mode:', ['Upload audio', 'Select example'])

file = None

if input_mode == 'Upload audio':
    file = st.sidebar.file_uploader("Choose a file", type=['mp3', 'mp4', 'wav', 'flac'])
elif input_mode == 'Select example':
    example_selected = st.sidebar.selectbox('Choose an audio example', EXAMPLE_PATH)
    file = open('data/' + example_selected, 'rb')

if file is not None:
    st.write('Audio added!')
    audio_bytes = file.read()
    st.audio(audio_bytes)
    file.close()
