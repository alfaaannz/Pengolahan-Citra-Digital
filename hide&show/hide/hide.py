from PIL import Image

def hide_message_in_image(image_path, output_path):
    img = Image.open('kucing.jpg')
    pixels = list(img.getdata())

    secret_message = input("Masukkan pesan yang akan disembunyikan: ")

    binary_message = ''.join(format(ord(char), '08b') for char in secret_message)

    pixel_index = 0
    for i in range(len(pixels)):
        pixel = list(pixels[i])
        for color_channel in range(3):
            if pixel_index < len(binary_message):
                pixel[color_channel] = int(format(pixel[color_channel], '08b')[:-1] + binary_message[pixel_index], 2)
                pixel_index += 1

        pixels[i] = tuple(pixel)

    img.putdata(pixels)
    img.save(output_path)
    print("Pesan berhasil disembunyikan dalam gambar!")

def reveal_message_in_image(image_path):
    img = Image.open(image_path)
    pixels = list(img.getdata())

    binary_message = ''
    for pixel in pixels:
        for color_channel in range(3):  # R, G, B channels
            binary_message += format(pixel[color_channel], '08b')[-1]

    message = ''
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        message += chr(int(byte, 2))

    return message

image_path = input("Masukkan path gambar: ")
output_path = input("Masukkan path untuk menyimpan gambar dengan pesan tersembunyi: ")

# Sembunyikan pesan dalam gambar
hide_message_in_image(image_path, output_path)