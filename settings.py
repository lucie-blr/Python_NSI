import pygame, os

levelmap=[  [ #le joueur voit par paquet de dix lignes
'WTTTTTTTT    TTTTTTTTTTTTTTTTTTTT',
'W       W    W                   ',
'W       W    W          W        ',
'W       W    W         GGGG      ',
'W       W    W                   ',
'W       W    W                   ',
'W       W    W                   ',
'W       W    W           Y       ',
'W P                      Y       ',
'W                        Y       ',
'',
'',
'',
'WGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG',
'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
'WGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG',
'',
'',
'',
'SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS',
'B'],
[
'   WTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT',
'                                                                                                                 ',
'   W                                                     L                                                       ',
'   W                                                    WWWW                                                     ',                                                                                                                
'   W                                                    W                                                        ',
'   W                                                    W                                                        ',
'   W                                                    W                                                        ',
'   W                                                    W                     W                                  ',
'   W                                                    W                     W                                  ',
'   W          P                        W                W                     W    WWWW                          ',
'   W                                   W                W              W   W  W                                  ',
'   W          L     F     W      L     W       L        WSSSSSS        WSSSWSSW   SSSSSSSSSS          F                       ',
'   GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG  GGGGGGGGGG  GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG',
'   EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE              EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
'   EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE              EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
'   WGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG                                            GGGGGGGGGGGGGG',
'   ',
'   ',
'   ',
'SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS',
'B']   ]



tile_size = 48

def import_folder(path):
    surface_list = []
    for _,__,img_files in os.walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
    return surface_list