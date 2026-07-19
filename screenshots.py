# =========================================
# screenshots.py
# Save webcam screenshots
# =========================================

import cv2
import os
from datetime import datetime


def save_screenshot(frame):
    """
    Save a screenshot from the webcam frame
    """

    # Create screenshots folder
    os.makedirs("screenshots", exist_ok=True)

    # Generate filename
    filename = datetime.now().strftime("%Y%m%d_%H%M%S") + ".png"

    # Full path
    path = os.path.join("screenshots", filename)

    # Save image
    cv2.imwrite(path, frame)

    print(f"Screenshot saved: {path}")

    return path


# Test
if __name__ == "__main__":

    # Create a dummy image
    import numpy as np

    dummy = np.zeros((300, 400, 3), dtype=np.uint8)

    save_screenshot(dummy)

    print("screenshots.py is working!")