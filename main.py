import pygame
import requests
from bs4 import BeautifulSoup
import re
import random
import math
import os

def main():

    run_game()

def run_game():
    pygame.init()
    width, height = 1280, 720
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Guess The Lyrics")
    running = True
    user_input = ""
    font_for_user_input = pygame.font.Font(None, 32)
    text_remover_rect = pygame.Rect(0, height - 100, width, 100)
    artist_selected = False
    song_selected = False
    artist = ""
    song = ""
    game_running = False
    
    while running:
        
        if artist_selected == False and user_input == "":
            draw_text(screen, font_for_user_input, "Enter Artist: ", width / 2 - 100, height - 100, "white")
        elif song_selected == False and user_input == "":
            draw_text(screen, font_for_user_input, "Enter Song: ", width / 2 - 100, height - 100, "white")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                raise SystemExit
            
            if event.type == pygame.KEYDOWN:
                if user_input == "":
                    pygame.draw.rect(screen, "black", text_remover_rect)

                if event.key == pygame.K_RETURN:
                    if song_selected == False or artist_selected == False:
                        pygame.draw.rect(screen, "black", text_remover_rect)
                        if artist_selected == False:
                            artist = "".join(user_input.split(" ")).lower()
                            artist_selected = True
                            user_input = ""

                        elif song_selected == False:
                            song = "".join(user_input.split(" ")).lower()
                            song_selected = True

                            pygame.draw.rect(screen, "black", text_remover_rect)
                            draw_text(screen, font_for_user_input, "Searching for song....", width / 2 - 100, height - 100, "white")
                            pygame.display.flip()

                            song = Song(artist, song)

                            if song.lyrics == "Error 404":
                                pygame.draw.rect(screen, "black", text_remover_rect)
                                draw_text(screen, font_for_user_input, "Sorry, couldn't find the song - Please select another", width / 2 - 200, height - 100, "white")
                                pygame.display.flip()
                                pygame.time.wait(5000)
                                pygame.draw.rect(screen, "black", text_remover_rect)
                                artist_selected = False
                                song_selected = False
                                user_input =""
                                continue
                            else:
                                pygame.draw.rect(screen, "black", text_remover_rect)
                                draw_text(screen, font_for_user_input, f"Song found!      Artist: {song.artist}      Song: {song.song_name}", width / 2 - 250, height - 100, "white")
                                pygame.display.flip()
                                pygame.time.wait(5000)
                                running = False
                                game_running = True
                elif event.key == pygame.K_BACKSPACE:
                    if user_input != "":
                        user_input = ""
                        pygame.draw.rect(screen, "black", text_remover_rect)

                else:
                    print("key pressed")
                    user_input += event.unicode
                    draw_text(screen, font_for_user_input, user_input, width / 2 - 100, height - 100, "white")

        selected_lyrics = (random.choice(song.lyrics))
        amount_of_lyris_to_replace = math.ceil(len(selected_lyrics) / 3.3)

        indexs_to_replace = {}

        while len(indexs_to_replace) < amount_of_lyris_to_replace:
            index = random.randint(0, len(selected_lyrics) - 1)
            if index not in indexs_to_replace:
                indexs_to_replace[index] = selected_lyrics[index].lower()

        for index in indexs_to_replace:
            selected_lyrics[index] = "-" * len(selected_lyrics[index])

        while game_running:
            print("entering game state")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    raise SystemExit

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

        render_game(screen)
        pygame.display.flip()
        clock.tick(60)

def draw_text(screen, font, text, x, y, color):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def render_game(screen):
    TS_Background = pygame.image.load(os.path.join('Images', 'TS_Eras_Tour.jpg')).convert()
    screen.blit(TS_Background, (0, 0))
    pygame.TEXTINPUT = "Guess The Lyrics"
    pygame.display.flip()

class Song:
    def __init__(self, artist, song_name):
        self.artist = artist
        self.song_name = song_name
        self.lyrics = self.get_lyrics()
    
    def get_lyrics(self):
        self.url = "https://www.azlyrics.com/lyrics/" + self.artist + "/" + self.song_name + ".html"
        response = requests.get(self.url)

    # DO NOT MODIFY THE BELOW CODE
        # I think this line does nothing, but I'm not modifying this code
        lyrics = ""
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
    # DO NOT MODIFY THE ABOVE CODE
    
if __name__ == "__main__":
    main()