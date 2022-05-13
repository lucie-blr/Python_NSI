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
'EEEEEEEEEEEEEETTTTTTTTTTTTTEETTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT',
'EEEEEEEEEEEEET             TT                                    W                                        WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWEEEEEEEEEEEEEEEEEEEEEEE',
'EEEEEEEEEEETT                                                    W   L                                     WWWWWWWWWWAAAAAAWWAAAAAAWWWWWWWWWEEEEEEEEEEEEEEEEEEEEEEE',
'EEEEEEEEEET                                                      W  WWWW                                   WWWWWAAAAAAAAAAAAAAAAAAAAAAAAWWWWEEEEEEEEEEEEEEEEEEEEEEE',                                                                                                                
'EEEEEEEEEG                                                       W  W→                                      WWWAAAAAAAAVVAAAAAAVVAAAAAAAAWWWEEEEEEEEEEEEEEEEEEEEEEE',
'EEEEEEEEEEG                                                      W  W→                                      WWAAAAAAAAAAAAAAAAAAAAAAAAAAAAWWEEEEEEEEEEEEEEEEEEEEEEE',
'EEEEEEEEEEE                                                      W  W→                                      WWAAAAAAAAAAAAAAAAAAAAAAAAAAAAWWEEEEEEEEEEEEEEEEEEEEEEE',
'EEEEEEEEEEEG                                                     W  W→                    W                 WAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWEEEEEEEEEEEEEEEEEEEEEEE',
'WEEEEEEEEEEE                                                     W  W→                    W                 WAAAAA  AAAAAAA  AAAAAAA  AAAAAWEEEEEEEEEEEEEEEEEEEEEEE',
'WWEEEEEEEEEE         P                     W                     W  W→                    W    WUUW         W          AA      AA          WEEEEEEEEEEEEEEEEEEEEEEE',
'AWEEEEEEEEEEG                U             W                        W→             W   W  W                 D          AA      AA    F     WEEEEEEEEEEEEEEEEEEEEEEE',
'AWWEEEEEEEEEEG       L  U    U        L    W               L        W↑↑↑↑↑↑        W↑↑↑W↑↑W   ↑↑↑↑↑↑↑↑↑↑         L     AAM M M AA          WEEEEEEEEEEEEEEEEEEEEEEE',
'AAWWEEEEEEEEEEWGGGGGGGGGGGGGGEGGGGGGGGGGGGGEGGGGGGGEGGGGGGGGGGGGGGGGEGGGGGGGGGGGGGGEGGGEGGEG  GGGGGGGGGG  GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGEEEEEEEEEEEEEEEEEEEEEEEE',
'AAAWEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE       K      EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
'WAAWEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE              EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
'WAAWWEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEGGGGGGGGGGGGGGEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
'WAAAWEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
'WAAAWWEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
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
'   EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE   D        K  K D EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
'   EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE       M           EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE',
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