# =========================================
# voice.py
# Text-to-Speech for gestures
# =========================================

import pyttsx3

# Initialize engine
engine = pyttsx3.init()

# Voice settings
engine.setProperty('rate', 150)   # Speed
engine.setProperty('volume', 1.0) # Volume


def speak(text):
    """
    Speak the given text
    """

    try:
        engine.say(text)
        engine.runAndWait()

    except Exception as e:
        print("Voice Error:", e)


# Test
if __name__ == "__main__":

    print("Testing voice...")
    speak("Hand Gesture Recognition is working")
    print("Voice test completed")