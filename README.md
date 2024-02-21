# Exif Embedder

Exif Embedder is a Python application designed to embed EXIF data into a series of images. This script creates multiple black images (1x1 pixel) and embeds modified EXIF data into each, incrementing the `DateTimeOriginal` field by one minute for each new image. This tool is useful for testing, forensics, and educational purposes.

## Features

- Automatically generates images with embedded EXIF data.
- Increments `DateTimeOriginal` in EXIF data for each image.
- Saves images with very low quality to minimize disk space usage.

## Prerequisites

Before running Exif Embedder, ensure you have Python 3.x installed on your system. Additionally, you will need the `Pillow` (PIL fork) and `piexif` libraries.

## Installation

1. **Clone or download this repository** to your local machine.

2. **Install required Python packages**. Open your terminal or command prompt and navigate to the directory containing the script. Run the following command to install the necessary libraries:

   ```sh
   pip install Pillow piexif
   ```

## Usage
### Prepare your image: 
Place the image from which you want to copy the EXIF data into the same directory as the script, or note its path.

### Run the script: 
Open a terminal or command prompt, navigate to the script's directory, and run:

   ```sh
    python index.py
   ```
### Customization:

You can modify the image_path variable in the script to point to your specific image file.
Optionally, change the output_folder variable to specify a different directory for the generated images.

## Example
After you've installed the required packages and prepared your image, you can run the script as follows:
   ```sh
    python index.py
   ```
Make sure to replace "example.jpg" with the path to your image in the script's __main__ section.




