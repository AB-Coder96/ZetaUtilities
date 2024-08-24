import os
from PIL import Image

def convert_webp_to_jpg(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".webp"):
            webp_path = os.path.join(directory, filename)
            jpg_path = os.path.join(directory, filename.replace(".webp", ".jpg"))
            with Image.open(webp_path) as img:
                img = img.convert("RGB")  # Convert to RGB before saving as JPG
                img.save(jpg_path)
            print(f"Converted {filename} to {jpg_path}")

if __name__ == "__main__":
    current_directory = os.path.dirname(os.path.abspath(__file__))
    convert_webp_to_jpg(current_directory)