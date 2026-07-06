pip install SpeechRecognition pyttsx3 PyAudio

# voice_assistant.py

import speech_recognition as sr
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

engine.setProperty("rate", 160)   # Speaking speed
engine.setProperty("volume", 1.0) # Maximum volume


def speak(text):
    """
    Convert text to speech.
    """

    print("Assistant:", text)

    engine.say(text)
    engine.runAndWait()


def listen():
    """
    Listen to the user's voice and convert it to text.
    """

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")

        recognizer.adjust_for_ambient_noise(source, duration=1)

        audio = recognizer.listen(source)

    try:

        text = recognizer.recognize_google(audio)

        print("You:", text)

        return text.lower()

    except sr.UnknownValueError:

        return "Sorry, I could not understand your voice."

    except sr.RequestError:

        return "Speech recognition service is unavailable."


def start_voice_assistant():
    """
    Run the voice assistant.
    """

    speak("Hello! I am your AI Medical Assistant.")
    speak("Tell me your symptoms or ask a health-related question.")

    while True:

        query = listen()

        if query in ["exit", "quit", "stop", "bye"]:
            speak("Goodbye. Stay healthy!")
            break

        elif "fever" in query:
            speak(
                "Fever may be caused by an infection. "
                "Stay hydrated, rest well, and consult a doctor if it is high or persistent."
            )

        elif "cough" in query:
            speak(
                "A cough can be due to several causes. "
                "Drink warm fluids and consult a doctor if it continues."
            )

        elif "headache" in query:
            speak(
                "A headache can be caused by stress, dehydration, or illness. "
                "Drink water, rest, and seek medical advice if it is severe."
            )

        elif "cold" in query:
            speak(
                "The common cold usually improves with rest and fluids."
            )

        elif "covid" in query:
            speak(
                "If you suspect COVID-19, follow local health guidance and consult a healthcare professional."
            )

        elif "thank" in query:
            speak("You're welcome!")

        elif "hello" in query or "hi" in query:
            speak("Hello! How can I help you today?")

        else:
            speak(
                "I'm sorry, I don't have enough information to answer that. "
                "Please consult a qualified healthcare professional."
            )


# Run directly
if __name__ == "__main__":
    start_voice_assistant()
