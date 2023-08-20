import cv2
import json
import random
import os
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import textwrap

script_dir = os.path.dirname(os.path.abspath(__file__))
image_names = [os.path.join(script_dir, 'images', f'image{i}.jpg') for i in range(1, 10)]
used_images = []

def select_image():
    global used_images
    if len(used_images) == 10:
        used_images = []
    selected_image = random.choice([img for img in image_names if img not in used_images])
    used_images.append(selected_image)
    return selected_image

def apply_gaussian_blur(image_path):
    image = cv2.imread(image_path)
    blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

    # Darken the image by scaling down the pixel values
    darken_factor = 0.4  # You can adjust this factor to make the image darker or lighter
    darkened_image = (blurred_image * darken_factor).astype(np.uint8)

    return darkened_image


def write_quote(image, quote, author):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    custom_font_path = os.path.join(script_dir, 'fonts', 'LoveYaLikeASister-Regular.ttf')
    pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pil_image)
    max_width = image.shape[1] - 20

    # Increase the initial font size for bigger text
    font_size = 180
    line_height = 144
    font = ImageFont.truetype(custom_font_path, font_size)
    lines = textwrap.wrap(quote, width=25) # Adjust width for wrapping
    while any(draw.textsize(line, font=font)[0] > max_width for line in lines):
        font_size -= 5
        font = ImageFont.truetype(custom_font_path, font_size)
        line_height = int(font_size * 0.8)
        lines = textwrap.wrap(quote, width=25) # Adjust width for wrapping

    shadow_offset = (2, 2)

    total_text_height = (len(lines) + 1) * line_height # +1 for the author line
    y_start = (image.shape[0] - total_text_height) // 2

    # Write each line with shadow
    for i, line in enumerate(lines):
        textsize = draw.textsize(line, font=font)
        textX = (image.shape[1] - textsize[0]) // 2
        textY = y_start + i * line_height
        draw.text((textX + shadow_offset[0], textY + shadow_offset[1]), line, fill=(0, 0, 0), font=font)
        draw.text((textX, textY), line, fill=(255, 255, 255), font=font)

    # Add extra space for the author and a line
    y_start += len(lines) * line_height + line_height

    # Write the author's name aligned to the right
    author_text = '.' + author
    textsize_author = draw.textsize(author_text, font=font)
    textX_author = image.shape[1] - textsize_author[0] - 20
    textY_author = y_start
    draw.text((textX_author + shadow_offset[0], textY_author + shadow_offset[1]), author_text, fill=(0, 0, 0), font=font)
    draw.text((textX_author, textY_author), author_text, fill=(255, 255, 255), font=font)

    # Convert back to OpenCV image
    image_with_text = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

    return image_with_text


def update_json_files(selected_quote):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    pending_path = os.path.join(script_dir, 'utils', 'pending.json')
    with open(pending_path, 'r') as file:
        pending_quotes = json.load(file)['pending_quotes']
        pending_quotes.remove(selected_quote)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    pending_path = os.path.join(script_dir, 'utils', 'pending.json')
    with open(pending_path, 'w') as file:
        json.dump({'pending_quotes': pending_quotes}, file)

    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        completed_path = os.path.join(script_dir, 'utils', 'completed.json')
        with open(completed_path, 'r') as file:
            completed_quotes = json.load(file)['completed_quotes']
    except:
        completed_quotes = []

    completed_quotes.append(selected_quote)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    completed_path = os.path.join(script_dir, 'utils', 'completed.json')
    with open(completed_path, 'w') as file:
        json.dump({'completed_quotes': completed_quotes}, file)

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    quoted_images_dir = os.path.join(script_dir, 'quoted_images')
    os.makedirs(quoted_images_dir, exist_ok=True)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    pending_path = os.path.join(script_dir, 'utils', 'pending.json')
    with open(pending_path, 'r') as file:
        quotes = json.load(file)['pending_quotes']

    selected_quote = random.choice(quotes)
    selected_image_name = select_image()
    image = apply_gaussian_blur(selected_image_name)
    image_with_quote = write_quote(image, selected_quote['quote'], selected_quote['author'])

    output_path = os.path.join(quoted_images_dir, os.path.basename(selected_image_name))
    cv2.imwrite(output_path, image_with_quote)

    update_json_files(selected_quote)
    print(f"Quote by {selected_quote['author']} applied to {output_path}")

    return output_path # Return the image path

if __name__ == "__main__":
    main()
