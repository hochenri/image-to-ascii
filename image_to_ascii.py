from PIL import Image
import PIL
import os

def resize(img, new_width):
    width, height = img.size
    aspect_ratio = height / width / 2 #considering also the aspect ratio of monospace font
    new_height = int(new_width*aspect_ratio)
    resized_image = img.resize((new_width, new_height), PIL.Image.ANTIALIAS) #antialiasing is optional
    return resized_image

def to_grayscale(img):
    return img.convert('L')

def to_ascii(img, width):
    ASCII_CHARS = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    ratio = 255 / (len(ASCII_CHARS) - 1) # 255 is the maximum intensity of a pixel (white)

    pixels = img.getdata()
    characters = ''.join([ASCII_CHARS[round(pixel/ratio)] for pixel in pixels])
    pixel_count = len(characters)
    ascii_image = '\n'.join(characters[i:(i+width)] for i in range(0, pixel_count, width))
    return ascii_image

def to_txt(text, output_path):
    with open(output_path, 'w') as f:
        f.write(text)

# MAIN
if __name__=="main":
    path = os.path.dirname(os.path.realpath(__file__)) + "/"
    input_file = "input.jpg"
    output_file = "ascii_output.txt"

    img = Image.open(path + input_file)

    new_width = 250
    ascii_image = to_ascii(to_grayscale(resize(img, new_width)), new_width)