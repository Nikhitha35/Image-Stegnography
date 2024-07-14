from PIL import Image

def encode_image():
    # Prompt user for input image path
    image_path = input("Enter the path to the input image (e.g., /Users/sainikhithakonatham/Desktop/cs1/input.png): ").strip()
    
    try:
        img = Image.open(image_path)
        print(f"Opened image: {image_path}")
    except FileNotFoundError:
        print(f"File not found: {image_path}")
        return
    
    # Prompt user for message to encode
    message = input("Enter the message to encode: ").strip()
    
    # Prompt user for output image path
    output_path = input("Enter the path to save the output image (e.g., /Users/sainikhithakonatham/Desktop/cs1/output.png): ").strip()
    
    encoded = img.copy()
    width, height = img.size
    index = 0
    
    message += chr(0)  # Add null character to indicate end of message
    message_bits = ''.join([format(ord(char), '08b') for char in message])  # Convert message to binary
    
    print(f"Message to encode: {message}")
    print(f"Message bits: {message_bits}")
    
    for row in range(height):
        for col in range(width):
            if index < len(message_bits):
                r, g, b = img.getpixel((col, row))
                
                r = (r & ~1) | int(message_bits[index])
                index += 1
                if index < len(message_bits):
                    g = (g & ~1) | int(message_bits[index])
                    index += 1
                if index < len(message_bits):
                    b = (b & ~1) | int(message_bits[index])
                    index += 1
                
                encoded.putpixel((col, row), (r, g, b))
    
    encoded.save(output_path)
    print(f"Encoded image saved as: {output_path}")

# Usage example
encode_image()

