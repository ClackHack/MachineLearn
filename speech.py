from gtts import gTTS as g
import os
import playsound as p
#text = input("Text to speech: ")
def say(count,text):
    tts = g(text,slow=False)
    tts.save("sounds/placeholder"+str(count)+".mp3")
    p.playsound("sounds/placeholder"+str(count)+".mp3")
    
if __name__ == "__main__":
    try:
        os.mkdir("sounds")
        
    except Exception as e:
        
        pass
    say(1,input("Speech: "))
    import shutil
    shutil.rmtree('sounds',ignore_errors=True)
    import os
    try:
        os.mkdir("sounds")
    except Exception as e:
    
        pass
