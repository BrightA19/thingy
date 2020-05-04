class StringUtility:
    def __init__(self, string):
        self.originalString = string

    def __str__(self):
        return self.originalString

    def vowels(self):
        '''
        Counts the amount of vowels present. Returns "many" if more than 5
        return: (str) The amount of vowels present
        '''

        VOWELS = "aeiou"
        lowercase_string = self.originalString.lower()
        vowelCount = 0

        for character in lowercase_string:
            if character in VOWELS:
                vowelCount += 1

        if vowelCount < 5:
            return str(vowelCount)
        else:
            return "many"

    def bothEnds(self):
        '''
        Creates a string with the first and last two characters, or nothing
        if the original string isn't large enough
        return: (str) A string with 4 or 0 characters
        '''

        if len(self.originalString) <= 2:
            return ""

        return self.originalString[0] + self.originalString[1]\
            + self.originalString[-2] + self.originalString[-1]

    def fixStart(self):
        '''
        Replaces all instances of the first character, except the first
        return: (str) The resulting string
        '''

        if len(self.originalString) == 0:
            return ""

        newString = ""
        firstCharacter = self.originalString[0]
        isFirstCharacter = True

        for character in self.originalString:
            if isFirstCharacter:
                newString += character
                isFirstCharacter = False
                continue

            newString += ("*" if character is firstCharacter else character)

        return newString

    def asciiSum(self):
        '''
        Adds up the ASCII value of all the characters in the original string
        return: (int) The total ascii value
        '''

        asciiTotalSum = 0

        for character in self.originalString:
            asciiTotalSum += ord(character)

        return asciiTotalSum

    def cipher(self):
        '''
        Encodes the original string by shifting its letters by how long the
        original string is
        return: (str) The encoded string
        '''

        LOWERCASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"
        UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        newString = ""

        for character in self.originalString:
            if character in LOWERCASE_LETTERS:
                letters = LOWERCASE_LETTERS
            elif character in UPPERCASE_LETTERS:
                letters = UPPERCASE_LETTERS
            else:
                newString += character
                continue

            # Shift the letters by the original string's length
            # If it passes z, it loops back to the beginning (Ex. Y + 2 = A)
            index = letters.find(character)
            newIndex = index + len(self.originalString)
            newIndex -= len(letters)\
                * (len(self.originalString) // len(letters)) + len(letters)

            newCharacter = letters[newIndex]
            newString += newCharacter

        return newString
