import os
import sys
import re
import ipdb

class WordleCli:

    def __init__(self):
        self.terminal_width = os.get_terminal_size().columns
        self.input_width = self.terminal_width//2
        self.game_over = False
        self.clear_command = 'cls' if os.name == 'nt' else 'clear'
        self.user_tries = 0
        self.words = []
        self.load_dictionary()
        try:
            self.MAX_TRIALS = int(os.getenv('GAME_TRIALS'))
        except:
            self.MAX_TRIALS = 5  
        self.play()
    

    def load_dictionary(self):
        with open("./data/dict.txt") as word_file:
            self.english_words = set(word.strip().lower() for word in word_file)


    def clear(self):
        os.system(self.clear_command)

    def print_qwerty(self):
        qwerty = ['Q W E R T Y U I O P', 'A S D F G H J K L', 'Z X C V B N M']
        for line in qwerty:
            print(line.center(self.terminal_width))

    def refresh_screen(self, message=""):
        sys.stdout.flush()
        self.clear()
        self.print_qwerty()
        print()
        print()
        for w in self.words:
            print(w.center(self.terminal_width))  
        print(message.center(self.terminal_width))    

    def update_game(self):
        self.user_tries += 1
        self.game_over = self.user_tries == self.MAX_TRIALS

    def check_word(self, word):
        if word.lower() in self.english_words:
            self.words.append(word.upper())
            return True
        return False        

    def play(self):
        self.refresh_screen()

        while(not self.game_over):
            word = input("".center(self.input_width))
            error_message = "Words must have 5 characters only"
            if re.findall(r'\b[a-zA-Z]{5}\b',word):
                error_message = "" if self.check_word(word) else "The word doesn't exist in the game's dictionary"
            self.refresh_screen(error_message)
            self.update_game()

        print("GAME FINISHED, YOU".center(self.terminal_width))    
            
            
def main():
    try:
        WordleCli()
    except KeyboardInterrupt:
        exit()


if __name__ == '__main__':
    main()

