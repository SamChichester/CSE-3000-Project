import requests
import os
from dotenv import load_dotenv

load_dotenv()

FACEPP_API_KEY = os.environ.get('FACEPP_API_KEY')
FACEPP_API_SECRET = os.environ.get('FACEPP_API_SECRET')


def detect_gender(image_path):
    """
    
    Find the gender from an image

    """

    url = "https://api-us.faceplusplus.com/facepp/v3/detect"

    with open(image_path, 'rb') as image_file:
        files = {'image_file': image_file}
        data = {
            'api_key': FACEPP_API_KEY,
            'api_secret': FACEPP_API_SECRET,
            'return_attributes': 'gender'
        }

        response = requests.post(url, files=files, data=data)
        result = response.json()

        faces = result.get("faces", [])
        if faces:
            gender = faces[0]["attributes"]["gender"]["value"]
            print(f"Detected gender: {gender}")
            return gender

        else:
            print("No face detected.")
            return None


if __name__ == "__main__":
    genders = []

    for num in range(50):
        genders.append(detect_gender(f'images/{num}.png'))

    print(f"%MALE: {genders.count('Male') / len(genders)}")
    print(f"%FEMALE: {genders.count('Female') / len(genders)}")
