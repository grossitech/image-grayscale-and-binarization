"""
Filename: image_processor.py
Author:   Luciano Grossi
Date:     August 19, 2025

Description:
This script performs fundamental image processing tasks as a demonstration of
manual, pixel-by-pixel manipulation. It downloads an image from a URL,
converts it to grayscale using the luminosity method, and then binarizes it
based on a set threshold.

The core image processing logic is implemented "from scratch" using standard
Python loops and data structures, intentionally avoiding high-level functions
from libraries like OpenCV or Scikit-Image for the processing steps.
The Pillow (PIL) library is used only for the essential tasks of loading the
initial image from a byte stream and saving the resulting processed images.

How to run:
1. Ensure you have the necessary libraries: pip install Pillow requests
2. Execute the script from your terminal: python image_processor.py
"""

# --- STEP 1: Import Libraries ---
from PIL import Image
import requests
import io
import os # <-- Library added to handle file paths and names

# --- STEP 2: Load the Original Image and Get Filename ---
# Let´s use the famous Lenna image from Wikipedia, but you can change the URL to any image you like.
url = "https://upload.wikimedia.org/wikipedia/en/thumb/7/7d/Lenna_%28test_image%29.png/250px-Lenna_%28test_image%29.png"

# --- Extract base filename from URL ---
# os.path.basename gets the last part of the URL (the filename)
filename_with_ext = os.path.basename(url)
# os.path.splitext splits the filename into its base and extension
filename_base, file_extension = os.path.splitext(filename_with_ext)

try:
    print("Downloading the image...")
    response = requests.get(url)
    response.raise_for_status()
    original_image = Image.open(io.BytesIO(response.content)).convert('RGB')
    width, height = original_image.size
    print(f"Original image '{filename_with_ext}' of {width}x{height} pixels loaded successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
    exit()

# --- STEP 3: Convert to Grayscale (MANUAL) ---
print("Starting grayscale conversion...")

grayscale_image = Image.new('L', (width, height))

for x in range(width):
    for y in range(height):
        r, g, b = original_image.getpixel((x, y))
        gray_value = int(0.299 * r + 0.587 * g + 0.114 * b)
        grayscale_image.putpixel((x, y), gray_value)

print("Grayscale conversion complete.")

# --- STEP 4: Binarize the Image (MANUAL) ---
print("Starting binarization...")

binary_image = Image.new('L', (width, height))
threshold = 127

for x in range(width):
    for y in range(height):
        gray_value = grayscale_image.getpixel((x, y))
        
        if gray_value > threshold:
            binary_pixel = 255 # White
        else:
            binary_pixel = 0   # Black
            
        binary_image.putpixel((x, y), binary_pixel)

print("Binarization complete.")

# --- STEP 5: Save and Display the Results with Dynamic Names ---

# --- NEW: Create dynamic filenames ---
grayscale_filename = f"{filename_base}_grayscale{file_extension}"
binary_filename = f"{filename_base}_binary{file_extension}"

# The files will be saved in the same directory as the .py script
grayscale_image.save(grayscale_filename)
binary_image.save(binary_filename)

# --- UPDATED: Print statement uses the new dynamic names ---
print(f"\nProcessed images saved successfully as '{grayscale_filename}' and '{binary_filename}'")

# Display the images by opening them with the default system viewer
print("Displaying images...")
original_image.show(title="Original Image")
grayscale_image.show(title="Grayscale Image")
binary_image.show(title="Binary Image")