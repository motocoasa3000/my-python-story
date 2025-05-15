from gtts import gTTS
import os
text = open('text.txt', 'r').read()

language='en'
output = gTTS(text=text, lang=language, slow=False)
output.save('fileoutput.mp3')
os.system("afplay fileoutput.mp3")
