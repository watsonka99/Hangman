import random

from words import Word


class HangMan:
    incorrect = 0
    guessed = []

    def setup(self):
        # Opens file to read
        file = open('word_list.txt', 'r')
        # picks a random line number
        word_number = random.randint(0, 99)
        i = 0
        # iterates to line number
        for line in file:
            i += 1
            if i == word_number:
                # saves word class within Hangman class
                self.word = Word(line)
                break
        # closes file
        file.close()

    def game(self):
        while True:
            # prints word to guess
            print("\n" * 10)
            print(self.word)
            guess = self.cli()
            check = self.word.guess_letter(guess)
            if not check:
                self.incorrect += 1
                if self.incorrect == 7:
                    print('you lose')
                    # breaks out of while loop to end app
                    break
            else:
                if self.word.win_check():
                    print('congratulations you win')
                    # breaks out of while loop to end app
                    break

    def cli(self):
        legal = False
        while not legal:
            legal = True
            guess = input('Please enter your next guess: ')
            # ensures string is a single letter
            if len(guess) > 1:
                print("Too many letters been inputted")
                legal = False
            elif len(guess) == 0:
                print("0 characters inputted")
                legal = False
            else:
                # checks if letter has been guessed
                for char in self.guessed:
                    if char == guess:
                        print('Letter has been guessed prior')
                        legal = False
        self.guessed.append(guess)
        return guess


if __name__ == '__main__':
    game = HangMan()
    game.setup()
    game.game()