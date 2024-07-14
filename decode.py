from PIL import Image

def decode_image(image_path):
    try:
        img = Image.open(image_path)
        print(f"Opened image: {image_path}")
    except FileNotFoundError:
        print(f"File not found: {image_path}")
        return ""
    
    width, height = img.size
    message = ""
    char_bits = []
    
    for row in range(height):
        for col in range(width):
            r, g, b = img.getpixel((col, row))
            
            char_bits.append(r & 1)
            char_bits.append(g & 1)
            char_bits.append(b & 1)
            
            if len(char_bits) >= 8:
                byte = 0
                for bit in char_bits[:8]:
                    byte = (byte << 1) | bit
                if byte == 0:
                    print(f"Decoded message: {message}")
                    return message
                message += chr(byte)
                char_bits = char_bits[8:]
    
    print(f"Decoded message: {message}")
    return message

# Usage example
image_path = input("Enter the path to the encoded image (e.g., /Users/sainikhithakonatham/Desktop/cs1/output.png): ").strip()
decoded_message = decode_image(image_path)
print(f"Decoded message from image: {decoded_message}")
