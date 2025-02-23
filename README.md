# stegnography
message encryption/decryption
Secure Data Hiding in Images Using Steganography
Overview
This project implements image-based steganography using Python and OpenCV. It allows users to hide secret messages within images while ensuring secure and discreet communication. The encryption process modifies pixel values to embed text, and the decryption process retrieves the hidden message when the correct password is provided.

Features
Secure Encryption: Hides messages inside images without noticeable changes.
Password Protection: Ensures only authorized users can decrypt the hidden message.
Minimal Image Distortion: Maintains the quality of the image after encryption.
Requirements
Python 3.x
OpenCV (cv2)
Install dependencies using:

bash
pip install opencv-python

Usage
Encryption

Run seperate_encryption.py and provide:
Path to the image
Secret message
Password for encryption
The encrypted image will be saved as "encryptedImage.jpg".
Run the script:

bash

python seperate_encryption.py
Decryption
Run seperate_dycryption.py and provide:
Path to the encrypted image
Length of the original message
Password used during encryption
If the password is correct, the hidden message will be revealed.
Run the script:

bash
python seperate_dycryption.py



Applications
Cybersecurity Professionals: Securely transmit sensitive data.
Journalists & Activists: Communicate safely in surveillance-heavy environments.
General Users: Hide confidential information within images for privacy.
Future Enhancements
Improve security by using more advanced encryption algorithms.
Support for multiple file formats (e.g., PNG, BMP).
Implement graphical user interface (GUI) for easier use.
