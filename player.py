import pygame
import time
import os
from settings import import_folder


class Player(pygame.sprite.Sprite): #Création de la class
    def __init__(self,pos): #Fonction qui se lance à la première utilisation de la class
        super().__init__() 
        self.import_character_assets() #Importation des différentes images de l'objet
        self.frame_index = 0 #Définition de la "frame index" qui servira à l'animation
        self.animation_speed = 0.15 #Définition de la vitesse de défilement des images dans une animation
        self.image = self.animations['idle'][self.frame_index] #Définition de la première animation du personnage
        self.rect = self.image.get_rect(topleft = pos) #Définition de la position de l'objet
        self.status = 'idle' #Définition du status de l'objet, qui servira dans à l'animation
        self.facing_right = True #Définition de l'orientation de l'image
        self.death = 0 #Définition de la valeur d'animation de mort
        self.win = False #Définition de si le joueur a gagné ou pas
        self.bullet = False
        self.key = 0
        
        #mouvement
        self.direction = pygame.math.Vector2(0,0) #Définition de la direction du perosnnage
        self.speed = 5 #Définition de la vitesse du personnage
        self.gravity = 0.8 #Définition de la gravité 
        self.jump_speed = -12 #Définition de la vitesse de saut
        self.double_jump = 1 #Définition de la quantité de double saut qu'à le joueur
        self.time = time.time() #Définition du cooldown du double saut via l'heure UNIX
    
    def import_character_assets(self): #Fonction qui importe toutes les images associées au personnage
        self.character_path='./alien/'
        self.animations = {'idle':[],'run':[],'jump':[],'fall':[], 'death':[]} #Définition des différents états d'animations
        
        
        for animation in self.animations.keys(): #Pour chaque état d'animation, on importe les informations des images
            self.full_path = self.character_path + animation
            self.animations[animation] = import_folder(self.full_path)
            
        
    
    def animate(self): #Fonction qui anime le personnage
        if self.status == "win": #Si le status du joueur est "win", défini la victoire du joueur comme vrai et met son status sur "idle"
            self.win = True
            self.status = 'idle'
        animation = self.animations[self.status] #Récupère la liste d'image du status du joueur
        if self.status == 'death': #Si le joueur est mort
            
            #Tant que la valeur d'animation de mort du joueur est inférieur à 20 
            if self.death < 20: 
                self.image = animation[int(self.death)] #défini l'image du joueur comme sa valeur d'animation de mort dans la liste d'images d'animation
                time.sleep(0.02) #attend 0.002 seconde
                
                self.death = self.death + 1 #rajoute 1 à la valeur d'animation de mort
                self.direction.x = 0 #défini sa direction en x sur 0
                self.direction.y = 0 #défini sa direction en y sur 0
            return
        elif self.win: #si le joueur a gagné et n'est pas mort
            if self.death < len(animation): #tant que la valeur d'animation de mort est inférieur au nombre d'image dans la liste d'images d'animation
                self.image = animation[0] #l'image du joueur est la première image de la liste d'image
                time.sleep(0.5) 
                
                self.death = self.death + 1 
                self.direction.x = 0 
                self.direction.y = 0
            return
        elif self.death == 0: #Si la valeur de mort vaut 0
            self.frame_index += self.animation_speed #Ajout au numéro de frame la vitesse d'animation
            if self.frame_index >= len(animation): #si le numéro de frame est supérieur ou égale à la taille de la liste d'image
                self.frame_index = 0 #le numéro d'image vaut 0
                            
            image = animation[int(self.frame_index)] #défini l'image à l'arrondi du numéro d'image
        
            if self.facing_right: #si le joueur est tourné vers la droite, retourner l'image
                flipped_image = pygame.transform.flip(image, True, False)
                self.image = flipped_image
            else:
                self.image = image
    
    def get_status(self): #récupération du status du joueur
        if self.death == 0: #si le joueur n'est pas mort
            if self.direction.y < 0: #si sa direction en y est supérieur à zéro, définir son status comme jump
                self.status = 'jump' 
            elif self.direction.y > 1: #si sa direction en y est inférieur à zéro, définir son status comme fall
                self.status = 'fall'
            elif self.direction.x != 0: #si sa direction e x est différente de zéro, définir son status comme run
                self.status = 'run'
            else: #sinon, définir son status comme idle
                self.status = 'idle'
    
    def get_input(self): #fonction qui récupère les touches pressées
        keys = pygame.key.get_pressed() #récupère les touches pressées
        
        if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]: #si flèche de droite et flèche de gauche sont pressés, définir la direction en x sur zéro
            self.direction.x=0
        
        elif keys[pygame.K_RIGHT]: #si la flèche de droite est pressée, définir sa direction en x sur 1 et s'il regarde à droite sur vraie
            self.direction.x = 1
            self.facing_right = True
        elif keys[pygame.K_LEFT]: #si la flèche de gauche est pressée, définir sa direction en x sur -1 et s'il regarde à droite sur faux
            self.direction.x = -1
            self.facing_right = False
        else: #sinon, définir sa direction en x sur zéro
            self.direction.x = 0
        
        if keys[pygame.K_UP] and self.double_jump == 1: #si le joueur appuie sur flèche du haut et qu'il a un double saut
            if self.direction.y == 0: #si sa direction en y vaut zéro, sauter
                self.jump()
            if self.direction.y != 0: #si sa direction est différente de zéro
                if time.time() > (self.time + 0.2): #si son temps actuel via l'heure UNIX avec 0.2 secondes de plus est supérieur au temps actuel via l'heure UNIX
                    self.double_jump = 0 #mettre le double jump sur 0
                    self.jump() #sauter
        
        if keys[pygame.K_SPACE]:
            self.bullet = True

        else:
            self.bullet = False
            
    def apply_gravity(self): #Application de la gravité
        self.direction.y += self.gravity #ajouter à la direction en y du joueur la gravité
        self.rect.y += self.direction.y #ajouter à la position en y la direction en y
    
    def jump(self): #Saut
        self.direction.y = self.jump_speed #Mettre la direction en y à la valeur de la vitesse de saut
    
    def update(self): #actualisation du joueur 
        if self.death == 0: #si le joueur n'est pas mort
            self.get_input() #récupérer les touches
        self.animate() #animer le joueur
        self.get_status() #récupérer le status du joueur
        self.rect.x += self.direction.x * self.speed #Ajouter à la position du joueur sa direction en x multiplié par sa vitesse
         
         
class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("./alien/bullet.png")
        self.rect = self.image.get_rect(topleft = pos)
        self.Ask_bullet = True
        self.speed = 15
        self.direction = pygame.math.Vector2(0,0)
        self.direction.x = 0


    def update(self):
        self.bullet
        self.rect.x += self.speed * self.direction.x


    def bullet(self, player):
        self.rect.x = player.rect.x
        self.rect.y = player.rect.y
        image = pygame.image.load("./alien/bullet.png")

        if player.facing_right == False:
            self.direction.x = -1
            flipped_image = pygame.transform.flip(image, True, False)
            self.image = flipped_image
            


        elif player.facing_right == True:
            self.direction.x = 1 
            self.image = image
                
                
            
#Tutoriel : Balle
#
#Quand tu tires la balle, tu dois définir une variable qui a comme valeur les secondes passées depuis l'heure UNIX (time.time())
#pour le cooldown, tu compares l'heure UNIX (time.time()) a la variable que tu as définis et à laquelle tu as ajouté x secondes 
#
#Pour vérifier la collision, tu regardes le code du joueur. Quand la balle touche un mur, tu mets la vitesse de la balle à zéro 
#et tu places la balle sous le sol