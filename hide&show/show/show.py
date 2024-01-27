from PIL import Image

def show_image(image_path):
    img = Image.open(image_path)
    img.show()

output_path = input("Masukkan path gambar dengan pesan tersembunyi: ")

show_image(output_path)