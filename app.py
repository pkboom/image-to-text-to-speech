from dotenv import find_dotenv, load_dotenv
from transformers import pipeline

load_dotenv(find_dotenv())


# img2text
def img2text(url):
    image_to_text = pipeline(
        "image-to-text", model="Salesforce/blip-image-captioning-large"
    )

    text = image_to_text(url)[0]["generated_text"]

    print(text)

    return text


img2text("photo.jpg")

# lim

# text to speech
