import io
import os
import glob
import numpy as np
from PIL import Image
from pydub import AudioSegment
import streamlit as st
from audio_conversion import to_mp3, to_wav, to_mp4, to_ogg, to_wma, to_aac, to_flac, to_flv

upload_path = "uploads/"
download_path = "downloads/"

st.set_page_config(
    page_title="Audio Converter",
    page_icon="musical_note",
    layout="centered",
    initial_sidebar_state="auto",
)

top_image = Image.open('static/banner_top.png')
bottom_image = Image.open('static/banner_bottom.png')
main_image = Image.open('static/main_banner.png')

st.sidebar.image(top_image,use_column_width='auto')
st.sidebar.header('🌟 Please choose the Audio Format 🎵')
trans_audio = st.sidebar.selectbox('Select target audio format type 🎯',["WAV","MP3","MP4","OGG","WMA","AAC","FLAC","FLV"])
st.sidebar.image(bottom_image,use_column_width='auto')

st.image(main_image,use_column_width='auto')
st.title("🎼🎶 Mini-Audio Converter 🎙🔉")
st.info('✨ Supports all popular audio formats - WAV, MP3, MP4, OGG, WMA, AAC, FLAC, FLV 😉')

uploaded_file = st.file_uploader("Upload audio file", type=["wav","mp3","ogg","wma","aac","flac","mp4","flv"])

audio_file = None

if uploaded_file is not None:
    audio_bytes = uploaded_file.read()
    with open(os.path.join(upload_path,uploaded_file.name),"wb") as f:
        f.write((uploaded_file).getbuffer())
    with st.spinner(f"Converting... 💫"):
        output_audio_file = uploaded_file.name.split('.')[0] + '.' + trans_audio

        ## To MP3 ##
        if trans_audio.lower() == "mp3":
            output_audio_file = to_mp3(uploaded_file, output_audio_file, upload_path, download_path)
            mime_type = 'audio/mpeg'

        ## To WAV ##
        elif trans_audio.lower() == "wav":
            output_audio_file = to_wav(uploaded_file, output_audio_file, upload_path, download_path)
            mime_type = 'audio/wav'

        ## To MP4 ##
        elif trans_audio.lower() == "mp4":
            output_audio_file = to_mp4(uploaded_file, output_audio_file, upload_path, download_path)
            mime_type = 'audio/mp4'

        ## To OGG ##
        elif trans_audio.lower() == "ogg":
            output_audio_file = to_ogg(uploaded_file, output_audio_file, upload_path, download_path)
            mime_type = 'audio/ogg'

        ## To WMA ##
        elif trans_audio.lower() == "wma":
            output_audio_file = to_wma(uploaded_file, output_audio_file, upload_path, download_path)
            mime_type = 'audio/x-ms-wma'

        ## To AAC ##
        elif trans_audio.lower() == "aac":
            output_audio_file = to_aac(uploaded_file, output_audio_file, upload_path, download_path)
            mime_type = 'audio/aac'

        ## To FLAC ##
        elif trans_audio.lower() == "flac":
            output_audio_file = to_flac(uploaded_file, output_audio_file, upload_path, download_path)
            mime_type = 'audio/flac'

        ## To FLV ##
        elif trans_audio.lower() == "flv":
            output_audio_file = to_flv(uploaded_file, output_audio_file, upload_path, download_path)
            mime_type = 'video/x-flv'

        audio_file = open(os.path.join(download_path,output_audio_file), 'rb')
        audio_bytes = audio_file.read()
        print("Opening ",audio_file)
        st.markdown("---")
        st.markdown("Feel free to play your converted audio 🎼")
        st.audio(audio_bytes)
        if st.download_button(
                             label="Download Converted Audio 🎶",
                             data=audio_bytes,
                             file_name=output_audio_file,
                             mime=mime_type
                         ):
            st.balloons()
            st.success('✅ Download Successful !!')
else:
    st.warning('⚠ Please upload your audio file 😯')

st.markdown("<br><hr><center>Made with ❤️ by <a href='mailto:ralhanprateek@gmail.com?subject=Mini-Audio Converter WebApp!&body=Please specify the issue you are facing with the app.'><strong>Prateek Ralhan</strong></a></center><hr>", unsafe_allow_html=True)

