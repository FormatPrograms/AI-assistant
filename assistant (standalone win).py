# libraries
import ollama as oll
import speech_recognition as sr
from time import sleep
import pyttsx3

eng = pyttsx3.init()


def gen(prompt):
	response = oll.chat(model='Llama3.1', messages=[{'role': 'user', 'content': f"{prompt}"},])
	global generated
	generated = response['message']['content']


def get_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening for the wake word...")
        try:
            audio = recognizer.listen(source, timeout=LISTEN_TIMEOUT, phrase_time_limit=PHRASE_TIME_LIMIT)
            said = recognizer.recognize_google(audio)
            print(f"Recognized: {said}")
            return said.lower()
        except sr.WaitTimeoutError:
            print("Listening timed out.")
        except sr.UnknownValueError:
            print("Speech not recognized.")
        except sr.RequestError as e:
            print(f"API request error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
    return ""


def main():
    prompt = get_audio()
    gen(prompt)
    eng.say(generated)


if __name__ == "__main__":
    while True:
        try:
            main()
            eng.runAndWait()
        except KeyboardInterrupt:
            print("Program terminated by user.")
