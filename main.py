import pygame
import requests
from bs4 import BeautifulSoup
import re

def main():

    # game = GameEngine()
    # game.run()

    # artist = "".join(input("Enter artist: ").split(" ")).lower()
    # song = "".join(input("Enter song: ").split(" ")).lower()
    
    artist="taylorswift"
    song="22"

    song = Song(artist, song)

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
        print("\n".join(self.lyrics))
    
    def get_lyrics(self):
        self.url = "https://www.azlyrics.com/lyrics/" + self.artist + "/" + self.song_name + ".html"
        response = requests.get(self.url)

        lyrics = ""

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            lyrics = soup.find("div", attrs={"class": lyrics, "id": None})
            lines = lyrics.stripped_strings
            lyricsmod = []
            for line in lines:
                if not line: 
                    continue
                lyricsmod.append(line)

            newestlyrics = '\n'.join(lyricsmod)
            
            pattern = r'\(([^)]*)\)'
            modified_text = re.sub(pattern, r'\1', newestlyrics)
            return (modified_text).split("\n")
        else:
            return f"Error {response.status_code}"
 
    
    

if __name__ == "__main__":
    main()

#isalnum -- WILL BE USEFUL FOR REMOVING ALT CHARACTERS WHEN SELECTING SONG LINES FOR THE GAME, SINCE THEY WON'T BE FUN