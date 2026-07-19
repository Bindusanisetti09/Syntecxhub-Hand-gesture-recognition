# =========================================
# gesture_classifier.py
# Finger counting and gesture recognition
# =========================================

class GestureClassifier:
    """
    Classifies hand gestures using MediaPipe landmarks.
    """

    def __init__(self):
        # Fingertip landmark IDs
        self.tip_ids = [4, 8, 12, 16, 20]

    def classify(self, landmarks):
        """
        Detect gesture from hand landmarks.
        """

        # No hand detected
        if not landmarks or len(landmarks) < 21:
            return "No Hand"

        fingers = []

        # ---------- Thumb ----------
        if landmarks[self.tip_ids[0]].x < landmarks[self.tip_ids[0] - 1].x:
            fingers.append(1)
        else:
            fingers.append(0)

        # ---------- Other 4 Fingers ----------
        for i in range(1, 5):

            if landmarks[self.tip_ids[i]].y < landmarks[self.tip_ids[i] - 2].y:
                fingers.append(1)
            else:
                fingers.append(0)

        # Count open fingers
        total_fingers = sum(fingers)

        # ---------- Gesture Mapping ----------
        if total_fingers == 0:
            return "FIST"

        elif total_fingers == 1:

            if fingers[1] == 1:
                return "ONE"
            else:
                return "THUMB"

        elif total_fingers == 2:
            return "TWO"

        elif total_fingers == 3:
            return "THREE"

        elif total_fingers == 4:
            return "FOUR"

        elif total_fingers == 5:
            return "OPEN PALM"

        return "UNKNOWN"


# =========================================
# Test
# =========================================
if __name__ == "__main__":

    classifier = GestureClassifier()

    print("GestureClassifier loaded successfully!")