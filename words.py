class Word:

    def __init__(self, word):
        self.word = word
        # conerst word to a list of '*'
        self.unknown_word = ['*' for letter in word if letter != '\n']

    def __str__(self):
        # converts list to String to print
        output = ''
        for char in self.unknown_word:
            output += char
        return output

    def guess_letter(self, character):
        """
        Method to check if a given letter is included within a word

        :param character: a single character
        :return: if a letter has been found
        """
        i = 0
        letter_found = False
        for letter in self.word:
            if character == letter:
                self.unknown_word[i] = character
                letter_found = True
                i += 1
            else:
                i += 1
        if letter_found:
            return True
        else:
            return False

    def win_check(self):
        """
        A method to check if a word has been guessed

        :return: if all the letters have been guessed
        """
        for i in range(0, len(self.unknown_word)):
            if self.word[i] != self.unknown_word[i]:
                return False
        return True
