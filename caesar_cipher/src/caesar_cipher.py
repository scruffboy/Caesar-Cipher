RUS_UP = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
ENG_UP = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
RUS_LOW = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
ENG_LOW = "abcdefghijklmnopqrstuvwxyz"


class Parameters:
    """Parameters for operations with text"""

    # Initialisation attributes of parameters
    def __init__(self, operation, language, step, text):
        self.operation = operation
        self.language = language
        self.step = step
        self.text = text


class CeaserCipher:
    """The basic logic of the cipher"""

    # Initialisation attributes for cipher
    def __init__(self, parameters: Parameters):
        self.parameters = parameters

    # Function for get language
    def _get_alphabet(self):
        if self.parameters.language in ["rus", "r"]:
            return RUS_UP, RUS_LOW
        elif self.parameters.language in ["eng", "e"]:
            return ENG_UP, ENG_LOW

    # Function for calculate new index of char
    def _calculate_index(self, alphabet, char, operation):
        current_index = alphabet.index(char)

        if operation in ["encrypt", "en"]:
            return (current_index + self.parameters.step) % len(alphabet)
        else:  # decrypt
            return (current_index - self.parameters.step) % len(alphabet)

    # Main function for encrypt or decrypt
    def encrypt_decrypt(self):
        result = ""
        alphabet_up, alphabet_low = self._get_alphabet()

        for char in self.parameters.text:
            if char in alphabet_up:
                new_idx = self._calculate_index(
                    alphabet_up, char, self.parameters.operation
                )
                result += alphabet_up[new_idx]

            elif char in alphabet_low:
                new_idx = self._calculate_index(
                    alphabet_low, char, self.parameters.operation
                )
                result += alphabet_low[new_idx]

            else:
                result += char  # save other symbols

        return result


class ParametersReader:
    """Get of parameters by user"""

    # Function for collecting parameters
    @staticmethod
    def get_parameters():
        while True:
            operation = input(
                "Enter the operation you need to do: (encrypt/decrypt)"
            ).lower()
            if operation not in ["encrypt", "en", "decrypt", "de"]:
                print("Operation must to be 'encrypt' or 'decrypt'")
                continue

            language = input("Enter the language of text: (rus/eng)").lower()
            if language not in ["rus", "eng", "r", "e"]:
                print("Language must to be 'rus' or 'eng'")
                continue

            try:
                step = int(input("Enter the step of shift: "))
            except ValueError:
                print("Enter a valid value!")
                continue

            text = input("Enter the text: ")
            if not text:
                print("Text can't be empty")
                continue

            print("Data was collected!")
            return Parameters(operation, language, step, text)


def main():
    """Main logic of program"""

    print("Hello, we're glad to see you on the program 'Ceaser Cipher'!")
    print("We need to collect parameters for run program")

    # Parameters object
    params = ParametersReader.get_parameters()

    # Cipher object
    cipher = CeaserCipher(params)

    # Result of program
    result = cipher.encrypt_decrypt()

    print(f"Result: {result}")


if __name__ == "__main__":
    main()
