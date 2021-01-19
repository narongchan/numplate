# from main import chars
from main import chars
from gtts import gTTS
from playsound import playsound

matched_market = "서구푸드마켓1호점"

mytext= matched_market

text_lang="ko"

myspeech= gTTS(text=mytext+"입니다", lang=text_lang, slow=False)
myspeech.save("welcome.mp3")

playsound("welcome.mp3")