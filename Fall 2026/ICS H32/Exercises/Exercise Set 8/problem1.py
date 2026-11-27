import pygame


def _draw_text(surface: pygame.Surface, font: pygame.font.SysFont, text: str) -> None:
    text_image = font.render(text, True, pygame.Color(255, 255, 255))
    surface.blit(text_image, (10, 10))

def _keys_to_text(pressedkeys) -> str:
    chars = []

    for key in pressedkeys:
        if pygame.K_0 <= key <= pygame.K_9:
            chars.append(chr(key))
        elif pygame.K_a <= key <= pygame.K_z:
            chars.append(chr(key).upper())

    chars.sort()

    ans = ""
    for c in chars:
        ans += c
    return ans


def run() -> None:
    pygame.init()

    try:
        surface = pygame.display.set_mode((600, 600))
        font = pygame.font.SysFont(None, 24)
        clock = pygame.time.Clock()

        pressedKeys = []

        running = True

        while running:
            clock.tick(30)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
                elif event.type == pygame.KEYDOWN:
                    if event.key not in pressedKeys:
                        pressedKeys.append(event.key)
                elif event.type == pygame.KEYUP:
                    if event.key in pressedKeys:
                        pressedKeys.remove(event.key)

            surface.fill(pygame.Color(128, 128, 128))

            _draw_text(surface, font, _keys_to_text(pressedKeys))
            
            pygame.display.flip()
    finally:
        pygame.quit()


if __name__ == '__main__':
    run()
