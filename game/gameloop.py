import pygame
import sys

# Initialize pygame
pygame.init()

# Game config
GAME_TITLE="Evolutionary Heroes"
# GAME_ICON="game.fav"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.display.set_caption(GAME_TITLE)
# icon = pygame.image.load(GAME_ICON)
# pygame.display.set_icon(icon)
GAME_SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Fonte
font = pygame.font.SysFont("arial", 20)

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
CARD_COLOR = (100, 150, 200)

assets = "../assets/ui_pack_rpg/PNG/"

# Configurações das barras de vida
# Colors: Blue, Green, Red, Yellow
# Orientation: vertical, horizontal
# Parts: left, color, right
# sentence: f"bar{color}_{orientation}{position}"
# loading health bar sprites
# Background
back_bar_left = pygame.image.load(assets+"barBack_horizontalLeft.png").convert_alpha()
back_bar_middle = pygame.image.load(assets+"barBack_horizontalMid.png").convert_alpha()
back_bar_right = pygame.image.load(assets+"barBack_horizontalRight.png").convert_alpha()
# Blue
blue_bar_left = pygame.image.load(assets+"barBlue_horizontalLeft.png").convert_alpha()
blue_bar_middle = pygame.image.load(assets+"barBlue_horizontalBlue.png").convert_alpha()
blue_bar_right = pygame.image.load(assets+"barBlue_horizontalRight.png").convert_alpha()

BAR_SPACING = 20  # Espaçamento seguro para os lados da barra
BAR_HEIGHT = blue_bar_left.get_height()
HEALTHBAR_SECTION_WIDTH = blue_bar_middle.get_width() * 8 + blue_bar_left.get_width() + blue_bar_right.get_width()

# Configurações dos cards
CARD_PADDING = 20
CARD_CORNER_RADIUS = 15
CARD_WIDTH = HEALTHBAR_SECTION_WIDTH + BAR_SPACING * 2  # Baseado na largura da barra
CARD_HEIGHT = 200  # Altura permanece constante

# Função para desenhar cards com bordas arredondadas
def draw_rounded_rect(surface, color, rect, corner_radius):
    pygame.draw.rect(surface, color, rect, border_radius=corner_radius)

# Lista de heróis
heroes = [f"Hero {i+1}" for i in range(1)]

# TODO: use this icon to show current selection
# arrow_select_icon = pygame.image.load("arrowBeige_right.png")

# function to draw health bars
# TODO: add color as parameter
# TODO: add percentage as parameter
def draw_health_bar(surface, x, y, cardwidth):
    # always 10 bar sections
    max_health_sections = 10
    # horizontally centralize card
    bar_x = x + (cardwidth - HEALTHBAR_SECTION_WIDTH) // 2
    # 10 px above the car bottom
    bar_y = y + CARD_HEIGHT - BAR_HEIGHT - 10

    # draw sprites
    for i in range(max_health_sections):
        # the offset is meant to be this way because sprites
        # were not equal width
        # first part
        if i == 0:
            surface.blit(back_bar_left, (bar_x + i * blue_bar_middle.get_width(), bar_y))
            surface.blit(blue_bar_left, (bar_x + i * blue_bar_middle.get_width(), bar_y))
        # last part
        elif i == max_health_sections - 1:
            offset = blue_bar_left.get_width() + (i-1) * blue_bar_middle.get_width()
            surface.blit(back_bar_right, (bar_x + offset, bar_y))
            surface.blit(blue_bar_right, (bar_x + offset, bar_y))
        # middle parts
        else:
            offset = blue_bar_left.get_width() + (i-1) * blue_bar_middle.get_width()
            surface.blit(back_bar_middle, (bar_x + offset, bar_y))
            surface.blit(blue_bar_middle, (bar_x + offset, bar_y))

def draw_hero_card(hero, x: float, y: float):
    # Desenhar o card
    draw_rounded_rect(GAME_SCREEN, CARD_COLOR, (x, y, CARD_WIDTH, CARD_HEIGHT), CARD_CORNER_RADIUS)

    # Adicionar o nome do herói acima do card
    text = font.render(hero, True, BLACK)
    text_rect = text.get_rect(center=(x + CARD_WIDTH // 2, y - 10))
    GAME_SCREEN.blit(text, text_rect)
    
    # Desenhar a barra de vida
    draw_health_bar(GAME_SCREEN, x, y, CARD_WIDTH)

def draw_hero_cards():
    num_heroes = len(heroes)
    # Dividir heróis entre as 2 linhas
    max_per_row = (num_heroes + 1) // 2

    # Determinar espaçamento entre os cards e centralização
    row_width = max_per_row * (CARD_WIDTH + CARD_PADDING) - CARD_PADDING
    start_x = (SCREEN_WIDTH - row_width) // 2  # Centralizar horizontalmente
    start_y = (SCREEN_HEIGHT - (2 * (CARD_HEIGHT + CARD_PADDING))) // 2  # Centralizar verticalmente

    # Desenhando os cards
    for index, hero in enumerate(heroes):
        row = index // max_per_row  # Determinar linha (0 ou 1)
        col = index % max_per_row  # Determinar coluna
        x = start_x + col * (CARD_WIDTH + CARD_PADDING)
        y = start_y + row * (CARD_HEIGHT + CARD_PADDING)
    
        draw_hero_card(hero, x, y)

# Draw User Interface
def draw_ui():
    draw_hero_cards()

# Game loop
def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        GAME_SCREEN.fill(WHITE)  # Fundo branco

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_ui()
        
        # Atualizar a tela
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
