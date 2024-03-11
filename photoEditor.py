from PIL import Image, ImageFilter
import os

# Get the current directory where the script is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define the input and output directories relative to the current directory
path = os.path.join(current_dir, "imgs")
path_out = os.path.join(current_dir, "editedImgs")

# Check if the output directory exists, create it if not
if not os.path.exists(path_out):
    os.makedirs(path_out)

# Iterate over each file in the current directory
for filename in os.listdir(current_dir):
    # Check if the file is a JPG image
    if filename.lower().endswith(".jpg"):
        # Open the image
        img = Image.open(os.path.join(current_dir, filename))

        # Apply image editing operations
        edit = img.convert('L')  # Convert to black and white (grayscale)

        # Save the edited image as JPG
        clean_name = os.path.splitext(filename)[0]
        edited_filename = f"{clean_name}_bw.jpg"
        edit.save(os.path.join(path_out, edited_filename))
