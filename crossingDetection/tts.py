import gtts
from playsound import playsound


# make request to google to get synthesis
tts = gtts.gTTS("There is a crossing ahead with walk sign on but there is an ambulance coming on the road.")

# save the audio file
tts.save("hello.mp3")

# play the audio file
playsound("hello.mp3")