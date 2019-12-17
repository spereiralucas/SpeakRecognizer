import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice', en_voice_id)

def listenToMicrophone():
	microphone = sr.Recognizer()
	with sr.Microphone() as source:
		microphone.adjust_for_ambient_noise(source)
		print("Say something: ")
		audio = microphone.listen(source)

	try:
		phrase = microphone.recognize_google(audio,language='en-US')
		print("You said: " + phrase)
		engine.say("You said: " + phrase)

	except sr.UnknownValueError:
		print("Sorry, I don't understand what you said. Please, try again.")
		engine.say("Sorry, I don't understand what you said. Please, try again.")
	return phrase	

phrase = listenToMicrophone()
engine.runAndWait()
