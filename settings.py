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
'   WTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT',
'                                                                                                W                              w',
'   W                                                     L                                      W                              W',
'   W                                                    WWWW                                    W                              W',                                                                                                                
'   W                                                    W→                                      W                              W',
'   W                                                    W→                                      W                              W',
'   W                                                    W→                                      W                              W',
'   W                                                    W→                    W                 W                              W',
'   W                                                    W→                    W                 W                              W',
'   W     P                             W                W→                    W    WWWW         W                              W',
'   W             W                     W                W→             W   W  W                 D                        F     W',
'   W     L       W        W      L     W       L        W↑↑↑↑↑↑        W↑↑↑W↑↑W   ↑↑↑↑↑↑↑↑↑↑         L       M M M             W',
'   GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG  GGGGGGGGGG  GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG',
'   EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE       K      EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
'   EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE              EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
'   WGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG                                            GGGGGGGGGGGGGG',
'   ',
'   ',
'   ',
'SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS',
'B'],
[
'   UTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT',
'   U                                                     W        W                                                                      ',
'   U                                                     W        W                                                                      ',
'   U       GG     WWW                                    W        W                                                                      ',                                                                                                                
'   U           W  W                w                     W        W                                                                       ',
'   U           ↓  U                W         W           W        WWWWWWW                                                                        ',
'   UGGG          ←U                W   WW                W           D                                                                    ',
'   UE   W   W     U                W                   K U                                                                              ',
'   U              U             W                 W      U        WWWWWWW                                                                      ',
'   U     P        U  WW                       W       WWWW                                                                               ',
'   U U          GGG           W                                                                                                         ',
'   U U      ↑↑↑↑EEE↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑   ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑ W↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑                                                                                                                          ',
'   GGGGGGGGGGGGGEEEGGGGGGGGGGGGGGGGGGGGGGGGG   GGGGGGGGGGGGGGG EGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG',
'   EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE   D   M    K  K D EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
'   EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE                   EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
'   EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE                                            GGGGGGGGGGGGGG',
'   ',
'   ',
'   ',
'SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS',
'B']   ]
levelsign = [[],
["Keep calm, but the spikes can kill you.","Press directional keys to move.","You can also make double jump.","As you can double jump, you can climb the walls.","Use your fucking gun to shoot the mobs."],
[]]


tile_size = 48

def import_folder(path):
    surface_list = []
    for _,__,img_files in os.walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
    return surface_list