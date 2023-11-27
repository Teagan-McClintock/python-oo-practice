from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self,filepath):
        """Creates wordlist after reading file and prints # of words in file"""

        self.filepath = filepath

        self.wordlist = self.get_wordlist()

        print(f"{len(self.wordlist)} words read")


    def __repr__(self):
        repr_string = f"<{self.__class__.__name__} filepath={self.filepath} "
        repr_string += f"wordlist Length = {len(self.wordlist)}>"
        return repr_string

    def get_wordlist(self):
        """Reads file and returns a wordlist of all words in file."""

        file = open(self.filepath, "r")
        wordlist = []

        for line in file:
            wordlist.append(line.strip())

        file.close()

        return wordlist


    def random(self):
        """Choose and returns a random word from the wordlist"""

        return choice(self.wordlist)


class SpecialWordFinder(WordFinder):
    """SpecialWordFinder: finds random words from a text file, ignoring
        blanks and comments (that start with #)"""

    def get_wordlist(self):
        """Reads file and returns a wordlist of all words in file except blank
            lines and lines that begin with #."""

        # wordlist = super().__readfile__()
        return [word for word in super().get_wordlist()
                if len(word) > 0 and not word.startswith('#')]
        # return trimmed_wordlist