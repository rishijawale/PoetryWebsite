from PIL import Image, ImageDraw, ImageFont
import random
import textwrap
import os

OUTPUT_DIR = "output_images"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_poetry_image(poem, author="Unknown"):
    img = Image.new("RGB", (1080, 1080), color="white")
    draw = ImageDraw.Draw(img)

    font_poem = ImageFont.truetype("arial.ttf", 50)
    font_author = ImageFont.truetype("arial.ttf", 30)

    wrapped = textwrap.fill(poem, width=32)

    bbox = draw.multiline_textbbox((0, 0), wrapped, font=font_poem)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]

    x = (1080 - text_w) / 2
    y = (1080 - text_h) / 2 - 40

    draw.multiline_text(
        (x, y),
        wrapped,
        fill="black",
        font=font_poem,
        align="center"
    )

    draw.text(
        (1080/2, y + text_h + 40),
        f"— {author}",
        fill="black",
        font=font_author,
        anchor="mm"
    )

    filename = os.path.join(OUTPUT_DIR, "poem_image.png")
    img.save(filename)

    return filename

