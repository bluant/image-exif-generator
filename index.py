from PIL import Image
import piexif
import os
from datetime import datetime, timedelta

def embed_exif_data(image_path, output_folder="IMAGES"):
    try:
        # Create the output folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        for i in range(547):
            # Create a small black image (1x1 pixel)
            new_img = Image.new("RGB", (1, 1), "black")

            # Get Exif data from the original image
            with Image.open(image_path) as img:
                exif_data = piexif.load(img.info.get("exif"))

            # Check if DateTimeOriginal exists in Exif data
            if 36867 in exif_data['Exif']:
                # Increment DateTimeOriginal by 1 minute for each image
                original_datetime = datetime.strptime(exif_data['Exif'][36867].decode(), "%Y:%m:%d %H:%M:%S")
                new_datetime = original_datetime + timedelta(minutes=i)
                exif_data['Exif'][36867] = new_datetime.strftime("%Y:%m:%d %H:%M:%S").encode()

            # Convert Exif data to bytes
            exif_bytes = piexif.dump(exif_data)

            # Save the new image with embedded Exif data and very low quality
            output_path = os.path.join(output_folder, f"output_image_{i + 1}.jpg")
            new_img.save(output_path, "JPEG", quality=1, exif=exif_bytes)
            print(f"Exif data embedded and saved to {output_path}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    image_path = "example.jpg"  # Replace with the actual path to your image
    embed_exif_data(image_path)
