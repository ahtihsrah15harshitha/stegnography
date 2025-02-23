import cv2

def decrypt_message(image_path, original_message_length, password, correct_password):
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Unable to load the image. Check the file path and format.")
        return None

    if password != correct_password:
        print("Access Denied! Incorrect password.")
        return None

    c = {i: chr(i) for i in range(32, 127)}  # Only valid ASCII characters

    message = ""
    n, m, z = 0, 0, 0

    if original_message_length > img.shape[0] * img.shape[1] * 3:
        print("Error: Message length is too long for this image.")
        return None

    for _ in range(original_message_length):
        pixel_value = img[n, m, z]
        message += c.get(pixel_value, "?")  # Use '?' for unrecognized values
        n += 1
        m += 1
        z = (z + 1) % 3

    return message

# Example usage
if __name__ == "__main__":
    img_path = input("Enter encrypted image path: ")
    msg_length = int(input("Enter length of original message: "))
    passcode = input("Enter passcode for decryption: ")
    correct_passcode = input("Enter the correct passcode (from encryption): ")

    decrypted_msg = decrypt_message(img_path, msg_length, passcode, correct_passcode)
    if decrypted_msg:
        print("Decrypted message:", decrypted_msg)
        print([ord(c) for c in decrypted_msg])  


