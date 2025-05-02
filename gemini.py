import google.generativeai as genai
import os
from dotenv import load_dotenv
from prompts import prompts

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_image(prompt, name):
    """

    Generate an image using Gemini (Google Generative AI)

    """

    model = genai.GenerativeModel("image")

    try:
        response = model.generate_image(prompt)
        image_bytes = response.image
        image_path = f"images/{prompt}/{name}.png"

        os.makedirs(os.path.dirname(image_path), exist_ok=True)

        with open(image_path, "wb") as f:
            f.write(image_bytes)

        print(f"Saved image: {image_path}")
        return image_path

    except Exception as e:
        print(f"Failed to generate image for prompt '{prompt}': {e}")
        return None


if __name__ == "__main__":
    for prompt in prompts:
        for num in range(50):
            generate_image(prompt, num)

        print(f'FINISHED PROMPT: {prompt}')

    print('DONE')
