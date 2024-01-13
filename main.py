import pygame
import requests
from bs4 import BeautifulSoup
import re
import random
import math

def main():

    # game = GameEngine()
    # game.run()
    

    while True:
        artist = "".join(input("Enter artist: ").split(" ")).lower()
        song = "".join(input("Enter song: ").split(" ")).lower()
        song = Song(artist, song)
        if song.lyrics == "Error 404":
            print("Sorry, couldn't find the song - Please select another")
        else:
            break
    print("\n")

    # for line in song.lyrics:
    #     print(" ".join(line))

    ##TODO: SELECT A LINE AND REMOVE WORDS BUT SAVE WHAT THEY WERE FOR GUESSING
    
    for i in range(10):
        random.choice(song.lyrics)
        selected_lyrics = (random.choice(song.lyrics))
        amount_of_lyris_to_replace = math.ceil(len(selected_lyrics) / 3.3)

        # print(selected_lyrics)
        # print(amount_of_lyris_to_replace)
        indexs_to_replace = {}

        while len(indexs_to_replace) < amount_of_lyris_to_replace:
            index = random.randint(0, len(selected_lyrics) - 1)
            if index not in indexs_to_replace:
                indexs_to_replace[index] = selected_lyrics[index]

        for index in indexs_to_replace:
            selected_lyrics[index] = "_" * len(selected_lyrics[index])

        print(" ".join(selected_lyrics))

    





class GameEngine:
    def __init__(self):
        pygame.init()
        self.width = 1280
        self.height = 720
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.running = True
        pygame.display.set_caption("Lyric Guesser")
        self.background = pygame.image.load("Images/TS_Eras_Tour.jpg")

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        pass

    def render(self):
        self.screen.fill("white")
        self.screen.blit(self.background, (0, 0))
        text = self.create_text("Taylor Swift Lyric Guesser", ("gold"), "Arial", 72)
        text_rect = text.get_rect(center=(self.width // 2 + 50, self.height - self.height + 100))
        self.screen.blit(text, text_rect)
        pygame.display.flip()

    def create_text(self, text, color, font, size):
        font = pygame.font.SysFont(font, size)
        text = font.render(text, True, color)
        return text

class Song:
    def __init__(self, artist, song_name):
        self.artist = artist
        self.song_name = song_name
        self.lyrics = self.get_lyrics()
    
    def get_lyrics(self):
        self.url = "https://www.azlyrics.com/lyrics/" + self.artist + "/" + self.song_name + ".html"
        response = requests.get(self.url)


        # TBH I don't think this line is doing anything
        lyrics = ""

        # DO NOT TOUCH BELOW CODE, IT WORKS -- Oh it modifies the not-so-beutiful soup into usable data --
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            lyrics_div = soup.find("div", attrs={"class": lyrics, "id": None})
            lyrics_div_in_lines = lyrics_div.stripped_strings
            lyrics_more_towards_text = []
            for line in lyrics_div_in_lines:
                if not line: 
                    continue
                lyrics_more_towards_text.append(line)

            lyrics_looking_like_lyrics = '\n'.join(lyrics_more_towards_text)
            
            pattern = r'\(([^)]*)\)'
            lyrics_without_some_silly_symbols = re.sub(pattern, r'\1', lyrics_looking_like_lyrics)
            lyrics_as_c_strings = lyrics_without_some_silly_symbols.split("\n")
            lyrics_array = []
            for line in lyrics_as_c_strings:
                lyrics_array.append(str(line).split(" "))
            
            return lyrics_array
        else:
            return f"Error {response.status_code}"
        # DO NOT TOUCH ABOVE CODE, IT WORKS -- Oh it modifies the not-so-beutiful soup into usable data --
    
    

if __name__ == "__main__":
    main()

# "".isalnum() -- WILL BE USEFUL FOR REMOVING ALT CHARACTER LINES WHEN SELECTING SONG LINES FOR THE GAME, SINCE THEY WON'T BE FUN
# OR MAYBE NOT COS OF COMMA'S AND STUFF -- SQUASH THIS BUG AT SOME POINT
    


    