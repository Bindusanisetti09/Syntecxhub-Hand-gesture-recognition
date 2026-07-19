# =========================================
# camera.py
# Webcam initialization and testing
# =========================================

import cv2
from settings import CAMERA_INDEX, FRAME_WIDTH, FRAME_HEIGHT


def initialize_camera():
    """Initialize the webcam"""

    # Open webcam
    cap = cv2.VideoCapture(CAMERA_INDEX)

    # Check camera
    if not cap.isOpened():
        raise Exception("Unable to open webcam")

    # Set resolution
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

    return cap


def test_camera():
    """Test webcam"""

    try:
        cap = initialize_camera()

        print("Webcam opened successfully")
        print("Press Q to close")

        while True:
            success, frame = cap.read()

            if not success:
                print("Failed to read frame")
                break

            # Mirror effect
            frame = cv2.flip(frame, 1)

            # Show camera
            cv2.imshow("Camera Test", frame)

            # Exit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except Exception as e:
        print("Error:", e)

    finally:
        try:
            cap.release()
        except:
            pass

        cv2.destroyAllWindows()
        print("Camera closed")


# Run directly
if __name__ == "__main__":
    test_camera()