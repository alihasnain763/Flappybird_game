from asyncio.windows_utils import pipe
import random #for generating random numbers
import sys
from unittest.main import main
import pygame
from pygame.locals import *  #basic pygame imports

# Global variables for the game

FPS = 32
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'gallery/sprites/bird.png'
BACKGROUND = 'gallery/sprites/background.png'
PIPE = 'gallery/sprites/pipe.png'

def welcomeScreen():
    '''
    Shows welcome images on the screeen
    '''
    playersx = int(SCREENWIDTH/5)
    playersy = int((SCREENHEIGHT - GAME_SPRITES['player'].get_hight())/2)
    messagex = int((SCREENHEIGHT - GAME_SPRITES['message'].get_hight())/2)
    messagey = int((SCREENHEIGHT * 0.13))
    basex = 0
    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, close the game
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

                # if the user presses space or up key, start the game for them
            elif event.type == KEYDOWN and (event.key== K_SPACE or event.key == K_UP):
                    return
            else:
                    SCREEN.blit(GAME_SPRITES['background'], (0, 0))
                    SCREEN.blit(GAME_SPRITES['player'], (playersx,playersy))
                    SCREEN.blit(GAME_SPRITES['nessage'], (messagex,messagey))
                    SCREEN.blit(GAME_SPRITES['base'], (basex,GROUNDY))
                    pygame.display.update()
                    FPSCLOSCK.tick(FPS)

    def mainGame():
        score = 9
        playersx = int(SCREENWIDTH/5)
        playersy = int(SCREENWIDTH/2)
        basex = 0

        #create two pipes for blitting on the screen
        newPipe1 = getRandomPipe()
        newPipe2 = getRandomPipe()

        #my list of upper pipes
        upperpipes = [
            {'x': SCREENWIDTH+200, 'y': newpipe1[0]['y']},
            {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y': newpipe2[1]['y']}
        ]
        #my list of lower pipes
        lowerpipes = [
            {'x': SCREENWIDTH+200, 'y': newpipe1[0]['y']},
            {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y': newpipe2[1]['y']}
        ]
        pipeVelX = -4

        playerVely = -9
        playerMaxVely = 10
        playerMinVely = -8
        playerAccVely = 1

        playerflapAccv -8 #velocity while flapping
        playerflapped = False  # It is true only when  the bird is flapping

        while True:
            for event in pygame.event.get():
               if event.type ==QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                   pygame.quit()
                   sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                    if playery> 0:
                        playersyVelY = playerFlapAccv
                        playerFlapped = True
                        GAME_SOUNDS['wing'].play()

            crashTest = isCollido(playerx, playery , upperPipes , lowerPipes) #this function will return true if player is crashed
            if crashtest:
                return            

            # check for score
            playerMidpos = playerx = GAME_SPRITES['player'].get_width()/2
            for pipe in upperPipes:
                pipeMidpos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width()/2
                if pipeMidpos<=playerMidpos < pipeMidpos +4:
                    score == 1
                    print(f'your score is {score}')
                    GAME_SPRITES['poing'].play()


            if playerVelY < playerMaxVelY and not playerFlapped:
                playerVelY == playerAccY

            if playerFlapped:
                playerFlapped = False

            playerHeight = GAME_SPRITES['player'].get_height()
            playery = playery + min(playerVely, GROUNDY -  playery - playerHeight)

            #move pipes to the left
            for upperPipe , lowerpipe in zip(upperPipes, lowerPipes):
                upperPipe['x'] += pipeVelX
                lowerPipe['x'] += pipeVelX

            # Add a new pipe when the first is about to cross the leftmost part of the screen
            if 0<upperPipes[0]['x']<5:
                newpipe = getRandomPipe()
                upperPipes.append(newpipe[0])
                lowerPipes.append(newpipe[1])


            # if the pipe is out of the screen, remove it
            if upperPipes[0]['x'] < -GAME_SPRITES["pipe"][0].get_width():
                upperpipes.pop()
                lowerpipes.pop()

            #lets blit our sprites now
            SCREEN.blit(GAME_SPRITES['background'], (0, 0))
            for upperPipe , lowerpipe in zip(upperPipes, lowerPipes):
                SCREEN.blit(GAME_SPRITES['pipe'][0], (upperpipe['x'], upperpipe['y']))
                SCREEN.blit(GAME_SPRITES['pipe'][1], (lowerpipe['x'], lowerpipe['y']))

            SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
            SCREEN.blit(GAME_SPRITES['player'], (playersx, playersy))
            myDigits = [int(x) or x in list(str(score))]
            width = 0
            for digit in myDigits:
                width += GAME_SPRITES['numbers'][digit].get_width()
            Xoffset = (SCREENWIDTH - width)/2

            for digit in myDigits:
                SCREEN.blit(GAME_SPRITES['numbers'][digit],(Xoffet, SCREENHEIGHT*0.12))
                Xoffset +=  GAME_SPRITES['numbers'][digit].get_width()
            pygame.display.update()
            FPSCLOSCKS.tick(FPS)

    def iscollide(playerx, playery , upperPipes , lowerPipes):
        return False

            
                

    

    def getRandomPipe():
         '''
         generate posiyions of two pipes(one bttom straight and one toprotated )
          for blitinh on the screen
         '''
     
         pipeHeight = GAME_SPRITES['pipe'][0].get_height()
         offset = SCREENWIDTH/3
         y2 = offset + random.randrange(0 , int(SCREENHEIGHT - GAME_SPRITES['base'],get_hight()  - 1.2 *offset))
         pipeX = SCREENWIDTH + 10
         y1 = pipeHeight - y2 = offset
         pipe =
          [
             {'x': pipeX, 'y': y1}
             {'x': pipeX, 'y': y2}
             ]
         return pipe



                    


if __name__ == "__main__":
    # this will the main point from where the game w ill start
    pygame.init()
    FPSCLOSCK = pygame.time.Clock()
    pygame.display.set_caption("flappy bird by Ali")
    GAME_SPRITES['numbers'] = (
        pygame.image.load('gallery/sprites/0.png').convert_alpha(),
        pygame.image.load('gallery/sprites/1.png').convert_alpha(),
        pygame.image.load('gallery/sprites/2.png').convert_alpha(),
        pygame.image.load('gallery/sprites/3.png').convert_alpha(),
        pygame.image.load('gallery/sprites/4.png').convert_alpha(),
        pygame.image.load('gallery/sprites/5.png').convert_alpha(),
        pygame.image.load('gallery/sprites/6.png').convert_alpha(),
        pygame.image.load('gallery/sprites/7.png').convert_alpha(),
        pygame.image.load('gallery/sprites/8.png').convert_alpha(),
        pygame.image.load('gallery/sprites/9.png').convert_alpha(),
    )
    GAME_SPRITES['message'] = pygame.image.load('gallery/sprites/message.png').convert_alpha()
    GAME_SPRITES['base'] = pygame.image.load('gallery/sprites/base.png').convert_alpha()
    GAME_SPRITES['pipe'] =(pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(),180),
     pygame.image.load(PIPE).convert_alpha()
    )

    # Game sounds
    GAME_SOUNDS['die'] = pygame.mixer.Sound('gallery/audio/die.wav')
    GAME_SOUNDS['hit'] = pygame.mixer.Sound('gallery/audio/hit.wav')
    GAME_SOUNDS['point'] = pygame.mixer.Sound('gallery/audio/point.wav')
    GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('gallery/audio/swoosh.wav')
    GAME_SOUNDS['wing'] = pygame.mixer.Sound('gallery/audio/wing.wav')
  

    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()

    while True:
        welcomScreen() #shows welcome screen to the user untill he presses the button
        mainGame() #this is main game
    
