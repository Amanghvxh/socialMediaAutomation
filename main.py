#!/usr/bin/env python3


import json
import os
# from data_generation import generateData
from prepare_image import main as prepare_image
from insta_uploader import upload_image_to_instagram

# def check_pending_quotes():
#     try:
#         with open('./utils/pending.json', 'r') as file:
#             pending_quotes = json.load(file)['pending_quotes']
#             if len(pending_quotes) > 0:
#                 return pending_quotes[0]
#             else:
#                 return None
#     except FileNotFoundError:
#         return None

# def generate_pending_quotes():
#     print("Generating pending quotes...")
#     generateData()

def create_image():
    print("Creating image with quote...")
    return prepare_image() # Return the image path

def upload_image(image_path):
    print("Uploading image to Instagram...")
    description = "Capturing the essence of love in all its forms. From the electrifying jolt of love at first sight to the enduring warmth of true love, every moment is a testament to the power of the heart. Distance only makes the heart grow fonder. ❤️ #Love #LoveAtFirstSight #FirstLove #UnconditionalLove #TrueLove #LongDistanceLove #HeartfeltMoments #LoveJourney #EndlessLove #LoveWithoutBorders" 
    upload_image_to_instagram(image_path, description)

def main():
    # Check if there are pending quotes
    # quote = check_pending_quotes()
    # if quote is None:
    #     # If no pending quotes, generate new quotes
    #     generate_pending_quotes()
    #     quote = check_pending_quotes()

    # # If still no quote, there might be an error in generation
    # if quote is None:
    #     print("Error generating quotes. Please try again.")
    #     return

    # Create an image with the quote
    image_path = create_image()

    # Upload the image to Instagram
    upload_image(image_path)

    # Delete the generated image from the system
    try:
        os.remove(image_path)
        print(f"Image {image_path} deleted successfully.")
    except Exception as e:
        print(f"Error deleting image {image_path}: {e}")

if __name__ == "__main__":
    main()
