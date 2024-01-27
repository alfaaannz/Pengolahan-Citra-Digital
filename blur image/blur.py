from PIL import Image, ImageFilter

def blur_image(input_path, output_path):
    image = Image.open(input_path)

    blurred_image = image.filter(ImageFilter.BLUR)
    blurred_image.save(output_path)

    image.show()
    blurred_image.show()

if __name__ == "__main__":
    
    input_image_path = 'beat.jpg'
    output_image_path = 'blurred_beat.jpg'
    blur_image(input_image_path, output_image_path)
