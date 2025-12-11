from random import choice
import textwrap


# Class for generating text based on a Markov chain
class TextGenerator:
    def __init__(self, filename):
        self.possible_chars = dict()

        # Build the dictionary of possible word transitions from the text file
        # (word1, word2) -> [list of possible next words]
        w1 = ''
        w2 = ''
        with open(filename, 'r') as f:
            for line in f:
                for char in line:
                    key = (w1, w2)
                    if key not in self.possible_chars:
                        self.possible_chars[key] = [char]
                    else:
                        self.possible_chars[key].append(char)
                    w1, w2 = w2, char


    # Generate text of a given word count
    def generate_text(self, word_count=50):
        # Start with a random word pair where the first word has at least one letter and starts with a capital letter
        w1, w2 = choice([k for k in self.possible_chars])
        text = ""
        for _ in range(word_count):
            text += w1
            next_word = choice(self.possible_chars[(w1, w2)])  # Randomly choose the next word based on the current pair
            w1, w2 = w2, next_word  # word2 becomes word1, next_word becomes word2
        return textwrap.fill(text)  # Format the text to fit within 70 characters per line (readability)


virtual_lewis_carroll = TextGenerator('data.txt')
print(virtual_lewis_carroll.generate_text(1000))