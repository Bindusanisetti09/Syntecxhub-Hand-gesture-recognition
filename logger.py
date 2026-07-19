# =========================================
# logger.py
# Save gesture history to CSV
# =========================================

import pandas as pd
from datetime import datetime
import os

# CSV file path
HISTORY_FILE = "data/history.csv"


def log_gesture(gesture):
    """
    Save detected gesture with timestamp
    """

    # Create data folder if not exists
    os.makedirs("data", exist_ok=True)

    # Create CSV file if not exists
    if not os.path.exists(HISTORY_FILE):

        df = pd.DataFrame(columns=["Timestamp", "Gesture"])
        df.to_csv(HISTORY_FILE, index=False)

    # New row
    new_row = {
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Gesture": gesture
    }

    # Read existing data
    df = pd.read_csv(HISTORY_FILE)

    # Add new row
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

    # Save
    df.to_csv(HISTORY_FILE, index=False)

    print(f"Logged: {gesture}")


# =========================================
# Test logger
# =========================================

if __name__ == "__main__":

    print("Testing logger...")

    log_gesture("OPEN PALM")
    log_gesture("FIST")

    print("Check data/history.csv")