import RPi.GPIO as GPIO
import picamera
import time, os
from gtts import gTTS
from playsound import playsound
  
def image_to_text(image_path:str) -> str:
    pass
    
def text_to_speech(text:str):
    # Language in which you want to convert
    language = 'ko'

    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    # have a high speed
    myobj = gTTS(text=text, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named
    mp3_name = str(time.time()) + ".mp3"
    myobj.save(mp3_name)

    # Playing the converted file

    playsound(mp3_name)  

button_pin = 14
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

if GPIO.input(button_pin) == GPIO.HIGH:
    image_name = str(time.time())+'.jpg'
    with picamera.PiCamera() as cam:
        cam.resolution = (640, 480)
        cam.start_preview()
        time.sleep(1)
        cam.capture(image_name)
        cam.stop_preview()
    
    text = image_to_text(image_name)
    text_to_speech(text)