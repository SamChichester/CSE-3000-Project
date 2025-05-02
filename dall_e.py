from openai import OpenAI
import requests
import os
from dotenv import load_dotenv
from prompts import prompts

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
load_dotenv()


def generate_image(prompt, name):
    """
    
    Generate an image using DALL-E

    """

    response = client.images.generate(prompt=prompt,
    n=1,
    size="512x512")
    image_url = response.data[0].url
    print(f"Image URL: {image_url}")

    img_data = requests.get(image_url).content
    image_path = f"images/{prompt}/{name}.png"
    with open(image_path, 'wb') as f:
        f.write(img_data)

    return image_path


if __name__ == "__main__":
    for prompt in prompts:
        for num in range(50):
            generate_image(prompt, num)

        print(f'FINISHED PROMPT: {prompt}')

    print('DONE')
