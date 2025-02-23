import cv2

def decrypt_message(image_path, original_message_length, password, correct_password):
    img = cv2.imread(image_path)

    if password != correct_password:
        print("Access Denied! Incorrect password.")
        return

    c = {i: chr(i) for i in range(255)}  # Pixel value to ASCII mapping

    message = ""
    n, m, z = 0, 0, 0

    for _ in range(original_message_length):
        message += c[img[n, m, z]]
        n += 1
        m += 1
        z = (z + 1) % 3  # Loop over RGB channels

    print("Decrypted message:", message)

# Example usage
if __name__ == "__main__":
    img_path = input("Enter encrypted image path: ")
    msg_length = int(input("Enter length of original message: "))
    passcode = input("Enter passcode for decryption: ")
    correct_passcode = input("Enter the correct passcode (from encryption): ")

    decrypt_message(img_path, msg_length, passcode, correct_passcode)
