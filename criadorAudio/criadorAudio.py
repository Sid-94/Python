from gtts import gTTS
from playsound import playsound

s = gTTS("Muito Obrigada e volte sempre!",lang='pt-pt')
s.save('obrigadaVolteSempre.mp3')
playsound('obrigadaVolteSempre.mp3')