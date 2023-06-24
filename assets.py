import pygame

class window:
    title = "Minesweeper"
    resolution = (640, 640)
    tile_size = 40

class sprites:

    resolution = (window.tile_size, window.tile_size)
    tile = pygame.transform.scale( pygame.image.load('assets/tile.png') , resolution )
    empty = pygame.transform.scale( pygame.image.load('assets/empty.png') , resolution )
    bomb = pygame.transform.scale( pygame.image.load('assets/bomb.png') , resolution )
    flag = pygame.transform.scale( pygame.image.load('assets/flag.png') , resolution )
    explode = pygame.transform.scale( pygame.image.load('assets/explode.png') , resolution )
    smiley = pygame.transform.scale( pygame.image.load('assets/smiley.png') , resolution )
    bomb_smiley = pygame.transform.scale( pygame.image.load('assets/bomb_smiley.png') , resolution )

    one = pygame.transform.scale( pygame.image.load('assets/1.png') , resolution )
    two = pygame.transform.scale( pygame.image.load('assets/2.png') , resolution )
    three = pygame.transform.scale( pygame.image.load('assets/3.png') , resolution )
    four = pygame.transform.scale( pygame.image.load('assets/4.png') , resolution )
    five = pygame.transform.scale( pygame.image.load('assets/5.png') , resolution )
    six = pygame.transform.scale( pygame.image.load('assets/6.png') , resolution )
    seven = pygame.transform.scale( pygame.image.load('assets/7.png') , resolution )
    eight = pygame.transform.scale( pygame.image.load('assets/8.png') , resolution )

    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',]