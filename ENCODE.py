class Encode:
    def __init__(self):
        self.word = ""
        self.length = 0
        self.new_word = ""

    def accept_word(self):
        self.word = input("Enter a word: ")
        self.length = len(self.word)

    def encode_word(self):
        self.new_word = list(self.word)  

        for i in range(self.length):
            if self.word[i].isalpha():
                if self.word[i] == 'Z':
                    self.new_word[i] = 'A'
                elif self.word[i] == 'z':
                    self.new_word[i] = 'a'
                else:
                    self.new_word[i] = chr(ord(self.word[i]) + 1)

        self.new_word = ''.join(self.new_word)  

    def display(self):
        print("O word:", self.word)
        print("E word:", self.new_word)

def main():
    s = Encode()
    s.accept_word()
    s.encode_word()
    s.display()

if __name__ == "__main__":
    main()
