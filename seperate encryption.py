import cv2
import os
import string

def encrypt_message(image_path, output_path, message, password):
    img = cv2.imread(image_path)  # Load the image

    d = {chr(i): i for i in range(255)}  # ASCII to pixel value mapping

    n, m, z = 0, 0, 0

    for char in message:
        img[n, m, z] = d[char]
        n += 1
        m += 1
        z = (z + 1) % 3  # Loop over RGB channels

    cv2.imwrite(output_path, img)
    os.system(f"start {output_path}")  # Open encrypted image (Windows)

# Example usage
if __name__ == "__main__":
    img_path = input("Enter image path: ")
    output_img = "encryptedImage.jpg"
    secret_msg = input("Enter secret message: ")
    passcode = input("Enter a passcode: ")
    
    encrypt_message(img_path, output_img, secret_msg, passcode)
    print("Encryption completed! Image saved as", output_img)
