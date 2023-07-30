import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
        return ""
    except sr.RequestError:
        print("Sorry, there was an issue with the speech recognition service.")
        return ""

if __name__ == "__main__":
    print("Jarvis: Hello! How can I assist you today?")
    while True:
        user_input = listen()
        if user_input == "exit":
            print("Jarvis: Goodbye!")
            break
        elif "hello" in user_input:
            speak("Hello! How can I assist you?")
        elif "time" in user_input:
            import datetime
            current_time = datetime.datetime.now().strftime("%H:%M")
            speak(f"Current time is {current_time}.")
        else:
            speak("I'm sorry, I cannot perform that task.")
