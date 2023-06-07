from PIL import Image
import glob

# Get a list of PNG files in the directory
png_files = glob.glob("F:/WORK/Python Work/Image_Converter/Images/*.png")

# Loop through each PNG file and convert it to WebP
for png_file in png_files:
    # Open the PNG image
    image = Image.open(png_file)

    # Generate the output WebP filename by replacing the extension
    webp_file = png_file.replace(".png", ".webp")

    # Convert the image to WebP format and save
    image.save(webp_file, "WEBP")
