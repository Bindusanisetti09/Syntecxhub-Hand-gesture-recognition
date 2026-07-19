# =========================================
# hand_detector.py
# Detect hand landmarks using MediaPipe
# =========================================

import cv2
import mediapipe as mp
from settings import (
    MAX_NUM_HANDS,
    MIN_DETECTION_CONFIDENCE,
    MIN_TRACKING_CONFIDENCE
)


class HandDetector:

    def __init__(self):

        # Initialize MediaPipe Hands
        self.mp_hands = mp.solutions.hands

        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=MAX_NUM_HANDS,
            min_detection_confidence=MIN_DETECTION_CONFIDENCE,
            min_tracking_confidence=MIN_TRACKING_CONFIDENCE
        )

        # Drawing utility
        self.mp_draw = mp.solutions.drawing_utils

    def detect_hands(self, frame):

        # Convert BGR to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process frame
        results = self.hands.process(rgb_frame)

        landmarks = []

        # Draw landmarks if hand detected
        if results.multi_hand_landmarks:

            for hand_landmarks in results.multi_hand_landmarks:

                self.mp_draw.draw_landmarks(
                    frame,
                    hand_landmarks,
                    self.mp_hands.HAND_CONNECTIONS
                )

                landmarks = hand_landmarks.landmark

        return frame, landmarks


# Test file
if __name__ == "__main__":

    from camera import initialize_camera

    cap = initialize_camera()
    detector = HandDetector()

    print("Hand detector started")
    print("Show your hand to the camera")
    print("Press Q to quit")

    while True:

        success, frame = cap.read()

        if not success:
            break

        frame = cv2.flip(frame, 1)

        frame, landmarks = detector.detect_hands(frame)

        if landmarks:
            cv2.putText(
                frame,
                f"Landmarks: {len(landmarks)}",
                (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

        cv2.imshow("Hand Detector Test", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()