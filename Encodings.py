alphabet = ['', '', '', '', '', '', '', '', '', '', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '_', '-']

encoded = ''
decoded = ''


class encode:
    def __init__(self, input):
        global encoded
        encoded = ''
        idx = 0
        for i in range(len(input)):
            letter = input[idx]
            list_index = alphabet.index(letter)
            encoded = encoded + str(list_index)
            idx += 1


class decode:
    def __init__(self, input):
        global decoded
        decoded = ''
        idx = 0
        numbers = []
        while idx < len(input):
            number = int(input[idx:idx + 2])
            numbers.append(number)
            idx += 2

        for num in numbers:
            letter = alphabet[num]
            decoded = decoded + letter

