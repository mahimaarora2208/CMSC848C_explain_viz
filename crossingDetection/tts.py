import gtts
from playsound import playsound

################################
# SCENARIO 1 (images 7, 9, 2)
################################
baselineStr = "img3_baseline.mp3"
fivecropStr = "img3_fivecrop.mp3"
manualStr = "img3_manual.mp3"

# make request to google to get synthesis

# # baseline 7
# tts = gtts.gTTS("this is a crosswalk")
# tts.save(baselineStr)

# # five crop 7
# tts = gtts.gTTS("a wall on the side of a building.power lines above the street.the road is tarmacked.white arrow painted on the street.white lines on a road.")
# tts.save(fivecropStr)
 
# # manual 7
# tts = gtts.gTTS("a sign on a pole.")
# tts.save(manualStr)

# # baseline 2
# tts = gtts.gTTS("a wall on the side of a building")
# tts.save(baselineStr)

# # five crop 2
# tts = gtts.gTTS("a tree in a city. a wall on the side of a building. this is a crosswalk.")
# tts.save(fivecropStr)
 
# # manual 2
# tts = gtts.gTTS("the light is orange")
# tts.save(manualStr)

# baseline 9
# tts = gtts.gTTS("this is a crosswalk")
# tts.save(baselineStr)

# # five crop 9
# tts = gtts.gTTS(" a wall on the side of a building. white line on road. this is a crosswalk.")
# tts.save(fivecropStr)
 
# # manual 9
# tts = gtts.gTTS("a city at night")
# tts.save(manualStr)


# playsound("hello.mp3")
################################
# SCENARIO 2 (images 6, 8, 3)
################################

# # baseline 6
# tts = gtts.gTTS("this is a crosswalk")
# tts.save(baselineStr)

# # five crop 6
# tts = gtts.gTTS(" a wall on the side of a building. the ground is gray. the street is grey.this is a crosswalk")
# tts.save(fivecropStr)
 
# # manual 6
# tts = gtts.gTTS("the car is parked on the side of the road")
# tts.save(manualStr)

# # baseline 8
# tts = gtts.gTTS("this is a crosswalk")
# tts.save(baselineStr)

# # five crop 8
# tts = gtts.gTTS(" a wall on the side of a building.a concrete sidewalk. white lines on a road")
# tts.save(fivecropStr)
 
# # manual 8
# tts = gtts.gTTS("a wall on the side of the building")
# tts.save(manualStr)

# baseline 3
tts = gtts.gTTS("this is a crosswalk")
tts.save(baselineStr)

# five crop 3
tts = gtts.gTTS("the sky is dark. a wall on the side of a building. the ground is gray. the road is tarmacked")
tts.save(fivecropStr)
 
# manual 3
tts = gtts.gTTS("white lines on the road")
tts.save(manualStr)

################################
# SCENARIO 2  (images 4, 5, 1)
################################