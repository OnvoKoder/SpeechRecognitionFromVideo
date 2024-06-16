import whisper
import moviepy.editor as mp
from pydub import AudioSegment
import os
from datetime import datetime

def extract_audio(video_path:str) -> str:
    video = mp.VideoFileClip(video_path)
    audio_path = video_path.replace('.mp4', '.wav')
    video.audio.write_audiofile(audio_path)
    return audio_path

def split_audio(audio_path:str, interval:int) -> list[str]:
    audio = AudioSegment.from_file(audio_path)
    chunk:AudioSegment
    chunks_name:str = ''
    history = []
    for i in range(0, len(audio), interval):
        chunks_name = f'chunk{i}.wav'
        chunk = audio[i : i + interval]
        chunk.export(chunks_name, format = 'wav')
        history.append(chunks_name)
    return history

def extract_text(chunk:str, language:str) -> str:
    model = whisper.load_model('small')
    print(f'[{datetime.now()}] {chunk} start recognition')
    audio_text = model.transcribe(chunk, language = language[0:2])
    print(f'[{datetime.now()}] {chunk} complete recognition')
    os.remove(chunk)
    return audio_text['text']

def upload_video(video_path:str, interval:int, language:str) -> str:
    audio_path:str = extract_audio(video_path)
    chunks:list[str] = split_audio(audio_path, interval)
    result = []
    for chunk in chunks:
        result.append(extract_text(chunk, language))
    tmp:str = '' 
    for index in range(0, len(result)):
        tmp += f'\ntime:{index} - {index + 1} minutes\n'
        tmp += result[index] 
    return tmp

current_dir = os.getcwd()
for filename in os.listdir(current_dir):
    if filename.endswith('.mp4') and filename.startswith('recognition!') == False:
        print(f'[{datetime.now()}] {filename} start recognition')
        text =  from_video(filename, 60000)
        file = open(filename.replace('.mp4', '.txt'), 'w')
        file.write(text)
        file.close()
        os.rename(filename,f'recognition!{filename}')
        print(f'[{datetime.now()}] {filename} finish recognition')