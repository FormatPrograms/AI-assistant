import socket
import speech_recognition as sr
from time import sleep
from pyspeak import speak

IP = "192.168.1.252"
PORT = 8773
MAX_FAILURES = 5
RECONNECT_DELAY = 2
LISTEN_TIMEOUT = 10
PHRASE_TIME_LIMIT = 5

def create_socket():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((IP, PORT))
        print(f"Connected to server at {IP}:{PORT}")
        return s
    except Exception as e:
        print(f"Error connecting to server: {e}")
        return False

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

def communicate_with_server(s, prompt):
    try:
        s.send(prompt.encode())
        response = s.recv(1024).decode()
        if response == "bruh./23":
            print("Server sent termination signal.")
            return False
        else:
            speak(response)
            print(f"Server response: {response}")
    except Exception as e:
        print(f"Error communicating with server: {e}")
    return False

def main():
    failure_count = 0
    server_socket = create_socket()

    while True:
        if server_socket is None:
            print("Reconnecting to server...")
            server_socket = create_socket()
            if server_socket is None:
                sleep(RECONNECT_DELAY)
                continue

        prompt = get_audio()

        if "cleo" in prompt:
            if communicate_with_server(server_socket, prompt):
                break
            failure_count = 0
        else:
            print("Wake word 'Cleo' not detected.")
            failure_count += 1

            if failure_count >= MAX_FAILURES:
                print(f"Too many failed attempts ({MAX_FAILURES}). Retrying...")
                failure_count = 0
                sleep(RECONNECT_DELAY)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Program terminated by user.")
        if server_socket:
            server_socket.close()
