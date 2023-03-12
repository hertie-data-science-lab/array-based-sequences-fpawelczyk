"""
Date: Feb 19th 2023
@author: Juan Pablo Brasdefer (juanbrasdefer) Fabian Pawelczyk (fpawelczyk)
"""


class CaesarCipher:
    def __init__(self, shift):
        # Initialize the class with a given shift value
        self.shift = shift

    def encrypt(self, message):
        # Convert message to a list of characters
        chars = list(message)
        # Loop over each character in the list
        for i in range(len(chars)):
            # Check if the character is a letter
            if chars[i].isalpha():
                # Convert to uppercase for ease of calculation
                if chars[i].islower():
                    chars[i] = chars[i].upper()
                    lower_case = True
                else:
                    lower_case = False
                # Shift the character by the given amount
                chars[i] = chr((ord(chars[i]) - 65 + self.shift) % 26 + 65)
                # Convert back to lowercase if necessary
                if lower_case:
                    chars[i] = chars[i].lower()
        # Join the list of characters back into a string
        encrypted_message = ''.join(chars)
        # Return the encrypted message
        return encrypted_message

    def decrypt(self, message):
        # Convert message to a list of characters
        chars = list(message)
        # Loop over each character in the list
        for i in range(len(chars)):
            # Check if the character is a letter
            if chars[i].isalpha():
                # Convert to uppercase for ease of calculation
                if chars[i].islower():
                    chars[i] = chars[i].upper()
                    lower_case = True
                else:
                    lower_case = False
                # Shift the character by the opposite amount
                chars[i] = chr((ord(chars[i]) - 65 - self.shift) % 26 + 65)
                # Convert back to lowercase if necessary
                if lower_case:
                    chars[i] = chars[i].lower()
        # Join the list of characters back into a string
        decrypted_message = ''.join(chars)
        # Return the decrypted message
        return decrypted_message

    def set_shift(self, new_shift):
        # Set a new shift value
        self.shift = new_shift

    def get_shift(self):
        # Get the current shift value
        return self.shift


# Create an instance of the CaesarCipher class with a shift value of 3
cipher = CaesarCipher(3)

# Encrypt a message using the created cipher
message = "THE EAGLE IS IN PLAY; MEET AT JOE'S"
coded = cipher.encrypt(message)
print("Secret: ", coded)

# Decrypt the encrypted message using the same cipher
answer = cipher.decrypt(coded)
print("Message: ", answer)

# Change the shift value to 5
cipher.set_shift(5)

# Encrypt a new message using the updated cipher
new_message = "HELLO, WORLD!"
new_coded = cipher.encrypt(new_message)
print("Secret: ", new_coded)

# Get the current shift value of the cipher
current_shift = cipher.get_shift()
print("Current shift value: ", current_shift)



cipher = CaesarCipher(3)
message = "THE EAGLE IS IN PLAY; MEET AT JOE'S"
coded = cipher.encrypt(message)
print("Secret: ", coded)
answer = cipher.decrypt(coded)
print("Message: ", answer)
