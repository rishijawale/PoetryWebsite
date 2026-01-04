import pandas as pd
import os
from datetime import date

# ===== FILE PATHS =====
DATA_FILE = "poems_with_tone.csv"
HISTORY_DIR = "history"
HISTORY_FILE = os.path.join(HISTORY_DIR, "posted_poems.csv")

# This is where website reads from
TODAY_POEM_OUTPUT = "../poetry_website/data/today_poem.csv"

os.makedirs(HISTORY_DIR, exist_ok=True)

# Load poems
df = pd.read_csv(DATA_FILE)

def load_history():
    if os.path.exists(HISTORY_FILE):
        return pd.read_csv(HISTORY_FILE)
    return pd.DataFrame(columns=["date", "poem"])

def save_history(history_df):
    history_df.to_csv(HISTORY_FILE, index=False)

def pick_poem():
    today = str(date.today())
    history = load_history()

    # If today's poem already picked, do nothing
    if today in history["date"].values:
        print("Today's poem already generated.")
        return

    used_poems = history["poem"].tolist()

    available = df[~df["poem content"].isin(used_poems)]

    if available.empty:
        raise Exception("No new poems left.")

    poem = available.sample(1).iloc[0]

    # Save to history
    history = pd.concat([
        history,
        pd.DataFrame([{
            "date": today,
            "poem": poem["poem content"]
        }])
    ])
    save_history(history)

    # ⭐ SAVE FOR WEBSITE
    pd.DataFrame([poem]).to_csv(TODAY_POEM_OUTPUT, index=False)

    print("Poem selected for", today)
    print(poem["poem content"])

    return poem

if __name__ == "__main__":
    pick_poem()
