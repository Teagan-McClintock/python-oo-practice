from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self,filepath):
        """Creates wordlist after reading file and prints # of words in file"""

        self.filepath = filepath

        self.wordlist = self.__readfile__()

        print(f"{len(self.wordlist)} words read")


    def __repr__(self):
        return (
        f"<WordFinder filepath={self.filepath} wordlist = {self.wordlist}>"
        )

    def __readfile__(self):
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


