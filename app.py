from dotenv import find_dotenv, load_dotenv
from transformers import pipeline

load_dotenv(find_dotenv())


def img2text(path):
    image_to_text = pipeline(
        "image-to-text", model="Salesforce/blip-image-captioning-large"
    )

    text = image_to_text(path)[0]["generated_text"]

    print(text)

    return text


img2text("hambuger.png")
# img2text("photo.jpg")

# lim

# text to speech
