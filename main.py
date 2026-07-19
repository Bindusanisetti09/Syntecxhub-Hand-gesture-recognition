# =========================================
# main.py
# Final Hand Gesture Recognition System
# =========================================

import cv2

from camera import initialize_camera
from hand_detector import HandDetector
from gesture_classifier import GestureClassifier
from gesture_actions import GestureActions
from utils import FPS, draw_fps, draw_gesture
from logger import log_gesture
from settings import WINDOW_NAME


def main():

    print("====================================")
    print("Hand Gesture Recognition Started")
    print("Press Q to quit")
    print("====================================")

    # Initialize camera
    # Initialize camera
    cap = initialize_camera()
    print("Camera connected successfully")
    # Initialize modules
    detector = HandDetector()
    classifier = GestureClassifier()
    actions = GestureActions()
    fps_counter = FPS()

    last_gesture = ""

    while True:

        # Read frame
        success, frame = cap.read()

        if not success:
            print("Failed to read frame")
            break

        # Mirror effect
        frame = cv2.flip(frame, 1)

        # Detect hand
        frame, landmarks = detector.detect_hands(frame)

        # Classify gesture
        gesture = classifier.classify(landmarks)

        # Update FPS
        fps_value = fps_counter.update()

        # Draw UI
        draw_fps(frame, fps_value)
        draw_gesture(frame, gesture)

        # New gesture detected
        if gesture != last_gesture and gesture != "No Hand":

            print(f"Detected Gesture: {gesture}")

            # Save to CSV
            log_gesture(gesture)

            # Perform action
            actions.perform_action(gesture, frame)

            last_gesture = gesture

        # Show window
        cv2.imshow(WINDOW_NAME, frame)

        # Exit
        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):
            print("Exiting...")
            break

    # Cleanup
    cap.release()
    cv2.destroyAllWindows()

    print("Program closed successfully")


if __name__ == "__main__":
    main()