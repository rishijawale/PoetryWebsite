from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

DATA_FILE = "data/poems_with_tone.csv"
DAILY_POEM_FILE = "data/today_poem.csv"

df = pd.read_csv(DATA_FILE)

@app.route("/")
def home():
    if not os.path.exists(DAILY_POEM_FILE):
        return "Daily poem not generated yet."

    daily_df = pd.read_csv(DAILY_POEM_FILE)
    poem = daily_df.iloc[0]

    return render_template(
        "index.html",
        poem=poem["poem content"],
        author=poem.get("author", "Unknown"),
        tone=poem["tone"]
    )

@app.route("/browse")
def browse():
    tone = request.args.get("tone")

    if tone:
        poems = df[df["tone"].str.lower() == tone.lower()]
    else:
        poems = df.sample(30)

    poems = poems.to_dict(orient="records")

    tones = sorted(df["tone"].dropna().unique())

    return render_template(
        "browse.html",
        poems=poems,
        tones=tones,
        selected_tone=tone
    )

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/privacy")
def privacy():
    return render_template("privacy.html")

from flask import send_from_directory

@app.route("/sitemap.xml")
def sitemap():
    return send_from_directory("static", "sitemap.xml")

if __name__ == "__main__":
    app.run(debug=True)
