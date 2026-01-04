from step3_daily_picker import pick_poem
from step4_image_generator import generate_poetry_image
from step5_caption_generator import generate_caption

def run_pipeline():
    poem_row = pick_poem()

    poem_text = poem_row["poem content"]
    tone = poem_row["tone"]
    author = poem_row.get("author", "Unknown")

    image_path = generate_poetry_image(poem_text, author)
    caption = generate_caption(poem_text, author, tone)

    print("\nIMAGE GENERATED:", image_path)
    print("\nCAPTION:\n")
    print(caption)

if __name__ == "__main__":
    run_pipeline()
