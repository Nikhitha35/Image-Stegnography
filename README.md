# Image-Stegnography
This project demonstrates a Python implementation of image steganography, a technique used to hide secret messages within images. Steganography ensures that the existence of the hidden message is concealed.

Features
Encoding: Embedding a secret message into an image file without affecting its visual quality significantly.
Decoding: Extracting the hidden message from the encoded image.
Technologies Used

Python
PIL (Python Imaging Library) or Pillow (a maintained fork of PIL)

Usage
Encoding a Message:
Run the encode.py script.
Provide the image file and the message to be hidden.
The encoded image will be saved as input.png.

Decoding the Message:
Run the decode.py script on the output.png.
The hidden message will be extracted and displayed.
