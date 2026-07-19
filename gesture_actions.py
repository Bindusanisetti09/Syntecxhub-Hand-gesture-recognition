# =========================================
# gesture_actions.py
# Perform actions for detected gestures
# =========================================

from voice import speak
from screenshots import save_screenshot
from settings import SPEAK_GESTURES, ENABLE_SCREENSHOTS


class GestureActions:

    def __init__(self):
        self.last_action = ""

    def perform_action(self, gesture, frame):
        """
        Execute action based on gesture
        """

        # Prevent repeated actions
        if gesture == self.last_action:
            return

        self.last_action = gesture

        # Ignore when no hand
        if gesture == "No Hand":
            return

        # -----------------------------
        # OPEN PALM
        # -----------------------------
        if gesture == "OPEN PALM":

            print("Action: Open Palm Detected")

            if SPEAK_GESTURES:
                speak("Open Palm")

        # -----------------------------
        # FIST
        # -----------------------------
        elif gesture == "FIST":

            print("Action: Fist Detected")

            if SPEAK_GESTURES:
                speak("Fist")

        # -----------------------------
        # ONE
        # -----------------------------
        elif gesture == "ONE":

            print("Action: One Finger")

            if SPEAK_GESTURES:
                speak("One")

        # -----------------------------
        # TWO
        # -----------------------------
        elif gesture == "TWO":

            print("Action: Two Fingers")

            if SPEAK_GESTURES:
                speak("Two")

        # -----------------------------
        # THREE
        # Save Screenshot
        # -----------------------------
        elif gesture == "THREE":

            print("Action: Screenshot Gesture")

            if ENABLE_SCREENSHOTS:
                path = save_screenshot(frame)
                print(f"Screenshot saved: {path}")

            if SPEAK_GESTURES:
                speak("Screenshot Taken")

        # -----------------------------
        # FOUR
        # -----------------------------
        elif gesture == "FOUR":

            print("Action: Four Fingers")

            if SPEAK_GESTURES:
                speak("Four")

        # -----------------------------
        # UNKNOWN
        # -----------------------------
        else:

            print(f"Action: Unknown Gesture ({gesture})")


# =========================================
# Simple Test
# =========================================

if __name__ == "__main__":

    actions = GestureActions()

    print("Testing gesture actions...")

    # Fake test
    actions.perform_action("OPEN PALM", None)
    actions.perform_action("FIST", None)
    actions.perform_action("ONE", None)

    print("gesture_actions.py is working!")