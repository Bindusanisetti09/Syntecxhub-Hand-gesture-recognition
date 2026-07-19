# =========================================
# settings.py
# Project configuration settings
# =========================================

# Camera Settings
CAMERA_INDEX = 0
FRAME_WIDTH = 1280
FRAME_HEIGHT = 720
FPS_LIMIT = 30

# Window Settings
WINDOW_NAME = "Hand Gesture Recognition"

# MediaPipe Settings
MAX_NUM_HANDS = 1
MIN_DETECTION_CONFIDENCE = 0.7
MIN_TRACKING_CONFIDENCE = 0.7

# Feature Toggles
SPEAK_GESTURES = True
SAVE_HISTORY = True
ENABLE_SCREENSHOTS = True

# Screenshot Settings
SCREENSHOT_FOLDER = "screenshots"

# Data Settings
HISTORY_FILE = "data/history.csv"

# Gesture Labels
GESTURE_LABELS = {
    0: "FIST",
    1: "ONE",
    2: "TWO",
    3: "THREE",
    4: "FOUR",
    5: "OPEN PALM"
}

# UI Colors (BGR format)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (255, 0, 0)
COLOR_RED = (0, 0, 255)
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)

# Text Settings
FONT_SCALE = 1
FONT_THICKNESS = 2

# Keyboard Controls
EXIT_KEY = 'q'
SCREENSHOT_KEY = 's'