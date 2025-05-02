import os
import requests
from dotenv import load_dotenv
from prompts import prompts

load_dotenv()

ADOBE_CLIENT_ID = os.getenv("ADOBE_CLIENT_ID")
ADOBE_CLIENT_SECRET = os.getenv("ADOBE_CLIENT_SECRET")
ADOBE_REFRESH_TOKEN = os.getenv("ADOBE_REFRESH_TOKEN")

def get_adobe_access_token():
    """

    Get an access token using Adobe's OAuth refresh token flow

    """
    url = "https://ims-na1.adobelogin.com/ims/token"
    data = {
        "client_id": ADOBE_CLIENT_ID,
        "client_secret": ADOBE_CLIENT_SECRET,
        "grant_type": "refresh_token",
        "refresh_token": ADOBE_REFRESH_TOKEN
    }

    response = requests.post(url, data=data)
    response.raise_for_status()
    return response.json()["access_token"]

def generate_image(prompt, name, access_token):
    """
    Generate an image using Adobe Firefly API
    """
    headers = {
        "Authorization": f"Bearer {access_token}",
        "x-api-key": ADOBE_CLIENT_ID,
        "Content-Type": "application/json"
    }

    data = {
        "prompt": prompt,
        "output_format": "png",
        "aspect_ratio": "1:1"
    }

    url = "https://firefly.adobe.io/v2/image/generate"

    response = requests.post(url, headers=headers, json=data)
    if response.status_code != 200:
        print(f"Error generating image: {response.status_code} - {response.text}")
        return None

    result = response.json()
    image_url = result["image_url"]

    img_data = requests.get(image_url).content
    image_path = f"images/{prompt}/{name}.png"
    os.makedirs(os.path.dirname(image_path), exist_ok=True)

    with open(image_path, "wb") as f:
        f.write(img_data)

    print(f"Saved image: {image_path}")
    return image_path


if __name__ == "__main__":
    access_token = get_adobe_access_token()

    for prompt in prompts:
        for num in range(50):
            generate_image(prompt, num, access_token)

        print(f'FINISHED PROMPT: {prompt}')

    print('DONE')
