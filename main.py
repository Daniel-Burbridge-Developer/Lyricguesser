import pygame
import requests
from bs4 import BeautifulSoup
import re
import random
import math
import os

def main():

    run_game()
    
    # while True:
    #     artist = "".join(input("Enter artist: ").split(" ")).lower()
    #     song = "".join(input("Enter song: ").split(" ")).lower()
    #     song = Song(artist, song)
    #     if song.lyrics == "Error 404":
    #         print("Sorry, couldn't find the song - Please select another")
    #     else:
    #         break
    # print("\n")

    # random.choice(song.lyrics)
    # selected_lyrics = (random.choice(song.lyrics))
    # amount_of_lyris_to_replace = math.ceil(len(selected_lyrics) / 3.3)

    # indexs_to_replace = {}

    # while len(indexs_to_replace) < amount_of_lyris_to_replace:
    #     index = random.randint(0, len(selected_lyrics) - 1)
    #     if index not in indexs_to_replace:
    #         indexs_to_replace[index] = selected_lyrics[index].lower()

    # for index in indexs_to_replace:
    #     selected_lyrics[index] = "_" * len(selected_lyrics[index])

    # while True:
    #     if len(indexs_to_replace) == 0:
    #         break
    #     print(" ".join(selected_lyrics))
    #     print(indexs_to_replace)
    #     guess = input("Enter guess: ").lower()
    #     if guess in indexs_to_replace.values():
    #         replace_index = None
    #         for index in indexs_to_replace:
    #             if indexs_to_replace[index] == guess:
    #                 selected_lyrics[index] = guess
    #                 replace_index = index
    #                 break
    #         indexs_to_replace.pop(replace_index)

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                raise SystemExit
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print("Enter Key Pressed!")


        render_game(screen)
        calc_logic()
        pygame.display.flip()
        clock.tick(60)

def render_game(screen):
    TS_Background = pygame.image.load(os.path.join('Images', 'TS_Eras_Tour.jpg')).convert()
    screen.blit(TS_Background, (0, 0))
    # pygame.TEXTINPUT = "Enter Guess"

def calc_logic():
    pass
    

            


class Song:
    def __init__(self, artist, song_name):
        self.artist = artist
        self.song_name = song_name
        self.lyrics = self.get_lyrics()
    

    # This took a fair few hours - but don't modify it, it's working well enough now. just leave it as it.
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
    # This took a fair few hours - but don't modify it, it's working well enough now. just leave it as it.
    
    

if __name__ == "__main__":
    main()

# "".isalnum() -- WILL BE USEFUL FOR REMOVING ALT CHARACTER LINES WHEN SELECTING SONG LINES FOR THE GAME, SINCE THEY WON'T BE FUN
# OR MAYBE NOT COS OF COMMA'S AND STUFF -- SQUASH THIS BUG AT SOME POINT
# I broke git, trying to fix it now