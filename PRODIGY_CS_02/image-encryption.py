from PIL import Image

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()
    
    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]
            pixels[i, j] = (
                (r + key) % 256,
                (g + key) % 256,
                (b + key) % 256
            )
    
    img.save(output_path)
    print("Image encrypted and saved as:", output_path)

def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]
            pixels[i, j] = (
                (r - key) % 256,
                (g - key) % 256,
                (b - key) % 256
            )
    
    img.save(output_path)
    print("Image decrypted and saved as:", output_path)

# Example usage:
# encrypt_image('original.png', 'encrypted.png', 50)
# decrypt_image('encrypted.png', 'decrypted.png', 50)
