def generate_caption(poem, author, tone):
    caption = f"""{poem}

— {author}

Tone: {tone}

#poetry #poems #quotes #writing #literature
"""
    return caption


if __name__ == "__main__":
    sample_poem = "Comfort is the enemy of growth."
    print(generate_caption(sample_poem, "Unknown", "motivational"))
