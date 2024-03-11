from PIL import Image, ImageFilter
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

path = os.path.join(current_dir, "imgs")
path_out = os.path.join(current_dir, "editedImgs")

if not os.path.exists(path_out):
    os.makedirs(path_out)

for filename in os.listdir(current_dir):
    if filename.lower().endswith(".jpg"):
        img = Image.open(os.path.join(current_dir, filename))

        edit = img.convert('L')  # Convert to black and white (grayscale)

        clean_name = os.path.splitext(filename)[0]
        edited_filename = f"{clean_name}_bw.jpg"
        edit.save(os.path.join(path_out, edited_filename))
