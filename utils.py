# =========================================
# utils.py
# FPS calculation and UI helper functions
# =========================================

import cv2
import time
from datetime import datetime


# -----------------------------------------
# FPS Calculator Class
# -----------------------------------------
class FPS:
    """
    Calculates Frames Per Second (FPS)
    """

    def __init__(self):
        self.previous_time = 0
        self.current_time = 0
        self.fps = 0

    def update(self):
        """
        Update FPS value
        """

        self.current_time = time.time()

        if self.previous_time != 0:
            self.fps = 1 / (self.current_time - self.previous_time)

        self.previous_time = self.current_time

        return int(self.fps)


# -----------------------------------------
# Draw Text on Frame
# -----------------------------------------
def draw_text(
    frame,
    text,
    position=(10, 30),
    color=(0, 255, 0),
    scale=1,
    thickness=2
):
    """
    Draw text on video frame
    """

    cv2.putText(
        frame,
        text,
        position,
        cv2.FONT_HERSHEY_SIMPLEX,
        scale,
        color,
        thickness,
        cv2.LINE_AA
    )


# -----------------------------------------
# Draw FPS
# -----------------------------------------
def draw_fps(frame, fps_value):
    """
    Display FPS on frame
    """

    draw_text(
        frame,
        f"FPS: {fps_value}",
        position=(10, 30),
        color=(0, 255, 0)
    )


# -----------------------------------------
# Draw Gesture Name
# -----------------------------------------
def draw_gesture(frame, gesture):
    """
    Display detected gesture
    """

    draw_text(
        frame,
        f"Gesture: {gesture}",
        position=(10, 70),
        color=(255, 0, 0)
    )


# -----------------------------------------
# Draw Status Message
# -----------------------------------------
def draw_status(frame, message):
    """
    Display status message
    """

    draw_text(
        frame,
        message,
        position=(10, 110),
        color=(0, 255, 255)
    )


# -----------------------------------------
# Get Current Timestamp
# -----------------------------------------
def get_timestamp():
    """
    Return current date and time
    """

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# -----------------------------------------
# Draw Center Crosshair
# -----------------------------------------
def draw_crosshair(frame):
    """
    Draw center crosshair
    """

    height, width = frame.shape[:2]

    center_x = width // 2
    center_y = height // 2

    # Horizontal line
    cv2.line(
        frame,
        (center_x - 20, center_y),
        (center_x + 20, center_y),
        (255, 255, 255),
        1
    )

    # Vertical line
    cv2.line(
        frame,
        (center_x, center_y - 20),
        (center_x, center_y + 20),
        (255, 255, 255),
        1
    )


# -----------------------------------------
# Simple Test
# -----------------------------------------
if __name__ == "__main__":

    fps = FPS()

    print("Testing FPS Calculator...")

    for i in range(5):
        time.sleep(0.1)
        value = fps.update()
        print(f"FPS: {value}")

    print("utils.py is working correctly!")