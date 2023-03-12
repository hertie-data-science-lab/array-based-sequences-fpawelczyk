# Author: Fabian Pawelczyk
# 

class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift

    def encrypt(self, message):
        # Convert message to a list of characters
        chars = list(message)
        # Loop over each character
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
        return encrypted_message

    def decrypt(self, message):
        # Convert message to a list of characters
        chars = list(message)
        # Loop over each character
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
        return decrypted_message


cipher = CaesarCipher(3)
message = "THE EAGLE IS IN PLAY; MEET AT JOE'S"
coded = cipher.encrypt(message)
print("Secret: ", coded)
answer = cipher.decrypt(coded)
print("Message: ", answer)
