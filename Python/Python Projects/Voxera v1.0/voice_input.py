import speech_recognition as sr
recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return ""

    text = text.lower().strip()
    print(f"You: {text}")
    return text

if __name__ == "__main__":
    listen()