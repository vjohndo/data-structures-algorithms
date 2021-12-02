class CaesarCipher:
    """Class for encryption and decryption of the casesar cypher"""

    def __init__(self, shift):
        """Construct caesar cypher using integer shift for rotation"""

        # Start by initialising the encoder and decoder lists
        # We know that these will be constant so to avoid cost associated with resizing the array
        # Let's create them all at 26
        encoder = [None] * 26
        decoder = [None] * 26

        # Create a for loop from 0 --> 25.
        # then create a cypher using the shift
        for k in range(26):
            encoder[k] = chr((k + shift)%26 + ord("A"))
            decoder[k] = chr((k - shift)%26 + ord("A"))

        # Join the encoder and decoder as a string
        # Remember that += on a string will cause it's reconstruction as it's immutable.
        self._forward = ''.join(encoder)
        self._backward = ''.join(decoder)
    
    def encrypt(self, message):
        """Return string representing encrypted message"""
        return self._transform(message, self._forward)

    def decrypt(self, message):
        """Return string representing decrypted message"""
        return self._transform(message, self._backward)

    
    def _transform(self, original, code):
        """Utility to perform transformation on original string and given code"""

        # Pass the original message into a list, we want to iterate through and edit 
        msg = list(original)

        # Iterate through the list, we want to get the right encypted letter for each character
        for k in range(len(msg)):

            # Only call the cypher is the item is a number
            if msg[k].isupper():

                # Get a O -> 25 representing the original message as number for 
                j = ord(msg[k]) - ord('A')

                # set item as
                msg[k] = code[j]
            
        return ''.join(msg)
    
if __name__ == '__main__':
    cipher = CaesarCipher(3)
    message = "THE EAGLE IS IN PLAY; MEET AT JOE S." 
    coded = cipher.encrypt(message)
    print('Secret: ', coded)
    answer = cipher.decrypt(coded)
    print('Message: ', answer)


            

