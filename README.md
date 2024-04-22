# Speech Recognition from video ▶ ılıılıılıılıılıılı
This script recognizes speech from a video and saves the recognized text to a .txt file.

### Third-party library:
- whisper - machine learning model for speech recognition and transcription
- pydub - library for working with audio files  
- moviepy - library for working with video files

### You need instsall these packages for speech recognize working:
- #### ffmpeg
This package works with a whisper. To install on Linux, use the following command:
```bash
sudo apt-get -y install ffmpeg 
```
To intsall on Windows, use the following link: 
https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/
- #### pydub, moviepy, whisper
```bash
pip install pydub
pip install moviepy
pip install openai-whisper
```
Then you need run command
```bash
python3 speech_recognition.py
```
### Script logic
1. Upload video file that need recognize
2. Library moviepy get audio file from video
3. Library pydub split audio on chunks with equal length
4. Chunks saved on folder
5. Library whisper recognize sequentially each chunk
6. Recognized chunk is removing
7. Recognized text save the .txt file 
#### You can see how the script works
![image](https://github.com/OnvoKoder/SpeechRecognitionFromVideo/assets/65452318/1e2ba370-206f-46cc-ba96-368890bc8acc)

