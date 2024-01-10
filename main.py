import pygame

def main():

    game = GameEngine()
    game.run()

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

if __name__ == "__main__":
    main()