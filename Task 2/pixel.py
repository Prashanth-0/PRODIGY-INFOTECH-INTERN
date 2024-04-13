from PIL import Image

def encrypt_image(image_path, key):
    try:
        image = Image.open(image_path)
        encrypted_image = Image.new(image.mode, image.size)
        width, height = image.size

        # Define separate encryption multipliers for each color channel
        multiplier_red = 5  # Increase the multiplier for more vibrant red colors
        multiplier_green = 2
        multiplier_blue = 3

        for i in range(width):
            for j in range(height):
                pixel = image.getpixel((i, j))
                red = (pixel[0] + key * multiplier_red) % 256
                green = (pixel[1] + key * multiplier_green) % 256
                blue = (pixel[2] + key * multiplier_blue) % 256
                new_pixel = (red, green, blue)
                encrypted_image.putpixel((i, j), new_pixel)

        encrypted_image.save("encrypted_image.png")
        print("Image encrypted successfully!")
    except Exception as e:
        print("Error during encryption:", e)

def decrypt_image(encrypted_image_path, key):
    try:
        encrypted_image = Image.open(encrypted_image_path)
        decrypted_image = Image.new(encrypted_image.mode, encrypted_image.size)
        width, height = encrypted_image.size

        # Define separate decryption multipliers for each color channel
        multiplier_red = 5  # Use the same multipliers for decryption
        multiplier_green = 2
        multiplier_blue = 3

        for i in range(width):
            for j in range(height):
                pixel = encrypted_image.getpixel((i, j))
                red = (pixel[0] - key * multiplier_red) % 256
                green = (pixel[1] - key * multiplier_green) % 256
                blue = (pixel[2] - key * multiplier_blue) % 256
                new_pixel = (red, green, blue)
                decrypted_image.putpixel((i, j), new_pixel)

        decrypted_image.save("decrypted_image.png")
        print("Image decrypted successfully!")
    except Exception as e:
        print("Error during decryption:", e)

# Take user input for image path and key with error handling
try:
    image_path = input("Enter the path to the image file: ")
    key = int(input("Enter the encryption key (an integer): "))

    # Encrypt the image
    encrypt_image(image_path, key)

    # Take user input for decryption key with error handling
    while True:
        try:
            decrypt_key = int(input("Enter the decryption key (an integer): "))
            decrypt_image("encrypted_image.png", decrypt_key)
            break  # Exit the loop if decryption is successful
        except ValueError:
            print("Please enter a valid integer for the decryption key.")
except Exception as e:
    print("Error:", e)