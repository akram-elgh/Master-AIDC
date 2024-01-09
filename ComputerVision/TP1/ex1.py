# import cv2
# import numpy as np

# Read image
# src = cv2.imread('./input.jpg', cv2.IMREAD_UNCHANGED)
# print(src.shape)

# # Extract red channel
# red_channel = src[:, :, 2]

# # Create empty image with same shape as that of src image
# red_img = np.zeros(src.shape)

# # Assign the red channel of src to empty image
# red_img[:, :, 2] = red_channel

# # Save image
# cv2.imwrite('./output.png', red_img)

# method 2 :

from PIL import Image


def extract_red_components(input_path, output_path):
    # Open the image using Pillow
    image = Image.open(input_path)

    # Get the size of the image
    width, height = image.size

    # Create a new blank image with the same size and mode as the original
    red_image = Image.new("RGB", (width, height))

    # Iterate through each pixel and extract the red component
    for x in range(width):
        for y in range(height):
            # Get the pixel color at (x, y)
            pixel_color = image.getpixel((x, y))

            # Create a new pixel with only the red component
            red_pixel = (pixel_color[0], 0, 0)

            # Set the pixel color in the red_image
            red_image.putpixel((x, y), red_pixel)

    # Save the extracted red components as a new image
    red_image.save(output_path)


def extract_green_components(input_path, output_path):
    # Open the image using Pillow
    image = Image.open(input_path)

    # Get the size of the image
    width, height = image.size

    # Create a new blank image with the same size and mode as the original
    green_image = Image.new("RGB", (width, height))

    # Iterate through each pixel and extract the red component
    for x in range(width):
        for y in range(height):
            # Get the pixel color at (x, y)
            pixel_color = image.getpixel((x, y))

            # Create a new pixel with only the red component
            green_pixel = (0, pixel_color[0], 0)

            # Set the pixel color in the red_image
            green_image.putpixel((x, y), green_pixel)

    # Save the extracted red components as a new image
    green_image.save(output_path)


def extract_blue_components(input_path, output_path):
    # Open the image using Pillow
    image = Image.open(input_path)

    # Get the size of the image
    width, height = image.size

    # Create a new blank image with the same size and mode as the original
    blue_image = Image.new("RGB", (width, height))

    # Iterate through each pixel and extract the red component
    for x in range(width):
        for y in range(height):
            # Get the pixel color at (x, y)
            pixel_color = image.getpixel((x, y))

            # Create a new pixel with only the red component
            blue_pixel = (0, 0, pixel_color[0])

            # Set the pixel color in the red_image
            blue_image.putpixel((x, y), blue_pixel)

    # Save the extracted red components as a new image
    blue_image.save(output_path)


# Usage
extract_red_components('input.jpg', 'ouput2_red.jpg')
extract_green_components('input.jpg', 'ouput2_green.jpg')
extract_blue_components('input.jpg', 'ouput2_blue.jpg')
