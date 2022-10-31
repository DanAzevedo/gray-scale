from PIL import Image
import os

image_path = "grayscale_images"
if image_path not in os.listdir():
    os.mkdir(image_path)

files_path = "fotos"
files = [i for i in os.listdir(files_path) if ".jpg" in i]

for file in files:
    file_path = os.path.join(files_path, file)
    new_path = os.path.join(image_path, file)

    img = Image.open(file_path).convert("L")
    img.save(new_path, "JPEG")
