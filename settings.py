import pygame, os

level_map = [
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'X                           ',
'X            X              ',
'X  P         X              ',
'X            X              ',
'X            X              ',
'X            X              ',
'X      XXXXX    XXXX        ',
'X     XXXXXX   XXXXX        ',
'X      XXXXX   XXXXX        ',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']
level_map_2 =[ #le joueur voit par paquet de dix lignes
'WTTTTTTTT    TTTTTTTTTTTTTTTTTTTT',
'W       W    W                   ',
'W       W    W          W        ',
'W       W    W         GGGG      ',
'W       W    W                   ',
'W       W    W                   ',
'W       W    W                   ',
'W       W    W                   ',
'W P                              ',
'W                                ',
'WGGGGGGGGGGGGGGGGGGGGGSSSGGGGGGGG',
'WGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG',
'WGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG',
'',
'',
'',
'',
'',
'',
'',
'',
'',
'SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS']


tile_size = 48
width = 1200
height = 600


def import_folder(path):
    surface_list = []
    for _,__,img_files in os.walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
    return surface_list