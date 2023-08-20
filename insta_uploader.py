from instagrapi import Client
from dotenv import load_dotenv
import os
load_dotenv()
USERNAME=os.getenv('USERNAME')
PASSWORD=os.getenv('PASSWORD')
def upload_image_to_instagram(image_path, description="Capturing the essence of love in all its forms. From the electrifying jolt of love at first sight to the enduring warmth of true love, every moment is a testament to the power of the heart. Distance only makes the heart grow fonder. ❤️ #Love #LoveAtFirstSight #FirstLove #UnconditionalLove #TrueLove #LongDistanceLove #HeartfeltMoments #LoveJourney #EndlessLove #LoveWithoutBorders"):
    # Initialize the client
    username = USERNAME 
    password = PASSWORD
    cl = Client()
    cl.login(username, password)

    # Upload the image with the description
    cl.photo_upload(image_path, caption=description)

