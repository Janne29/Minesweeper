import pygame
from assets import window, sprites
import game


def main():
    global SCREEN, CLOCK, RUNNING
    pygame.init()
    pygame.display.set_caption(window.title)
    SCREEN = pygame.display.set_mode(window.resolution)
    CLOCK = pygame.time.Clock()
    RUNNING = True
    game.createGrid()
    grid.draw()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            elif RUNNING == False: continue

            elif event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 1:  
                    if click.left(pygame.mouse.get_pos()) == False:
                        RUNNING = False
                elif event.button == 3:  
                    click.right(pygame.mouse.get_pos())

        pygame.display.update()




class click: 

    def left(pos):

        res = game.click_tile(pos)

        if res == False:
            grid.showBombs()
            return False
        
        if res == True:
            grid.draw()
            pygame.time.wait(200)
            grid.showSmileys()
            return False
        
        grid.draw()


    def right(pos):
        game.place_flag(pos)
        grid.draw()
    

class grid:

    def draw():

        tile_size = window.tile_size

        for x in range(16):
            for y in range(16):

                if game.grid[x][y] in ('', 'bomb'):
                    SCREEN.blit(sprites.tile, (x * tile_size, y * tile_size, tile_size, tile_size))
                
                if game.grid[x][y] == 0:
                    SCREEN.blit(sprites.empty, (x * tile_size, y * tile_size, tile_size, tile_size))
                
                if game.grid[x][y] in game.numbers:
                    number = sprites.numbers[game.grid[x][y] - 1] 
                    SCREEN.blit(getattr(sprites, number), (x * tile_size, y * tile_size, tile_size, tile_size))
                
                elif game.grid[x][y] == 'empty':
                    SCREEN.blit(sprites.empty, (x * tile_size, y * tile_size, tile_size, tile_size))

                elif game.grid[x][y] in ('flag', 'flagged_bomb'):
                    SCREEN.blit(sprites.flag, (x * tile_size, y * tile_size, tile_size, tile_size))

    def showBombs():

        tile_size = window.tile_size

        for x in range(16):
            for y in range(16):

                if game.grid[x][y] in ('flagged_bomb', 'bomb'):
                    SCREEN.blit(sprites.bomb, (x * tile_size, y * tile_size, tile_size, tile_size))

                elif game.grid[x][y] == 'exploded_bomb':
                    SCREEN.blit(sprites.explode, (x * tile_size, y * tile_size, tile_size, tile_size))
    
    def showSmileys():

        tile_size = window.tile_size

        for x in range(16):
            for y in range(16):

                if game.grid[x][y] in ('flagged_bomb', 'bomb'):
                    SCREEN.blit(sprites.smiley, (x * tile_size, y * tile_size, tile_size, tile_size))

main()
