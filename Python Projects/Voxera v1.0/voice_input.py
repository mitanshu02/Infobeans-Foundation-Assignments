import speech_recognition as sr


recognizer = sr.Recognizer()


def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        text = text.lower().strip()
        print(f"You: {text}")
        return text

    except sr.UnknownValueError:
        print("Could not understand the audio.")
        return ""

    except sr.RequestError:
        print("Speech recognition service is unavailable.")
        return ""

listen()